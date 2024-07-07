import streamlit as st
from utils.db import init_db, get_available_rooms

# Inicializar la base de datos
init_db()

st.title("Disponibilidad de Habitaciones")
check_in = st.session_state.get('check_in')
check_out = st.session_state.get('check_out')
tipo_habitacion = st.session_state.get('tipo_habitacion')

if not check_in or not check_out or not tipo_habitacion:
    st.error("Por favor complete la búsqueda primero.")
else:
    habitaciones = get_available_rooms(check_in, check_out, tipo_habitacion)
    if habitaciones:
        st.write("### Habitaciones disponibles:")
        
        # Ordenar habitaciones por número de habitación en orden ascendente
        habitaciones.sort(key=lambda x: x[0])
        
        for habitacion in habitaciones:
            camas_disponibles = habitacion[3] - habitacion[4]
            st.markdown(f"""
            **Número de Habitación:** {habitacion[0]}  
            **Tipo:** {habitacion[1]}  
            **Camas Disponibles:** {camas_disponibles}  
            """)
            if st.button("Reservar", key=f"reservar_{habitacion[0]}"):
                st.session_state['id_habitacion'] = habitacion[0]
                st.experimental_rerun()  # Redirigir a la página de reserva
    else:
        st.write("No hay habitaciones disponibles para las fechas seleccionadas.")