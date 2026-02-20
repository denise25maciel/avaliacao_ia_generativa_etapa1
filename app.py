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


def gerar_comando_ia(descricao_exercicio, tema_ods):
    return (
        f"Adapte o exercício a seguir para o contexto de '{tema_ods}', "
        f"mantendo o nível de dificuldade e a habilidade principal. "
        f"Exercício original: {descricao_exercicio}"
    )


def adaptar_exercicio_para_ods(descricao_exercicio, tema_ods):
    return (
        f"No contexto de {tema_ods}, {descricao_exercicio} "
        f"Relacione a solução técnica com impactos sociais, ambientais e de cidadania."
    )


def gerar_proximo_codigo_exercicio(df_exercicios):
    codigos_validos = []
    for codigo in df_exercicios["Código"].astype(str).tolist():
        if codigo.startswith("EX") and codigo[2:].isdigit():
            codigos_validos.append(int(codigo[2:]))
    proximo_numero = (max(codigos_validos) + 1) if codigos_validos else 1
    return f"EX{proximo_numero:03d}"


def render_painel_ia(idx, descricao, fonte, ano, dificuldade, view_only):
    ods_opcoes = [
        "ODS 1 - Erradicação da Pobreza",
        "ODS 3 - Saúde e Bem-Estar",
        "ODS 4 - Educação de Qualidade",
        "ODS 8 - Trabalho Decente e Crescimento Econômico",
        "ODS 9 - Indústria, Inovação e Infraestrutura",
        "ODS 10 - Redução das Desigualdades",
        "ODS 11 - Cidades e Comunidades Sustentáveis",
        "ODS 12 - Consumo e Produção Responsáveis",
        "ODS 13 - Ação Contra a Mudança Global do Clima",
        "ODS 16 - Paz, Justiça e Instituições Eficazes",
    ]

    tema_key = f"tema_ods_ex_{idx}"
    comando_key = f"comando_ia_ex_{idx}"
    comando_tema_key = f"comando_ia_tema_ex_{idx}"
    resultado_key = f"resultado_adaptacao_ex_{idx}"

    if tema_key not in st.session_state:
        st.session_state[tema_key] = "ODS 4 - Educação de Qualidade"

    st.subheader("Comandos para a IA")
    tema_ods = st.selectbox(
        "Tema ODS",
        options=ods_opcoes,
        key=tema_key,
        disabled=view_only,
    )

    if (
        comando_key not in st.session_state
        or st.session_state.get(comando_tema_key) != tema_ods
    ):
        st.session_state[comando_key] = gerar_comando_ia(descricao, tema_ods)
        st.session_state[comando_tema_key] = tema_ods

    st.text_area(
        "Insira os comandos para a IA",
        key=comando_key,
        height=180,
        label_visibility="collapsed",
        disabled=view_only,
    )

    if st.button("Processar", key="processar_ia", use_container_width=True, disabled=view_only):
        st.session_state[resultado_key] = adaptar_exercicio_para_ods(
            descricao_exercicio=descricao,
            tema_ods=tema_ods,
        )
        st.success("Exercício adaptado com sucesso.")

    st.subheader("Resultado da Adaptação")
    st.text_area(
        "Exercício adaptado",
        value=st.session_state.get(resultado_key, ""),
        height=220,
        label_visibility="collapsed",
        disabled=True,
    )

    if st.button("Salvar adaptação", key="salvar_adaptacao_ia", use_container_width=True, disabled=view_only):
        resultado_adaptado = st.session_state.get(resultado_key, "").strip()
        if not resultado_adaptado:
            st.warning("Processe a adaptação antes de salvar.")
        else:
            novo_codigo = gerar_proximo_codigo_exercicio(st.session_state.exercicios_df)
            novo_exercicio = {
                "Código": novo_codigo,
                "Descrição": resultado_adaptado,
                "Fonte": fonte,
                "Ano": int(ano),
                "Dificuldade": dificuldade,
            }
            st.session_state.exercicios_df = pd.concat(
                [st.session_state.exercicios_df, pd.DataFrame([novo_exercicio])],
                ignore_index=True,
            )
            st.success(f"Exercício adaptado salvo como novo registro ({novo_codigo}).")


if "exercicios_df" not in st.session_state:
    st.session_state.exercicios_df = inicializar_dados()

if "modo" not in st.session_state:
    st.session_state.modo = "lista"   # lista | editar

if "editando_idx" not in st.session_state:
    st.session_state.editando_idx = None

if "modo_magica" not in st.session_state:
    st.session_state.modo_magica = False

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
    modo_magica = st.session_state.get("modo_magica", False)

    codigo = df.at[idx, "Código"]
    descricao = df.at[idx, "Descrição"]
    fonte = df.at[idx, "Fonte"]
    ano = int(df.at[idx, "Ano"])
    dificuldade = df.at[idx, "Dificuldade"]

    if modo_magica:
        st.header("Adaptação do exercício")
        st.divider()
        st.subheader("Questão")
        st.text_area(
            "Questão original",
            value=descricao,
            height=180,
            disabled=True,
            label_visibility="collapsed",
        )
        st.caption(f"Código: {codigo} | Fonte: {fonte} | Ano: {ano} | Dificuldade: {dificuldade}")
        st.divider()

        render_painel_ia(idx, descricao, fonte, ano, dificuldade, view_only=False)

        if st.button("Voltar", key="voltar_magica", use_container_width=True):
            st.session_state.modo = "lista"
            st.session_state.editando_idx = None
            st.session_state.view_only = False
            st.session_state.modo_magica = False
            st.rerun()

        st.stop()

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
            st.session_state.modo_magica = False
            st.rerun()

        if b2.button("Cancelar", key="cancelar_edicao", use_container_width=True):
            st.session_state.modo = "lista"
            st.session_state.editando_idx = None
            st.session_state.view_only = False
            st.session_state.modo_magica = False
            st.rerun()

    # -------------------------
    # COLUNA LATERAL (PREVIEW)
    # -------------------------

    with col_direita:
        render_painel_ia(idx, descricao, fonte, ano, dificuldade, view_only)
        
        
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