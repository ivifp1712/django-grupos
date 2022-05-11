PASOS A SEGUIR

1. Sino tienes instalado esto, instalalo a continuacion

pip install django
pip install psycopg2

2. Conexion con base de datos en carpeta Prueba1/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django1',
        'USER': 'postgres',
        'PASSWORD': 'curso',
        'HOST': 'localhost',
        'DATABASE_PORT': '5432',
    }
}

3. Ejecutar los siguientes comandos para crear el modelo de base de datos

python manage.py makemigrations
python manage.py migrate

// Se inicia en el puero 8000 por defecto
python manage.py runserver 
