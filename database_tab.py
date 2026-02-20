import streamlit as st
import pandas as pd
from datetime import datetime


def render_aba_bases_dados():
    """Renderiza o conteúdo da aba 'Bases de Dados'. Usa e atualiza
    `st.session_state.bases_df`.
    """

    # garante que o DataFrame exista
    if "bases_df" not in st.session_state:
        st.session_state.bases_df = pd.DataFrame({
            "ID": ["BD001", "BD002", "BD003"],
            "Nome": ["ENADE Computação 2021", "ENADE Computação 2023", "Concursos TI 2024"],
            "Data_Upload": ["2024-01-15", "2024-02-10", "2024-02-18"],
            "ODS": ["ODS 4", "ODS 4", "ODS 8"],
            "Tema": ["Educação", "Educação", "Trabalho Digno"],
        })

    if "visualizando_base" not in st.session_state:
        st.session_state.visualizando_base = None

    if "arquivos_importados" not in st.session_state:
        st.session_state.arquivos_importados = set()
    
    if "processando_upload" not in st.session_state:
        st.session_state.processando_upload = False

    df = st.session_state.bases_df

    st.subheader("Bases de Dados Cadastradas")

    # Componente para importar nova base de dados
    arquivo = st.file_uploader(
        "Importar base de dados",
        type=["csv", "xlsx", "json"],
        help="Faça upload de um arquivo CSV, Excel ou JSON contendo exercícios",
        key="uploader_bases"
    )

    if arquivo is not None and not st.session_state.processando_upload:
        # Cria um identificador único baseado no nome e tamanho do arquivo
        arquivo_id = f"{arquivo.name}_{arquivo.size}"
        
        # Verifica se este arquivo já foi processado
        if arquivo_id not in st.session_state.arquivos_importados:
            st.session_state.processando_upload = True
            
            try:
                # Lê o arquivo conforme o tipo
                if arquivo.name.endswith('.csv'):
                    df_importado = pd.read_csv(arquivo)
                elif arquivo.name.endswith('.xlsx'):
                    df_importado = pd.read_excel(arquivo)
                elif arquivo.name.endswith('.json'):
                    df_importado = pd.read_json(arquivo)

                # Adiciona a nova base ao DataFrame de bases
                nome_base = arquivo.name.split('.')[0]
                
                # Gera ID único para a nova base
                ultimo_id = len(st.session_state.bases_df) + 1
                id_base = f"BD{ultimo_id:03d}"
                
                data_upload = datetime.now().strftime("%Y-%m-%d")
                ods = "ODS 4"  # Pode ser ajustado
                tema = "Educação"  # Pode ser ajustado

                nova_base = {
                    "ID": id_base,
                    "Nome": nome_base,
                    "Data_Upload": data_upload,
                    "ODS": ods,
                    "Tema": tema,
                }

                st.session_state.bases_df = pd.concat(
                    [st.session_state.bases_df, pd.DataFrame([nova_base])],
                    ignore_index=True
                )
                
                # Marca o arquivo como processado
                st.session_state.arquivos_importados.add(arquivo_id)
                st.session_state.processando_upload = False

                st.success(f"✅ Base '{nome_base}' importada com sucesso!")
                st.rerun()

            except Exception as e:
                st.session_state.processando_upload = False
                st.error(f"❌ Erro ao importar arquivo: {str(e)}")

    st.divider()

    # Cabeçalho da tabela
    header = st.columns([0.7, 2, 3, 1.2, 1.5, 1, 0.5, 0.5])
    header[0].write("**ID**")
    header[1].write("**Nome**")
    header[2].write("**Data Upload**")
    header[3].write("**ODS**")
    header[4].write("**Tema**")
    header[5].write("")
    header[6].write("**Ver**")
    header[7].write("**Excluir**")

    for idx, row in df.iterrows():
        linha = st.columns([0.7, 2, 3, 1.2, 1.5, 1, 0.5, 0.5])
        linha[0].write(row["ID"])
        linha[1].write(row["Nome"])
        linha[2].write(row["Data_Upload"])
        linha[3].write(row["ODS"])
        linha[4].write(row["Tema"])
        linha[5].write("")

        if linha[6].button("👁️", key=f"ver_base_{idx}"):
            st.session_state.visualizando_base = row["Nome"]
            st.rerun()

        if linha[7].button("🗑️", key=f"deletar_base_{idx}"):
            st.session_state.bases_df = df.drop(idx).reset_index(drop=True)
            st.rerun()
