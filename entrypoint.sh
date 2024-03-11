#!/bin/sh
# Esperar hasta que ambas bases de datos estén disponibles
while ! nc -z db 5432 ; do
  echo "Esperando a que las bases de datos estén disponibles..."
  sleep 3
done

# Aplicar las migraciones de Django
python manage.py makemigrations
python manage.py migrate 

# Iniciar la aplicación Django
exec "$@"