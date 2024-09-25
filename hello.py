import streamlit as st

st.write("CD/TEC")
st.write("Hello world")

generos_musicais = ["Sertanejo", "Rock", "Eletronica"]

genero_musical = st.selectbox("Genero musical", generos_musicais)

bandas = {
    "Sertanejo": ["Gusttavo Lima", "Marilia Mendonça", "Zé Neto e Cristiano"],
    "Rock": ["Linkin Park", "Evanescence", "Green Day", "Alok", "Tiesto", "Zeeba"],
    "Eletronica": ["Alok", "Tiesto", "Alan Walker"]}

bandas_prediletas = st.selectbox("Escolha sua banda predileta: ", bandas[genero_musical])

st.write(f"A melhor banda de {genero_musical} é {bandas_prediletas}")