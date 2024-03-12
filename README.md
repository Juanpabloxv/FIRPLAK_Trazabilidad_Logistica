# FIRPLAK_Trazabilidad_Logistica
Aploicacion FIRPLAK Trazabilidad Logistica desarrollado del backend

## Descripción

La aplicación desarrollada en Django Rest Framework busca optimizar el flujo logístico de FIRPLAK S.A al proporcionar una solución integral de trazabilidad en tiempo real para sus entregas nacionales. A través de la automatización de procesos, la aplicación gestiona pedidos, asigna mercancías, registra entregas y facilita la obtención de Pruebas de Entrega (POD) de manera eficiente. Utilizando contenedores Docker, la aplicación se presenta como una solución fácilmente desplegable, permitiendo a los usuarios clonar el repositorio, levantar la aplicación con un simple comando, y explorar y probar los endpoints a través de la documentación Swagger. La implementación efectiva de esta solución busca reducir los tiempos de facturación, mejorar la trazabilidad de las entregas y, en última instancia, optimizar el flujo de caja de FIRPLAK S.A.

## Requisitos
- Docker y Docker-compose instalado (Docker desktop tambien funciona)
- Git instalado

## Instalación y Uso

1. **Clonar el Repositorio:**
    ```bash
    git clone https://github.com/Juanpabloxv/FIRPLAK_Trazabilidad_Logistica.git

    luego de tener clonado el repositorio ingresar a la ruta donde se clono 
    cd ./FIRPLAK_Trazabilidad_Logistica
    ```
2. **Levantar la Aplicación con Docker:**
    Para esto primero es importante tener docker instalado y corriendo,
    luego:
    ```bash
    docker-compose up -d
    ```
    Importante: correr este comando donde se encuentra la carpeta "docker-compose.yml"

3.  **Acceder a la Aplicación:**
    - Abre tu navegador web y visita [http://localhost:8000](http://localhost:8000)

    Luego podras acceder a 2 diferentes endpoints los cuales son:
    - [http://localhost:8000/api/](http://localhost:8000/api/) esta url es para ver todas las posibles rutas y acceder a crear instancias en el modelo para poder hacer la trazabilidad

    Recomendada: En esta podras ver todos los endpoints creados para poder hacer las peticiones http en las cuales veras como listar, crear, eliminar y editar cada uno de las tablas de la base de datos, tambien podras ver los modelos creados.
    - [http://localhost:8000/swagger/](http://localhost:8000/swagger/)

4. **Detener la Aplicación:**
    ```bash
    docker-compose down
    ```
    Importante: correr este comando donde se encuentra la carpeta "docker-compose.yml"

## Contribuciones
- Siéntete libre de contribuir o informar problemas (issues) en el [repositorio de GitHub](https://github.com/Juanpabloxv/FIRPLAK_Trazabilidad_Logistica).

## Licencia
Creado por: Juan Pablo Herrera Herrera