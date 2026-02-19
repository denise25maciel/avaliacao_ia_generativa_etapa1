import streamlit as st

st.title("Plataforma de Gestão de Exercícios")
import pandas as pd
# cria abas principais
aba_exercicios, aba_avaliacoes, aba_bases = st.tabs(["Exercícios", "Avaliações", "Bases de Dados"])
# função de diálogo decorada
@st.dialog("Editar exercício")
def edit_dialog(idx):
    df = st.session_state.exercicios_df
    edited = {}
    for col in df.columns:
        edited[col] = st.text_input(col, value=str(df.at[idx, col]))
    col1, col2 = st.columns(2)
    if col1.button("Salvar"):
        for col, val in edited.items():
            st.session_state.exercicios_df.at[idx, col] = val
        st.rerun()
    if col2.button("Cancelar"):
        st.rerun()

    st.write("Dados atuais:")
    st.dataframe(st.session_state.exercicios_df)

with aba_exercicios:
    st.header("Exercícios")
    # tabela de exercícios persistente em sessão
    



    if "exercicios_df" not in st.session_state:
        # cria 30 exercícios de exemplo automaticamente
        codigos = [f"EX{i:03d}" for i in range(1, 31)]
        descricoes = [f"Exercício número {i}" for i in range(1, 31)]
        fontes = ["ENADE" if i % 2 == 1 else "CONCURSO" for i in range(1, 31)]
        anos = [2020 + (i % 6) for i in range(1, 31)]
        dificuldades = ["Fácil" if i % 3 == 0 else ("Médio" if i % 3 == 1 else "Difícil") for i in range(1, 31)]
        data = {
            "Código": codigos,
            "Descrição": descricoes,
            "Fonte": fontes,
            "Ano": anos,
            "Dificuldade": dificuldades,
        }
        st.session_state.exercicios_df = pd.DataFrame(data)

    df = st.session_state.exercicios_df

    if st.button("Adicionar novo exercício"):
        new = {k: "" for k in df.columns}
        st.session_state.exercicios_df = pd.concat([df, pd.DataFrame([new])], ignore_index=True)
        edit_dialog(len(st.session_state.exercicios_df) - 1)

    st.subheader("Lista de exercícios")
    # cabeçalho customizado
    header_cols = st.columns([1,3,2,1,1,1])
    header_cols[0].write("Código")
    header_cols[1].write("Descrição")
    header_cols[2].write("Fonte")
    header_cols[3].write("Ano")
    header_cols[4].write("Dificuldade")
    header_cols[5].write("")

    # exibe cada linha com botão de edição ao lado
    for idx, row in df.iterrows():
        row_cols = st.columns([1,3,2,1,1,1])
        row_cols[0].write(row["Código"])
        row_cols[1].write(row["Descrição"])
        row_cols[2].write(row["Fonte"])
        row_cols[3].write(row["Ano"])
        row_cols[4].write(row["Dificuldade"])
        if row_cols[5].button("✏️", key=f"edit_{idx}"):
            edit_dialog(idx)




with aba_avaliacoes:
    st.header("Avaliações")
    st.write("Área para montagem e visualização de avaliações/provas.")

with aba_bases:
    st.header("Bases de Dados")
    st.write("Upload e gerenciamento de bases de exercícios.")
