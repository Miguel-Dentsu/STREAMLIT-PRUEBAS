import streamlit as st
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Gráfico de Torta basado en Inputs")

# Espacios para escribir los inputs
input1 = st.text_input("Ingrese el primer valor:", "10")
input2 = st.text_input("Ingrese el segundo valor:", "20")

# Asumiendo que el input tiene valores numéricos
if input1 and input2:
    try:
        # Convertimos los inputs a float
        value1 = float(input1)
        value2 = float(input2)

        # Los datos para el gráfico de torta
        labels = ['Valor 1', 'Valor 2']
        sizes = [value1, value2]
        colors = ['#ff9999','#66b3ff']

        # Creación del gráfico de torta
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Hacer que el gráfico sea circular

        # Mostrar el gráfico en la aplicación de Streamlit
        st.pyplot(fig)

    except ValueError:
        st.error("Por favor, ingrese valores numéricos válidos.")

else:
    st.write("Ingrese valores en ambos campos de texto para ver el gráfico.")
