from datetime import datetime
from django.db import IntegrityError, transaction
from django.shortcuts import get_object_or_404, redirect, render
from accounts.forms import DireccionForm, OrdenTrabajoForm
from accounts.helpers import get_unica_organizacion
from accounts.models import Concepto, Cotizacion, Direccion, OrdenTrabajoConcepto
from django.contrib import messages
from accounts.forms import OrdenTrabajoForm, DireccionForm
from django.template.loader import render_to_string
from weasyprint import HTML
from django.core.files.base import ContentFile
from django.core.paginator import Paginator

# VISTA PRA DIRIGIR A INTERFAZ DE COTIZACIONES ACEPTADAS
def cotizaciones_aceptadas_list(request):
    # Notificación
    notificaciones = request.user.notificacion_set.all()
    notificaciones_no_leidas = notificaciones.filter(leido=False).count()
    
    # Parámetro de ordenamiento desde la URL
    order_by = request.GET.get('order_by', 'fecha_solicitud')  # Default order
    
    if not order_by:  # Asegura que siempre haya un valor válido para order_by
        order_by = 'fecha_solicitud'
    
    # Filtrar cotizaciones que están aceptadas
    cotizaciones = Cotizacion.objects.filter(estado=True).order_by(order_by)
    
    # Paginación
    paginator = Paginator(cotizaciones, 50) # Mostrar 50 cotizaciones aceptadas por página
    page_number = request.GET.get('page')
    cotizaciones_page = paginator.get_page(page_number)
    
    context = {
        'notificaciones': notificaciones,
        'notificaciones_no_leidas': notificaciones_no_leidas,
        'cotizaciones': cotizaciones,
        'cotizaciones_page': cotizaciones_page,  
        
        
    }
    return render(request, "accounts/cotizacionesAceptadas/cotizaciones_aceptadas.html", context)

# VISTA PARA CREAR ORDEN DE TRABAJO
def generar_orden_trabajo(request, pk):
    
    # Obtener la cotización según el ID proporcionado
    cotizacion = get_object_or_404(Cotizacion, id=pk)

    # Verificar que la cotización esté aceptada
    if not cotizacion.estado:
        messages.error(
            request, 'No se puede generar una orden de trabajo para una cotización no aceptada.')
        return redirect('cotizacion_detalle', pk=cotizacion.id)

    # Obtener los conceptos asociados a la cotización
    conceptos = Concepto.objects.filter(cotizacion=cotizacion)
    
    if request.method == 'POST':
        # Procesar los formularios enviados
        form = OrdenTrabajoForm(request.POST)
        direccion_form = DireccionForm(request.POST)
        if form.is_valid() and direccion_form.is_valid():
            try:
                with transaction.atomic():
                    # Crear una instancia de la orden de trabajo sin guardarla aún
                    orden_trabajo = form.save(commit=False)
                    direccion_data = direccion_form.cleaned_data
                    direccion_actual = cotizacion.persona.empresa.direccion

                    # Verificar si la dirección ha cambiado
                    if not all(direccion_data[key] == getattr(direccion_actual, key) for key in direccion_data):
                        # Crear una nueva dirección si los datos son diferentes
                        nueva_direccion = Direccion.objects.create(**direccion_data)
                        orden_trabajo.direccion = nueva_direccion
                    else:
                        # Usar la dirección actual si los datos no han cambiado
                        orden_trabajo.direccion = cotizacion.persona.empresa.direccion

                    # Verificar si el proyecto es a gestión
                    if 'proyecto_a_gestion' in request.POST:
                        orden_trabajo.gestion = True

                    # Asignar la cotización a la orden de trabajo
                    orden_trabajo.cotizacion = cotizacion
                    orden_trabajo.save()

                    # Filtrar los conceptos seleccionados
                    conceptos_orden_trabajo = []
                    for concepto in Concepto.objects.filter(cotizacion=cotizacion):
                        if f'usar_concepto_{concepto.id}' in request.POST:
                            # El concepto ha sido seleccionado para incluirse en la orden de trabajo
                            usar_otra_descripcion = request.POST.get(f'usar_otra_descripcion_{concepto.id}', 'off') == 'on'
                            descripcion_personalizada = request.POST.get(f'otra_descripcion_{concepto.id}', '').strip() if usar_otra_descripcion else None
                            
                            OrdenTrabajoConcepto.objects.create(
                                orden_de_trabajo=orden_trabajo,
                                concepto=concepto,
                                descripcion_personalizada=descripcion_personalizada
                            )
                            conceptos_orden_trabajo.append(concepto)
                            
                    # Generar el PDF
                    pdf_data = generar_pdf_orden_trabajo(request, orden_trabajo)
                    # Guardar el PDF en el modelo
                    orden_trabajo.orden_trabajo_pdf.save(f"orden_trabajo_{orden_trabajo.id_personalizado}.pdf", ContentFile(pdf_data))
                    orden_trabajo.save()
                    messages.success(request, 'Orden de trabajo generada exitosamente.')
                    return redirect('cotizacion_detalle', pk=cotizacion.id)
            except IntegrityError:
                messages.error(
                    request, 'Hubo un error al crear la orden de trabajo. Inténtalo de nuevo.')
        else:
            print(form.errors)
            print(direccion_form.errors)
            messages.error(
                request, 'Hubo un error en el formulario. Por favor, revisa los campos e intenta nuevamente.')
    else:
        direccion_initial_data = {
            'calle': cotizacion.persona.empresa.direccion.calle,
            'numero': cotizacion.persona.empresa.direccion.numero,
            'colonia': cotizacion.persona.empresa.direccion.colonia,
            'ciudad': cotizacion.persona.empresa.direccion.ciudad,
            'codigo': cotizacion.persona.empresa.direccion.codigo,
            'estado': cotizacion.persona.empresa.direccion.estado,
        }
        form = OrdenTrabajoForm()
        direccion_form = DireccionForm(initial=direccion_initial_data)
    context = {
        'form': form,
        'direccion_form': direccion_form,
        'cotizacion': cotizacion,
        'conceptos': conceptos,
    }
    return render(request, 'accounts/cotizacionesAceptadas/generar_orden_trabajo.html', context)

