import streamlit as st
from datetime import datetime
from utils.db import init_db

# Inicializar la base de datos
init_db()

st.title("Buscar Habitación")

# Información sobre los tipos de habitaciones (detallada)
st.write("### Información sobre los tipos de habitaciones:")
st.write("""
**King:** Habitación con cama King, ideal para dos personas. Disfruta de una estancia cómoda y espaciosa. Las habitaciones King están diseñadas para ofrecer el máximo confort y lujo con servicios adicionales para una experiencia inolvidable.
""")
st.write("""
**Individual:** Habitación con cama individual, perfecta para una sola persona. Comodidad y privacidad garantizadas. Ideal para viajeros solitarios que buscan un espacio tranquilo y acogedor.
""")
st.write("""
**Compartida:** Habitación compartida con capacidad para cuatro personas. Conoce gente nueva y disfruta de una estancia económica. Perfecta para grupos de amigos o personas que viajan solas y desean socializar.
""")
st.write("### Búsqueda de Habitación")

st.write("##### Ingrese las fechas de su estadía y el tipo de habitación que desea reservar:")

# Validación de fechas
today = datetime.today().date()
check_in = st.date_input("Fecha de Check-in", min_value=today)
check_out = st.date_input("Fecha de Check-out", min_value=check_in)

# Descripciones sencillas para la selección de habitación
descriptions = {
    "King": "Habitación con cama King para dos personas.",
    "Individual": "Habitación con cama individual para una persona.",
    "Compartida": "Habitación compartida para hasta cuatro personas."
}

tipo_habitacion = st.selectbox("Tipo de Habitación", ["King", "Individual", "Compartida"])

# Mostrar descripción de la habitación seleccionada
st.write(f"**Descripción:** {descriptions[tipo_habitacion]}")

# Validaciones adicionales y mensajes de error
if st.button("Buscar"):
    st.session_state['check_in'] = check_in
    st.session_state['check_out'] = check_out
    st.session_state['tipo_habitacion'] = tipo_habitacion
    st.success("Búsqueda realizada con éxito. Verifique la disponibilidad.")
    st.experimental_set_query_params(pagina="disponibilidad")
    st.experimental_rerun()  # Redirigir a la página de disponibilidad
