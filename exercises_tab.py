import streamlit as st
import pandas as pd


def render_aba_exercicios():
    """Renderiza o conteúdo da aba 'Exercícios'. Usa e atualiza `st.session_state.exercicios_df`.
    """
    # garante que o DataFrame exista
    if "exercicios_df" not in st.session_state:
        st.session_state.exercicios_df = pd.DataFrame({
            "Código": [],
            "Descrição": [],
            "Fonte": [],
            "Ano": [],
            "Dificuldade": [],
        })

    df = st.session_state.exercicios_df

    st.subheader("Lista de exercícios")

    if st.button("Adicionar novo exercício"):
        novo = {
            "Código": "",
            "Descrição": "",
            "Fonte": "ENADE",
            "Ano": 2024,
            "Dificuldade": "Fácil",
        }
        st.session_state.exercicios_df = pd.concat([df, pd.DataFrame([novo])], ignore_index=True)
        st.session_state.editando_idx = len(st.session_state.exercicios_df) - 1
        st.session_state.modo = "editar"
        st.rerun()

    st.divider()

    # Cabeçalho
    header = st.columns([1, 3, 2, 1, 1, 1])
    header[0].write("Código")
    header[1].write("Descrição")
    header[2].write("Fonte")
    header[3].write("Ano")
    header[4].write("Dificuldade")
    header[5].write("")

    for idx, row in df.iterrows():
        linha = st.columns([1, 3, 2, 1, 1, 1])
        linha[0].write(row["Código"])
        linha[1].write(row["Descrição"])
        linha[2].write(row["Fonte"])
        linha[3].write(row["Ano"])
        linha[4].write(row["Dificuldade"])

        if linha[5].button("✏️", key=f"editar_{idx}"):
            st.session_state.editando_idx = idx
            st.session_state.modo = "editar"
            st.rerun()

    # tabela tradicional abaixo para visualização completa
    st.write("Dados atuais:")
    st.dataframe(st.session_state.exercicios_df)
