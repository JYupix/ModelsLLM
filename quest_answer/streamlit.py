import streamlit as st

from main import get_answer

st.title("Sistema de Pregunta-Respuesta con Transformers")

question = st.text_input("Pregunta:", placeholder="Escribe tu pregunta aquí")
context = st.text_area("Contexto:", placeholder="Escribe o pega el contexto aquí")

if st.button("Obtener Respuesta"):
    if question and context:
        answer = get_answer(question, context)
        st.success(f"Respuesta: {answer}")
    else:
        st.warning("Por favor, ingresa tanto la pregunta como el contexto.")
