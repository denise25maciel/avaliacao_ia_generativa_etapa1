import streamlit as st
import pandas as pd

# Dados de teste
exercicios_data = [
    {"ID": 1, "Enunciado": "Resolva a equação x+2=4.", "Tema": "Matemática Básica", "ODS": "4 - Educação de Qualidade", "Dificuldade": "Simples", "Origem": "Concurso 2020"},
    {"ID": 2, "Enunciado": "Explique o conceito de biodiversidade.", "Tema": "Biologia", "ODS": "15 - Vida Terrestre", "Dificuldade": "Intermediário", "Origem": "Concurso 2021"},
    {"ID": 3, "Enunciado": "Calcule a derivada de x^2.", "Tema": "Cálculo", "ODS": "4 - Educação de Qualidade", "Dificuldade": "Avançado", "Origem": "Concurso 2022"},
    {"ID": 4, "Enunciado": "Liste três fontes de energia renovável.", "Tema": "Ciências", "ODS": "7 - Energia Limpa", "Dificuldade": "Simples", "Origem": "Concurso 2023"},
]
df_exercicios = pd.DataFrame(exercicios_data)

# Sidebar - Upload e Filtros
st.sidebar.header("Upload e Filtros")
uploaded_file = st.sidebar.file_uploader("Upload da base de exercícios", type=["csv", "xlsx"])
temas = df_exercicios["Tema"].unique().tolist()
ods = df_exercicios["ODS"].unique().tolist()

filtro_tema = st.sidebar.multiselect("Filtrar por tema", temas)
filtro_ods = st.sidebar.multiselect("Filtrar por ODS", ods)
filtro_dificuldade = st.sidebar.selectbox("Nível de dificuldade", ["Todos", "Simples", "Intermediário", "Avançado"])
filtro_palavra = st.sidebar.text_input("Buscar por palavra-chave")

# Filtragem
df_filtrado = df_exercicios.copy()
if filtro_tema:
    df_filtrado = df_filtrado[df_filtrado["Tema"].isin(filtro_tema)]
if filtro_ods:
    df_filtrado = df_filtrado[df_filtrado["ODS"].isin(filtro_ods)]
if filtro_dificuldade != "Todos":
    df_filtrado = df_filtrado[df_filtrado["Dificuldade"] == filtro_dificuldade]
if filtro_palavra:
    df_filtrado = df_filtrado[df_filtrado["Enunciado"].str.contains(filtro_palavra, case=False)]

# Área principal - Tabela de Exercícios
st.title("Gestão de Exercícios para Provas")
st.subheader("Exercícios Cadastrados")
st.dataframe(df_filtrado, use_container_width=True)

# Ações por exercício
st.subheader("Ações")
for idx, row in df_filtrado.iterrows():
    st.markdown(f"**Enunciado:** {row['Enunciado']}")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Adaptar", key=f"adaptar_{row['ID']}"):
            st.session_state[f"adaptar_{row['ID']}"] = True
    with col2:
        if st.button("Vincular ODS", key=f"ods_{row['ID']}"):
            st.session_state[f"ods_{row['ID']}"] = True
    with col3:
        if st.button("Histórico", key=f"hist_{row['ID']}"):
            st.session_state[f"hist_{row['ID']}"] = True
    # Adaptação
    if st.session_state.get(f"adaptar_{row['ID']}"):
        st.info("Adaptação de exercício")
        st.text_area("Exercício original", value=row['Enunciado'], disabled=True)
        nova_versao = st.text_area("Nova versão do exercício", key=f"nova_{row['ID']}")
        novo_nivel = st.selectbox("Novo nível de dificuldade", ["Simples", "Intermediário", "Avançado"], key=f"nivel_{row['ID']}")
        if st.button("Salvar adaptação", key=f"salvar_{row['ID']}"):
            st.success("Adaptação salva (simulado)")
    # Vinculação ODS
    if st.session_state.get(f"ods_{row['ID']}"):
        st.info("Vinculação com ODS")
        novo_ods = st.selectbox("Selecione o ODS", ods, key=f"ods_sel_{row['ID']}")
        justificativa = st.text_area("Justificativa da vinculação", key=f"just_{row['ID']}")
        if st.button("Salvar vinculação", key=f"salvar_ods_{row['ID']}"):
            st.success("Vinculação salva (simulado)")
    # Histórico (simulado)
    if st.session_state.get(f"hist_{row['ID']}"):
        st.info("Histórico de versões (simulado)")
        st.write("Versão original:", row['Enunciado'])
        st.write("Versão adaptada: (exemplo)")
        st.write("...")
    st.markdown("---")

# Organização e Progressão das Questões
st.header("Exibição Progressiva por Tema")
tema_prog = st.selectbox("Tema para exibição progressiva", temas)
for nivel in ["Simples", "Intermediário", "Avançado"]:
    st.subheader(nivel)
    questoes_nivel = df_exercicios[(df_exercicios["Tema"] == tema_prog) & (df_exercicios["Dificuldade"] == nivel)]
    for _, q in questoes_nivel.iterrows():
        st.markdown(f"- {q['Enunciado']}")
