import streamlit as st
import matplotlib.pyplot as plt
from io import BytesIO

# Título de la aplicación
st.title("Mix de Inversión")

# Inicializar listas para almacenar categorías y presupuestos
if 'categorias' not in st.session_state:
    st.session_state.categorias = []
if 'presupuestos' not in st.session_state:
    st.session_state.presupuestos = []

# Entrada de datos
categoria = st.text_input("Ingrese la categoría:")
presupuesto = st.number_input("Ingrese el presupuesto en euros:", min_value=0.0, step=1.0)

# Botón para añadir la categoría y el presupuesto
if st.button("Añadir Categoría"):
    if categoria and presupuesto > 0:
        st.session_state.categorias.append(categoria)
        st.session_state.presupuestos.append(presupuesto)
        st.success(f"Categoría '{categoria}' con un presupuesto de {presupuesto}€ añadida.")
    else:
        st.error("Por favor, ingrese una categoría y un presupuesto válido.")

# Botón para generar el gráfico
if st.button("Listo"):
    if st.session_state.categorias and st.session_state.presupuestos:
        fig, ax = plt.subplots()
        ax.pie(st.session_state.presupuestos, labels=st.session_state.categorias, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Hacer que el gráfico sea circular
        st.pyplot(fig)

        # Crear un buffer para la descarga
        buffer = BytesIO()
        fig.savefig(buffer, format="png")
        buffer.seek(0)

        st.download_button(
            label="Descargar gráfico",
            data=buffer,
            file_name="mix_de_inversion.png",
            mime="image/png"
        )
    else:
        st.error("Por favor, añada al menos una categoría y un presupuesto antes de generar el gráfico.")
