import streamlit as st
from mis_funciones import tasa, get_cuota, get_tabla

st.set_page_config("Ejemplo2_Streamlit",page_icon="🤖")
st.title("Tabla de amortizacion")

monto=st.number_input("Ingrese el monto solicitado",min_values=0)
plazo=st.number_input("Ingrese el numero de cuotas",min_values=0)




