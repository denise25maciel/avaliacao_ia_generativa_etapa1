import streamlit as st
import pandas as pd


def render_aba_exercicios():
    """Renderiza o conteúdo da aba 'Exercícios'. Usa e atualiza `st.session_state.exercicios_df`.
    """
    # garante que o DataFrame exista
    if "exercicios_df" not in st.session_state:
        # Inicializa com alguns exercícios de exemplo
        st.session_state.exercicios_df = pd.DataFrame({
            "Código": ["EX001", "EX002", "EX003", "EX004", "EX005"],
            "Descrição": [
                "Sobre estruturas de dados lineares, qual estrutura segue o princípio FILO?",
                "Qual é a complexidade de tempo do algoritmo Quick Sort no melhor caso?",
                "Qual protocolo da camada de transporte garante entrega confiável de dados?",
                "Em Programação Orientada a Objetos, qual princípio garante que detalhes internos sejam ocultados?",
                "Qual é a diferença entre compilador e interpretador?"
            ],
            "Fonte": ["ENADE", "ENADE", "ENADE", "ENADE", "Concurso"],
            "Ano": [2021, 2021, 2021, 2023, 2024],
            "Dificuldade": ["Médio", "Médio", "Médio", "Médio", "Fácil"],
            "Origem": ["ENADE Computação 2021", "ENADE Computação 2021", "ENADE Computação 2021", "ENADE Computação 2023", "Concursos TI 2024"],
        })

    df = st.session_state.exercicios_df
    
    # Garantir que a coluna "Origem" existe (compatibilidade com dados antigos)
    if "Origem" not in df.columns:
        df["Origem"] = "Dados Legados"
        st.session_state.exercicios_df = df

    if st.button("Adicionar novo exercício"):
        novo = {
            "Código": "",
            "Descrição": "",
            "Fonte": "ENADE",
            "Ano": 2024,
            "Dificuldade": "Fácil",
            "Origem": "Manual",
        }
        st.session_state.exercicios_df = pd.concat([df, pd.DataFrame([novo])], ignore_index=True)
        st.session_state.editando_idx = len(st.session_state.exercicios_df) - 1
        st.session_state.modo = "editar"
        st.session_state.modo_magica = False
        # precisamos recriar a interface imediatamente após a alteração do estado
        # `st.rerun()` (ou `st.experimental_rerun()`) força o Streamlit a reexecutar o
        # script desde o topo. Sem ela a atualização só aparece num clique seguinte
        # ou outra interação. Comentá‑la não causa erro, mas faz com que a página
        # pareça não carregar/atualizar até o usuário fazer algo.
        st.rerun()

    st.divider()

    # Cabeçalho com colunas extras para visualizar/editar/mágica/deletar
    # pesos menores nas ações para maximizar espaço dos dados
    header = st.columns([1, 3, 2, 1, 1, 2, 0.7, 0.7, 0.7, 0.7])
    header[0].write("Código")
    header[1].write("Descrição")
    header[2].write("Fonte")
    header[3].write("Ano")
    header[4].write("Dificuldade")
    header[5].write("Origem")
    header[6].write(" ")
    header[7].write(" ")
    header[8].write(" ")
    header[9].write(" ")

    for idx, row in df.iterrows():
        linha = st.columns([1, 3, 2, 1, 1, 2, 0.7, 0.7, 0.7, 0.7])
        linha[0].write(row["Código"])
        linha[1].write(row["Descrição"])
        linha[2].write(row["Fonte"])
        linha[3].write(row["Ano"])
        linha[4].write(row["Dificuldade"])
        linha[5].write(row.get("Origem", "N/A"))

        # visualizar redireciona para edição em modo somente leitura
        if linha[6].button("👁️", key=f"ver_{idx}"):
            st.session_state.editando_idx = idx
            st.session_state.modo = "editar"
            st.session_state.view_only = True
            st.session_state.modo_magica = False
            st.rerun()

        if linha[7].button("✏️", key=f"editar_{idx}"):
            st.session_state.editando_idx = idx
            st.session_state.modo = "editar"
            st.session_state.view_only = False
            st.session_state.modo_magica = False
            # atualização do estado e rerun para mudar a tela
            st.rerun()

        if linha[8].button("🪄", key=f"magica_{idx}"):
            st.session_state.editando_idx = idx
            st.session_state.modo = "editar"
            st.session_state.view_only = False
            st.session_state.modo_magica = True
            st.rerun()

        if linha[9].button("🗑️", key=f"deletar_{idx}"):
            st.session_state.exercicios_df = df.drop(idx).reset_index(drop=True)
            st.rerun()


