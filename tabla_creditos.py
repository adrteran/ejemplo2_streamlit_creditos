import streamlit as st
from funciones import tasa, get_cuota, get_tabla

st.set_page_config("Ejemplo2_Streamlit",page_icon="🤖")
st.title("Tabla de amortizacion")

monto = st.number_input("Ingrese el monto solicitado",min_value=0)
plazo = st.number_input("Ingrese el numero de cuotas",min_value=0,step=3)

if st.button("Procesar"):
    if monto > 0 and plazo > 0:
        tabla = get_tabla(monto,plazo,tasa)
        st.dataframe(tabla)
    else:
        st.write("Por favor ingresa valores positivos!")




