import streamlit as st
import pandas as pd
from exercises_tab import render_aba_exercicios
from evaluation_tab import render_aba_avaliacoes
from database_tab import render_aba_bases_dados

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
    dados = {
        "Código": [f"EX{i:03d}" for i in range(1, 31)],
        "Descrição": [
            "Sobre estruturas de dados lineares, qual estrutura segue o princípio FILO?",
            "Qual é a complexidade de tempo do algoritmo Quick Sort no melhor caso?",
            "Qual protocolo da camada de transporte garante entrega confiável?",
            "Em POO, qual princípio garante que detalhes internos sejam ocultados?",
            "Qual é a diferença entre compilador e interpretador?",
            "Explique o conceito de normalização em bancos de dados",
            "O que é injeção de dependência em programação?",
            "Qual técnica criptográfica utiliza duas chaves diferentes?",
            "Em SQL, qual comando recupera dados de tabelas?",
            "Qual é a complexidade de espaço do algoritmo Merge Sort?",
            "Descreva o padrão de projeto Singleton",
            "Qual é a diferença entre REST e SOAP?",
            "Explique o conceito de eventual consistency",
            "O que é Docker e sua principal vantagem?",
            "Qual modelo de processo tem iterações curtas?",
            "Qual camada do OSI é responsável por roteamento?",
            "O que é uma função hash criptográfica?",
            "Descreva o padrão MVC na arquitetura de software",
            "Qual é o teorema CAP em sistemas distribuídos?",
            "O que é uma chave estrangeira em bancos de dados?",
            "Explique o conceito de deadlock em SO",
            "Qual é a diferença entre TCP e UDP?",
            "O que é o padrão Observer em design patterns?",
            "Descreva o pipeline de um processador",
            "Qual é a função da Unidade Lógica e Aritmética?",
            "O que é cache em sistemas computacionais?",
            "Explique o conceito de multithreading",
            "Qual é a diferença entre busca DFS e BFS?",
            "O que é normalização de dados?",
            "Descreva o ciclo de vida do software"
        ],
        "Fonte": ["ENADE" if i % 2 == 1 else "Concurso" for i in range(1, 31)],
        "Ano": [2020 + (i % 6) for i in range(1, 31)],
        "Dificuldade": [
            "Fácil" if i % 3 == 0 else ("Médio" if i % 3 == 1 else "Difícil")
            for i in range(1, 31)
        ],
    }
    
    return pd.DataFrame(dados)


if "exercicios_df" not in st.session_state:
    st.session_state.exercicios_df = inicializar_dados()

if "modo" not in st.session_state:
    st.session_state.modo = "lista"   # lista | editar

if "editando_idx" not in st.session_state:
    st.session_state.editando_idx = None

# ---------------------------------------------------
# estado para a aba "Avaliações"
# ---------------------------------------------------
if "avaliacoes_df" not in st.session_state:
    st.session_state.avaliacoes_df = pd.DataFrame({
        "Título": [],
        "Data": [],
        "Disciplina": [],
        "ODS": [],
    })

if "modo_avaliacoes" not in st.session_state:
    st.session_state.modo_avaliacoes = "lista"  # lista | editar

if "avaliacoes_editando_idx" not in st.session_state:
    st.session_state.avaliacoes_editando_idx = None


df = st.session_state.exercicios_df


# ===================================================
# MODO EDIÇÃO FULLSCREEN
# ===================================================

