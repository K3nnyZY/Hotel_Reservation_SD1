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
    id_usuario = st.text_input("ID de Usuario")
    info_pago = st.text_input("Información de Pago")

    if st.button("Confirmar Reserva"):
        make_reservation(id_usuario, id_habitacion, check_in, check_out, info_pago)
        st.success("Reserva confirmada")
