import streamlit as st

st.title("Plataforma de Gestão de Exercícios")

# cria abas principais
aba_exercicios, aba_avaliacoes, aba_bases = st.tabs(["Exercícios", "Avaliações", "Bases de Dados"])

with aba_exercicios:
    st.header("Exercícios")
    st.write("Aqui serão exibidos os exercícios cadastrados.")

with aba_avaliacoes:
    st.header("Avaliações")
    st.write("Área para montagem e visualização de avaliações/provas.")

with aba_bases:
    st.header("Bases de Dados")
    st.write("Upload e gerenciamento de bases de exercícios.")
