import streamlit as st
import pandas as pd

# ---------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# ---------------------------------------------------

st.set_page_config(
    page_title="Plataforma de Gestão de Exercícios",
    layout="wide"
)

st.title("Plataforma de Gestão de Exercícios")


# ---------------------------------------------------
# INICIALIZAÇÃO DO ESTADO
# ---------------------------------------------------

def inicializar_dados():
    codigos = [f"EX{i:03d}" for i in range(1, 31)]
    descricoes = [f"Exercício número {i}" for i in range(1, 31)]
    fontes = ["ENADE" if i % 2 == 1 else "CONCURSO" for i in range(1, 31)]
    anos = [2020 + (i % 6) for i in range(1, 31)]
    dificuldades = [
        "Fácil" if i % 3 == 0 else ("Médio" if i % 3 == 1 else "Difícil")
        for i in range(1, 31)
    ]

    return pd.DataFrame({
        "Código": codigos,
        "Descrição": descricoes,
        "Fonte": fontes,
        "Ano": anos,
        "Dificuldade": dificuldades,
    })


if "exercicios_df" not in st.session_state:
    st.session_state.exercicios_df = inicializar_dados()

if "modo" not in st.session_state:
    st.session_state.modo = "lista"   # lista | editar

if "editando_idx" not in st.session_state:
    st.session_state.editando_idx = None


df = st.session_state.exercicios_df


# ===================================================
# MODO EDIÇÃO FULLSCREEN
# ===================================================

if st.session_state.modo == "editar":

    idx = st.session_state.editando_idx

    st.header("Editar exercício")
    st.divider()

    col_esquerda, col_direita = st.columns([2, 1])

    # -------------------------
    # COLUNA PRINCIPAL (FORM)
    # -------------------------

    with col_esquerda:

        codigo = st.text_input(
            "Código",
            value=df.at[idx, "Código"]
        )

        descricao = st.text_area(
            "Descrição",
            value=df.at[idx, "Descrição"],
            height=150
        )

        fonte = st.selectbox(
            "Fonte",
            options=["ENADE", "CONCURSO"],
            index=["ENADE", "CONCURSO"].index(df.at[idx, "Fonte"])
        )

        ano = st.number_input(
            "Ano",
            value=int(df.at[idx, "Ano"]),
            step=1
        )

        dificuldade = st.selectbox(
            "Dificuldade",
            options=["Fácil", "Médio", "Difícil"],
            index=["Fácil", "Médio", "Difícil"].index(df.at[idx, "Dificuldade"])
        )

        st.divider()

        b1, b2 = st.columns(2)

        if b1.button("Salvar", key="salvar_exercicio", use_container_width=True):
            st.session_state.exercicios_df.at[idx, "Código"] = codigo
            st.session_state.exercicios_df.at[idx, "Descrição"] = descricao
            st.session_state.exercicios_df.at[idx, "Fonte"] = fonte
            st.session_state.exercicios_df.at[idx, "Ano"] = ano
            st.session_state.exercicios_df.at[idx, "Dificuldade"] = dificuldade

            st.session_state.modo = "lista"
            st.session_state.editando_idx = None
            st.rerun()

        if b2.button("Cancelar", key="cancelar_edicao", use_container_width=True):
            st.session_state.modo = "lista"
            st.session_state.editando_idx = None
            st.rerun()

    # -------------------------
    # COLUNA LATERAL (PREVIEW)
    # -------------------------

    with col_direita:
        
        st.subheader("Comandos para a IA")
        comandos_ia = st.text_area(
            "Insira os comandos para a IA",
            value="",
            height=150,
            label_visibility="collapsed"
        )

        if st.button("Processar", key="processar_ia", use_container_width=True):
            # Aqui você pode adicionar a lógica para processar os comandos
            st.info(f"Comandos recebidos: {comandos_ia}")

        st.subheader("Resultado da Adaptação")
        comandos_ia = st.text_area(
            "IExercício adaptado para o ENEM",
            value="",
            height=150,
            label_visibility="collapsed"
        )

        if st.button("Salvar", use_container_width=True):
            # Aqui você pode adicionar a lógica para processar os comandos
            st.info(f"Comando salvo: {comandos_ia}")
        
        
    # Impede renderização do restante da página
    st.stop()


# ===================================================
# MODO LISTAGEM PRINCIPAL
# ===================================================

aba_exercicios, aba_avaliacoes, aba_bases = st.tabs(
    ["Exercícios", "Avaliações", "Bases de Dados"]
)

with aba_exercicios:

    st.subheader("Lista de exercícios")

    if st.button("Adicionar novo exercício"):
        novo = {
            "Código": "",
            "Descrição": "",
            "Fonte": "ENADE",
            "Ano": 2024,
            "Dificuldade": "Fácil"
        }

        st.session_state.exercicios_df = pd.concat(
            [df, pd.DataFrame([novo])],
            ignore_index=True
        )

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


with aba_avaliacoes:
    st.header("Avaliações")
    st.write("Área para montagem e visualização de avaliações.")


with aba_bases:
    st.header("Bases de Dados")
    st.write("Upload e gerenciamento de bases de exercícios.")