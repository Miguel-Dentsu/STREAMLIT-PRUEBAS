import streamlit as st
import matplotlib.pyplot as plt
from io import BytesIO

# Título de la aplicación
st.title("Mix de Inversión")

# Inicializar listas para las categorías y presupuestos
categorias = []
presupuestos = []

# Entrada de datos
categoria = st.text_input("Ingrese la categoría:")
presupuesto = st.number_input("Ingrese el presupuesto en euros:", min_value=0.0, step=1.0)

# Botón para añadir la categoría y el presupuesto
if st.button("Añadir categoría"):
    if categoria and presupuesto > 0:
        categorias.append(categoria)
        presupuestos.append(presupuesto)
        st.success(f"Categoría '{categoria}' con un presupuesto de {presupuesto}€ añadida.")
    else:
        st.error("Por favor, ingrese una categoría y un presupuesto válido.")

# Mostrar el gráfico de torta si hay datos
if categorias and presupuestos:
    fig, ax = plt.subplots()
    ax.pie(presupuestos, labels=categorias, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Hacer que el gráfico sea circular
    st.pyplot(fig)

    # Crear un botón de descarga
    buffer = BytesIO()
    fig.savefig(buffer, format="png")
    buffer.seek(0)
    
    st.download_button(
        label="Descargar gráfico",
        data=buffer,
        file_name="mix_de_inversion.png",
        mime="image/png"
    )

