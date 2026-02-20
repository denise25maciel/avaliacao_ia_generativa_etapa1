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
        # precisamos recriar a interface imediatamente após a alteração do estado
        # `st.rerun()` (ou `st.experimental_rerun()`) força o Streamlit a reexecutar o
        # script desde o topo. Sem ela a atualização só aparece num clique seguinte
        # ou outra interação. Comentá‑la não causa erro, mas faz com que a página
        # pareça não carregar/atualizar até o usuário fazer algo.
        st.rerun()

    st.divider()

    # Cabeçalho com colunas extras para visualizar/editar/deletar
    # pesos menores nas ações para maximizar espaço dos dados
    header = st.columns([1, 4, 3, 1, 1, 0.4, 0.4, 0.4])
    header[0].write("Código")
    header[1].write("Descrição")
    header[2].write("Fonte")
    header[3].write("Ano")
    header[4].write("Dificuldade")
    header[5].write("Ver")
    header[6].write("Editar")
    header[7].write("Excluir")

    for idx, row in df.iterrows():
        linha = st.columns([1, 4, 3, 1, 1, 0.4, 0.4, 0.4])
        linha[0].write(row["Código"])
        linha[1].write(row["Descrição"])
        linha[2].write(row["Fonte"])
        linha[3].write(row["Ano"])
        linha[4].write(row["Dificuldade"])

        # visualizar redireciona para edição em modo somente leitura
        if linha[5].button("👁️", key=f"ver_{idx}"):
            st.session_state.editando_idx = idx
            st.session_state.modo = "editar"
            st.session_state.view_only = True
            st.rerun()

        if linha[6].button("✏️", key=f"editar_{idx}"):
            st.session_state.editando_idx = idx
            st.session_state.modo = "editar"
            st.session_state.view_only = False
            # atualização do estado e rerun para mudar a tela
            st.rerun()

        if linha[7].button("🗑️", key=f"deletar_{idx}"):
            st.session_state.exercicios_df = df.drop(idx).reset_index(drop=True)
            st.rerun()


