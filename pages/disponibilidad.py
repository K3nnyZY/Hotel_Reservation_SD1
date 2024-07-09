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
    habitaciones_disponibles = get_available_rooms(check_in, check_out, tipo_habitacion)
    
    if habitaciones_disponibles:
        st.write("### Habitaciones disponibles para las fechas seleccionadas:")
        
        # Ordenar habitaciones por número de habitación en orden ascendente
        habitaciones_disponibles.sort(key=lambda x: x[0])
        
        for habitacion in habitaciones_disponibles:
            camas_ocupadas_periodo = habitacion[4]
            camas_disponibles = habitacion[2] - camas_ocupadas_periodo
            st.markdown(f"""
            **Número de Habitación:** {habitacion[0]}  
            **Tipo:** {habitacion[1]}  
            **Camas Disponibles:** {camas_disponibles}  
            """)
            if st.button(f"Reservar Habitación {habitacion[0]}", key=f"reservar_{habitacion[0]}"):
                st.session_state['id_habitacion'] = habitacion[0]
                st.session_state['reserva_mensaje'] = "Habitación seleccionada. Complete el formulario de reserva."
                st.experimental_rerun()  # Redirigir a la misma página para mostrar el mensaje

if 'reserva_mensaje' in st.session_state:
    st.success(st.session_state['reserva_mensaje'])
    del st.session_state['reserva_mensaje']
    st.query_params = {"pagina": "reserva"}