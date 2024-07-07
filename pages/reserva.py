import streamlit as st
from utils.db import init_db, make_reservation

# Inicializar la base de datos
init_db()

st.title("Reserva de Habitación")
id_habitacion = st.session_state.get('id_habitacion')
check_in = st.session_state.get('check_in')
check_out = st.session_state.get('check_out')

if not id_habitacion or not check_in or not check_out:
    st.error("Por favor seleccione una habitación primero.")
else:
    st.write(f"**Reservando Habitación Número:** {id_habitacion}")
    st.write(f"**Fecha de Check-in:** {check_in}")
    st.write(f"**Fecha de Check-out:** {check_out}")

    numero_identificacion = st.text_input("Número de Identificación")
    nombre = st.text_input("Nombre Completo")
    numero_contacto = st.text_input("Número de Contacto")
    email = st.text_input("Email")

    if st.button("Confirmar Reserva"):
        if not numero_identificacion or not nombre or not numero_contacto or not email:
            st.error("Por favor complete todos los campos para confirmar la reserva.")
        else:
            make_reservation(numero_identificacion, nombre, id_habitacion, check_in, check_out, numero_contacto, email)
            st.success("Reserva confirmada")