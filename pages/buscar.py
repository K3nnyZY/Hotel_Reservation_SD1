import streamlit as st
from utils.db import init_db

# Inicializar la base de datos
init_db()

st.title("Buscar Habitación")
st.write("Ingrese las fechas de su estadía y el tipo de habitación que desea reservar.")
check_in = st.date_input("Fecha de Check-in")
check_out = st.date_input("Fecha de Check-out")
tipo_habitacion = st.selectbox("Tipo de Habitación", ["King", "Individual", "Compartida"])

if st.button("Buscar"):
    st.session_state['check_in'] = check_in
    st.session_state['check_out'] = check_out
    st.session_state['tipo_habitacion'] = tipo_habitacion
    st.success("Búsqueda realizada con éxito. Verifique la disponibilidad.")
    st.experimental_rerun()  # Redirigir a la página de disponibilidad