if st.session_state.modo == "editar":

    idx = st.session_state.editando_idx
    view_only = st.session_state.get("view_only", False)

    st.header("Editar exercício")
    st.divider()

    col_esquerda, col_direita = st.columns([2, 1])

    # -------------------------
    # COLUNA PRINCIPAL (FORM)
    # -------------------------

    with col_esquerda:

        codigo = st.text_input(
            "Código",
            value=df.at[idx, "Código"],
            disabled=view_only,
        )

        descricao = st.text_area(
            "Descrição",
            value=df.at[idx, "Descrição"],
            height=150,
            disabled=view_only,
        )

        fonte = st.selectbox(
            "Fonte",
            options=["ENADE", "CONCURSO"],
            index=["ENADE", "CONCURSO"].index(df.at[idx, "Fonte"]),
            disabled=view_only,
        )

        ano = st.number_input(
            "Ano",
            value=int(df.at[idx, "Ano"]),
            step=1,
            disabled=view_only,
        )

        dificuldade = st.selectbox(
            "Dificuldade",
            options=["Fácil", "Médio", "Difícil"],
            index=["Fácil", "Médio", "Difícil"].index(df.at[idx, "Dificuldade"]),
            disabled=view_only,
        )

        st.divider()

        b1, b2 = st.columns(2)

        if not view_only and b1.button("Salvar", key="salvar_exercicio", use_container_width=True):
            st.session_state.exercicios_df.at[idx, "Código"] = codigo
            st.session_state.exercicios_df.at[idx, "Descrição"] = descricao
            st.session_state.exercicios_df.at[idx, "Fonte"] = fonte
            st.session_state.exercicios_df.at[idx, "Ano"] = ano
            st.session_state.exercicios_df.at[idx, "Dificuldade"] = dificuldade

            st.session_state.modo = "lista"
            st.session_state.editando_idx = None
            st.session_state.view_only = False
            st.rerun()

        if b2.button("Cancelar", key="cancelar_edicao", use_container_width=True):
            st.session_state.modo = "lista"
            st.session_state.editando_idx = None
            st.session_state.view_only = False
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
# MODO EDIÇÃO AVALIAÇÕES FULLSCREEN
# ===================================================
if st.session_state.modo_avaliacoes == "editar":

    idx = st.session_state.avaliacoes_editando_idx
    df2 = st.session_state.avaliacoes_df
    view_only = st.session_state.get("view_only", False)

    st.header("Editar avaliação")
    st.divider()

    col_esquerda, col_direita = st.columns([2, 1])

    with col_esquerda:

        titulo = st.text_input(
            "Título",
            value=df2.at[idx, "Título"],
            disabled=view_only,
        )

        data = st.date_input(
            "Data",
            value=pd.to_datetime(df2.at[idx, "Data"]) if df2.at[idx, "Data"] != "" else pd.to_datetime("today"),
            disabled=view_only,
        )

        disciplina = st.text_input(
            "Disciplina",
            value=df2.at[idx, "Disciplina"],
            disabled=view_only,
        )

        ods = st.text_input(
            "ODS",
            value=df2.at[idx, "ODS"],
            disabled=view_only,
        )

        st.divider()

        b1, b2 = st.columns(2)

        if not view_only and b1.button("Salvar", key="salvar_avaliacao", use_container_width=True):
            st.session_state.avaliacoes_df.at[idx, "Título"] = titulo
            st.session_state.avaliacoes_df.at[idx, "Data"] = str(data)
            st.session_state.avaliacoes_df.at[idx, "Disciplina"] = disciplina
            st.session_state.avaliacoes_df.at[idx, "ODS"] = ods

            st.session_state.modo_avaliacoes = "lista"
            st.session_state.avaliacoes_editando_idx = None
            st.session_state.view_only = False
            st.rerun()

        if b2.button("Cancelar", key="cancelar_edicao_avaliacao", use_container_width=True):
            st.session_state.modo_avaliacoes = "lista"
            st.session_state.avaliacoes_editando_idx = None
            st.session_state.view_only = False
            st.rerun()

    with col_direita:
        st.subheader("Questões")
        questoes = []
        if "Questoes" in df2.columns and idx is not None:
            questoes = df2.at[idx, "Questoes"]
        if not isinstance(questoes, list):
            questoes = []

        exercises = st.session_state.get("exercicios_df", pd.DataFrame())
        descricao_por_codigo = (
            exercises.set_index("Código")["Descrição"].to_dict()
            if not exercises.empty
            else {}
        )

        if len(questoes) == 0:
            st.info("Esta avaliação não possui questões associadas.")
        else:
            for i, codigo in enumerate(questoes, start=1):
                descricao = descricao_por_codigo.get(codigo, "")
                st.write(f"{i}. {codigo} - {descricao}")

    # Impede renderização do restante da página
    st.stop()


# ===================================================
# MODO LISTAGEM PRINCIPAL
# ===================================================

aba_exercicios, aba_avaliacoes, aba_bases = st.tabs(
    ["Exercícios", "Avaliações", "Bases de Dados"]
)

with aba_exercicios:
    # Delega renderização da aba para o módulo exercises_tab
    # O próprio `render_aba_exercicios` já invoca `st.rerun()` nos
    # momentos em que o estado é alterado (adição/edição).
    # A chamada abaixo causava um loop infinito e impedia o carregamento
    # correto da página, especialmente quando comentada em testes.
    render_aba_exercicios()
    # não há mais necessidade de forçar rerun aqui



with aba_avaliacoes:
    # renderiza a aba usando o módulo dedicado
    render_aba_avaliacoes()


with aba_bases:
    render_aba_bases_dados()