# VISTA PARA CREAR PDF DE ORDEN DE TRABAJO
def generar_pdf_orden_trabajo(request, orden_trabajo):
    # Asumimos que orden_trabajo es la instancia de OrdenDeTrabajo para la cual generar el PDF.
    conceptos_orden_trabajo = OrdenTrabajoConcepto.objects.filter(orden_de_trabajo=orden_trabajo)
    
    conceptos = Concepto.objects.filter(cotizacion=orden_trabajo.cotizacion)
    org = get_unica_organizacion()
    # Suponiendo que conceptos_seleccionados ya contiene los conceptos correctos con su descripción personalizada
    conceptos_data = [
        {
            'nombre': ctp.concepto.servicio.nombre_servicio,
            'metodo': ctp.concepto.servicio.metodo,
            'descripcion': ctp.concepto.servicio.descripcion,
            'cantidad': ctp.concepto.cantidad_servicios,
            'descripcion_personalizada': ctp.descripcion_personalizada if ctp.descripcion_personalizada else ctp.concepto.notas,
            'nota': ctp.concepto.notas,
        } 
        for ctp in conceptos_orden_trabajo
    ]

    context = {
        'org': get_unica_organizacion(),
        'formato': org.f_orden.nombre_formato,
        'version':org.f_orden.version,
        'emision':org.f_orden.emision.strftime("%Y/%m/%d"),
        'user': request.user if request.user.is_authenticated else None,
        'current_date': datetime.now().strftime("%Y/%m/%d"),
        'logo_url': request.build_absolute_uri('/static/img/logo.png'),
        'orden_trabajo': orden_trabajo,
        'conceptos_data': conceptos_data,
    }

    html_string = render_to_string(
        'accounts/cotizacionesAceptadas/orden_trabajo_plantilla.html', context)
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    pdf = html.write_pdf()

    return pdf
