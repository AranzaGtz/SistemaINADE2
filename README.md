# SistemaINADE2

Este es un proyecto de Django llamado SistemaINADE2. 

## Requisitos

Asegúrate de tener los siguientes requisitos antes de empezar:

- Python 3.x
- Pip
- Virtualenv
- Django 

## Instalación

Sigue estos pasos para clonar el repositorio y configurar el proyecto en tu máquina local.

### 1. Clonar el repositorio

Abre una terminal y ejecuta el siguiente comando para clonar el repositorio:

bash
git clone https://github.com/AranzaGtz/SistemaINADE2.git

## 2. Navegar al directorio del proyecto

bash
 cd SistemaINADE2

## 3. Crear un entorno virtual
Crea un entorno virtual para el proyecto:

bash
Copiar código
python3 -m venv env

## 4. Activar el entorno virtual
En macOS y Linux, usa:

bash
Copiar código
source env/bin/activate

En Windows, usa:

bash
Copiar código
.\env\Scripts\activate

## 5. Instalar las dependencias
Instala las dependencias necesarias usando el archivo requirements.txt:

bash
Copiar código
pip install -r requirements.txt


## 6. Configurar las variables de entorno
Crea un archivo .env en el directorio raíz del proyecto y añade tus variables de entorno necesarias, como la configuración de la base de datos. 
Un ejemplo de archivo .env puede verse así:

plaintext
Copiar código
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_database_url

## 7. Migrar la base de datos
Ejecuta las migraciones de la base de datos:

bash
Copiar código
python manage.py migrate

## 8. Crear un superusuario
Crea un superusuario para acceder al administrador de Django:

bash
Copiar código
python manage.py createsuperuser

## 9. Ejecutar el servidor de desarrollo
Ejecuta el servidor de desarrollo de Django:

bash
Copiar código
python manage.py runserver
Ahora, puedes acceder al proyecto en http://127.0.0.1:8000/.
