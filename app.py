import streamlit as st

st.title("Plataforma de Gestão de Exercícios")

# cria abas principais
aba_exercicios, aba_avaliacoes, aba_bases = st.tabs(["Exercícios", "Avaliações", "Bases de Dados"])

with aba_exercicios:
    st.header("Exercícios")
    st.write("Aqui serão exibidos os exercícios cadastrados.")
    # tabela de exercícios persistente em sessão
    import pandas as pd

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

    st.subheader("Lista de exercícios")
    # escolha de um exercício
    options = [f"{i} - {row['Código']}" for i, row in df.iterrows()]
    selected = None
    if options:
        choice = st.selectbox("Selecione um exercício", options, key="sel_ex")
        selected = int(choice.split(" - ")[0])
        if st.button("Editar este exercício"):
            st.session_state.edit_index = selected
            st.session_state.show_modal = True

    if st.button("Adicionar novo exercício"):
        new = {k: "" for k in df.columns}
        st.session_state.exercicios_df = pd.concat([df, pd.DataFrame([new])], ignore_index=True)
        st.session_state.edit_index = len(st.session_state.exercicios_df) - 1
        st.session_state.show_modal = True

    # modal para edição
    if st.session_state.get("show_modal"):
        idx = st.session_state.get("edit_index")
        with st.modal("Editar exercício", key="modal"):
            edited = {}
            for col in df.columns:
                edited[col] = st.text_input(col, value=str(df.at[idx, col]))
            if st.button("Salvar"):
                for col, val in edited.items():
                    st.session_state.exercicios_df.at[idx, col] = val
                st.session_state.show_modal = False
            if st.button("Cancelar"):
                st.session_state.show_modal = False

    st.write("Dados atuais:")
    st.dataframe(st.session_state.exercicios_df)

with aba_avaliacoes:
    st.header("Avaliações")
    st.write("Área para montagem e visualização de avaliações/provas.")

with aba_bases:
    st.header("Bases de Dados")
    st.write("Upload e gerenciamento de bases de exercícios.")
