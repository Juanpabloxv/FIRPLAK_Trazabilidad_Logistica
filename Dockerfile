# Imagen base de Python 3.9
FROM python:3.12.2

# Establece la variable de entorno PYTHONUNBUFFERED
ENV PYTHONUNBUFFERED=1

# Actualiza pip
RUN pip install --upgrade pip

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

RUN apt-get update && apt-get install -y netcat-openbsd

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Copia el resto de los archivos del proyecto al contenedor
COPY . .

# Exponemos el puerto 8000
EXPOSE 8000

# Comando para ejecutar el servidor de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
