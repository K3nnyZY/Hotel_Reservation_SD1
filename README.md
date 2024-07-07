# Sistema de Reservas del Hotel "El Horizonte del Llano"

Bienvenido al sistema de reservas del Hotel "El Horizonte del Llano". Este proyecto proporciona una plataforma para que los usuarios puedan buscar, verificar la disponibilidad y reservar habitaciones en el hotel. El sistema está desarrollado utilizando Streamlit y SQLite para la gestión de datos.

![](/assets/show.png)

## Tabla de Contenidos

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Instalación](#instalación)
- [Uso](#uso)
- [Características](#características)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)

## Descripción del Proyecto

El Hotel "El Horizonte del Llano" está ubicado en la zona rural del municipio de Acacías, Meta, Colombia. Ofrecemos un entorno único rodeado de paisajes impresionantes y una variedad de servicios para hacer de su estancia una experiencia inolvidable. Este sistema permite a los usuarios realizar reservas de habitaciones de manera eficiente y cómoda.


## Instalación

Sigue estos pasos para configurar el proyecto en tu entorno local:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/hotel_reservations.git
   ```

2. Navega al directorio del proyecto:
   ```bash
   cd hotel_reservations
   ```

3. Crea un entorno virtual:
   ```bash
   python -m venv venv
   ```

4. Activa el entorno virtual:

   - En Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

Para ejecutar la aplicación, sigue estos pasos:

1. Asegúrate de que tu entorno virtual esté activado.
2. Ejecuta la aplicación Streamlit:
   ```bash
   streamlit run principal.py
   ```

3. Abre tu navegador y ve a `http://localhost:8501`.

## Características

- **Búsqueda de Habitaciones:** Los usuarios pueden buscar habitaciones disponibles ingresando las fechas de check-in y check-out, así como el tipo de habitación.
- **Verificación de Disponibilidad:** El sistema muestra la disponibilidad de habitaciones según los criterios de búsqueda.
- **Reserva de Habitaciones:** Los usuarios pueden realizar reservas proporcionando su información personal.
- **Descripciones Detalladas:** Información detallada sobre los tipos de habitaciones y servicios del hotel.

## Tecnologías Utilizadas

- **Frontend:** [Streamlit](https://streamlit.io/)
- **Backend:** [SQLite](https://www.sqlite.org/)
- **Lenguaje de Programación:** Python