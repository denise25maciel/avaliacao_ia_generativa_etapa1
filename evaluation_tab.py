import streamlit as st
import pandas as pd


def render_aba_avaliacoes():
    """Renderiza o conteúdo da aba 'Avaliações'. Usa e atualiza
    `st.session_state.avaliacoes_df`.
    """

    # garante que o DataFrame exista
    if "avaliacoes_df" not in st.session_state:
        st.session_state.avaliacoes_df = pd.DataFrame({
            "Título": [],
            "Data": [],
            "Disciplina": [],
            "ODS": [],
        })

    df = st.session_state.avaliacoes_df

    st.subheader("Lista de avaliações")

    if st.button("Adicionar nova avaliação"):
        novo = {
            "Título": "",
            "Data": pd.Timestamp.today().strftime("%Y-%m-%d"),
            "Disciplina": "",
            "ODS": "",
        }
        st.session_state.avaliacoes_df = pd.concat([df, pd.DataFrame([novo])], ignore_index=True)
        st.session_state.avaliacoes_editando_idx = len(st.session_state.avaliacoes_df) - 1
        st.session_state.modo_avaliacoes = "editar"
        # forçamos rerun para que a aba de edição seja exibida imediatamente
        st.rerun()

    st.divider()

    # Cabeçalho da tabela com ações extras (colunas estreitas)
    header = st.columns([3, 2, 2, 1, 0.4, 0.4, 0.4])
    header[0].write("Título")
    header[1].write("Data")
    header[2].write("Disciplina")
    header[3].write("ODS")
    header[4].write("Ver")
    header[5].write("Editar")
    header[6].write("Excluir")

    for idx, row in df.iterrows():
        linha = st.columns([3, 2, 2, 1, 0.4, 0.4, 0.4])
        linha[0].write(row["Título"])
        linha[1].write(row["Data"])
        linha[2].write(row["Disciplina"])
        linha[3].write(row["ODS"])

        # visualizar leva a edição em modo leitura
        if linha[4].button("👁️", key=f"ver_av_{idx}"):
            st.session_state.avaliacoes_editando_idx = idx
            st.session_state.modo_avaliacoes = "editar"
            st.session_state.view_only = True
            st.rerun()

        if linha[5].button("✏️", key=f"editar_av_{idx}"):
            st.session_state.avaliacoes_editando_idx = idx
            st.session_state.modo_avaliacoes = "editar"
            st.session_state.view_only = False
            st.rerun()

        if linha[6].button("🗑️", key=f"deletar_av_{idx}"):
            st.session_state.avaliacoes_df = df.drop(idx).reset_index(drop=True)
            st.rerun()

    # removida a seção de visualização isolada
