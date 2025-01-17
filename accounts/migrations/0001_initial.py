# Generated by Django 5.0.7 on 2024-07-29 23:14

import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cotizacion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "id_personalizado",
                    models.CharField(blank=True, max_length=4, null=True, unique=True),
                ),
                ("fecha_solicitud", models.DateField()),
                ("fecha_caducidad", models.DateField()),
                (
                    "metodo_pago",
                    models.CharField(
                        choices=[
                            ("MXN", "MXN - Moneda Nacional Mexicana"),
                            ("USD", "USD - Dolar Estadunidense"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "tasa_iva",
                    models.DecimalField(decimal_places=2, default=0.16, max_digits=4),
                ),
                ("notas", models.TextField(blank=True, null=True)),
                ("correos_adicionales", models.TextField(blank=True, null=True)),
                (
                    "subtotal",
                    models.DecimalField(decimal_places=2, max_digits=10, null=True),
                ),
                (
                    "iva",
                    models.DecimalField(decimal_places=2, max_digits=10, null=True),
                ),
                (
                    "total",
                    models.DecimalField(decimal_places=2, max_digits=10, null=True),
                ),
                ("estado", models.BooleanField(default=False)),
                (
                    "cotizacion_pdf",
                    models.FileField(
                        blank=True, null=True, upload_to="cotizaciones_pdfs/"
                    ),
                ),
                (
                    "orden_pedido_pdf",
                    models.FileField(
                        blank=True, null=True, upload_to="ordenes_pedido_pdfs/"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Direccion",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("calle", models.CharField(max_length=50)),
                ("numero", models.CharField(max_length=50)),
                ("colonia", models.CharField(max_length=100)),
                ("ciudad", models.CharField(max_length=100)),
                ("codigo", models.CharField(max_length=6)),
                ("estado", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="FormatoCotizacion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre_formato", models.CharField(max_length=255)),
                ("version", models.CharField(max_length=50)),
                ("emision", models.DateField(default=django.utils.timezone.now)),
                ("terminos", models.TextField(blank=True)),
                ("avisos", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="FormatoOrden",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre_formato", models.CharField(max_length=255)),
                ("version", models.CharField(max_length=50)),
                ("emision", models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name="InformacionContacto",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("correo_electronico", models.EmailField(max_length=254)),
                ("telefono", models.CharField(blank=True, max_length=120)),
                ("celular", models.CharField(blank=True, max_length=20)),
                ("fax", models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Metodo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("metodo", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Titulo",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("titulo", models.CharField(max_length=50)),
                ("abreviatura", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("celular", models.CharField(blank=True, max_length=15, null=True)),
                (
                    "rol",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("admin", "Administrador"),
                            ("coordinador", "Coordinador"),
                            ("muestras", "Muestras"),
                            ("informes", "Informes"),
                            ("laboratorio", "Laboratorio"),
                            ("calidad", "Calidad"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Concepto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cantidad_servicios", models.IntegerField()),
                ("precio", models.DecimalField(decimal_places=2, max_digits=10)),
                ("notas", models.TextField(blank=True, null=True)),
                (
                    "cotizacion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="conceptos",
                        to="accounts.cotizacion",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Empresa",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("nombre_empresa", models.CharField(max_length=100)),
                ("rfc", models.CharField(blank=True, max_length=50)),
                (
                    "moneda",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("MXN", "MXN - Moneda Nacional Mexicana"),
                            ("USD", "USD - Dolar Estadunidense"),
                        ],
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "condiciones_pago",
                    models.CharField(blank=True, default="15", max_length=200),
                ),
                (
                    "direccion",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.direccion",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Notificacion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tipo", models.CharField(max_length=100)),
                ("mensaje", models.TextField()),
                ("enlace", models.URLField()),
                ("leido", models.BooleanField(default=False)),
                ("fecha_creacion", models.DateTimeField(auto_now_add=True)),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-fecha_creacion"],
            },
        ),
        migrations.CreateModel(
            name="OrdenTrabajo",
            fields=[
                (
                    "id_personalizado",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("estado", models.BooleanField(default=False)),
                ("fecha_creacion", models.DateTimeField(auto_now_add=True)),
                ("fecha_actualizacion", models.DateTimeField(auto_now=True)),
                ("gestion", models.BooleanField(default=False)),
                (
                    "orden_trabajo_pdf",
                    models.FileField(
                        blank=True, null=True, upload_to="ordenes_trabajo_pdfs/"
                    ),
                ),
                (
                    "cotizacion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orden_trabajo",
                        to="accounts.cotizacion",
                    ),
                ),
                (
                    "direccion",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ordenes_trabajo",
                        to="accounts.direccion",
                    ),
                ),
                (
                    "receptor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="ordenes_trabajo",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrdenTrabajoConcepto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("descripcion_personalizada", models.TextField(blank=True, null=True)),
                (
                    "concepto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.concepto",
                    ),
                ),
                (
                    "orden_de_trabajo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="conceptos",
                        to="accounts.ordentrabajo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Organizacion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre",
                    models.CharField(
                        default="Ingenieria y Administración Estratégica, S.A. de C.V.",
                        max_length=255,
                    ),
                ),
                (
                    "direccion",
                    models.CharField(
                        default="Calle Puebla, No. 4990, col. Guillen, Tijuana BC, México, C.P. 22106",
                        max_length=255,
                    ),
                ),
                (
                    "telefono",
                    models.CharField(default="(664) 104 51 44", max_length=20),
                ),
                ("pagina_web", models.URLField()),
                (
                    "f_cotizacion",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="formatos",
                        to="accounts.formatocotizacion",
                    ),
                ),
                (
                    "f_orden",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="formatos",
                        to="accounts.formatoorden",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Persona",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=50)),
                ("apellidos", models.CharField(max_length=100)),
                ("activo", models.BooleanField(default=True)),
                (
                    "empresa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.empresa",
                    ),
                ),
                (
                    "informacion_contacto",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="accounts.informacioncontacto",
                    ),
                ),
                (
                    "titulo",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="accounts.titulo",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="cotizacion",
            name="persona",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="accounts.persona",
            ),
        ),
        migrations.CreateModel(
            name="Prospecto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "persona",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="prospecto",
                        to="accounts.persona",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Servicio",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre_servicio", models.CharField(max_length=100)),
                (
                    "precio_sugerido",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("descripcion", models.TextField()),
                (
                    "metodo",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="accounts.metodo",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="concepto",
            name="servicio",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="accounts.servicio"
            ),
        ),
    ]
