import streamlit as st

# Título y descripción del hotel
st.title("Hotel 'El Horizonte del Llano'")
st.write("""
Bienvenido al sistema de reservas del Hotel 'El Horizonte del Llano'. Nuestro hotel está ubicado en la zona rural del municipio de Acacías, Meta, Colombia. Ofrecemos un entorno único rodeado de paisajes impresionantes y una variedad de servicios para hacer de su estancia una experiencia inolvidable.

### Acacías, Meta, Colombia
Acacías es uno de los municipios más importantes del departamento del Meta, conocido por su biodiversidad, historia y actividades al aire libre. Se encuentra a solo 19 km de Villavicencio, la capital del Meta, y a 122,2 km de Bogotá, la capital de Colombia. Acacías es famoso por el Festival del Retorno, que atrae a turistas nacionales e internacionales cada año en octubre.

### Características del Hotel
- **Restaurante:** Nuestro restaurante tiene capacidad para 40 personas, ofreciendo una variedad de platos locales e internacionales.
- **Parqueadero:** Contamos con un parqueadero con capacidad para 25 vehículos.
- **Transporte:** Ofrecemos un servicio de transporte entre Acacías y el hotel en un microbús con capacidad para 20 personas. El viaje dura aproximadamente 90 minutos.

### Información de Check-in y Check-out
- **Check-in:** Desde las 3:00 pm
- **Check-out:** Antes de las 1:00 pm

### Servicios Adicionales
- **Reserva de parqueadero**
- **Transporte al pueblo**
- **Servicio de restaurante**
- **Servicio de lavandería**
- **Servicio de guía**
- **Huéspedes adicionales**

### Entorno Natural
Nuestros huéspedes destacan los paisajes que rodean el hotel, convirtiéndolo en un destino soñado para aquellos que buscan tranquilidad y conexión con la naturaleza.

### Seguridad
Tenga en cuenta que Acacías puede experimentar problemas de orden público debido a la presencia de grupos armados al margen de la ley. En ciertas épocas del año, se pueden realizar paros armados que afectan la entrada o salida del municipio y sus alrededores.

#### En esta plataforma, puede realizar reservas de habitaciones que tenemos disponibles actualmente. ¡Esperamos que disfrute su estadía con nosotros!
""")

# Mostrar imagen del hotel
st.image("assets/hotel.jpg", caption="Hotel El Horizonte del Llano", use_column_width=True)
