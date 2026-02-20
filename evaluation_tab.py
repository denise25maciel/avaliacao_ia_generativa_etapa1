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

    st.subheader("Gerador de avaliações")

    # inicializa estado do wizard para criação de avaliação
    if "wizard_step" not in st.session_state:
        st.session_state.wizard_step = 0      # 0 = inativo, 1/2/3 passos
    if "wizard_selected" not in st.session_state:
        st.session_state.wizard_selected = []
    if "wizard_order" not in st.session_state:
        st.session_state.wizard_order = []

    # botão de iniciar wizard
    if st.button("Criar avaliação", use_container_width=False):
        st.session_state.wizard_step = 1
        st.session_state.wizard_selected = []
        st.session_state.wizard_order = []
        st.rerun()

    st.divider()

    # se wizard ativo, renderiza o passo correspondente e retorna cedo
    if st.session_state.wizard_step != 0:
        step = st.session_state.wizard_step
        exercises = st.session_state.exercicios_df
        descricao_por_codigo = exercises.set_index("Código")["Descrição"].to_dict() if not exercises.empty else {}

        # Botões de navegação entre os passos
        col_steps = st.columns(3)
        with col_steps[0]:
            if st.button("Etapa 1: Seleção", use_container_width=True, type="primary" if step == 1 else "secondary", key="nav_step_1"):
                st.session_state.wizard_step = 1
                st.rerun()
        with col_steps[1]:
            if st.button("Etapa 2: Ordenação", use_container_width=True, type="primary" if step == 2 else "secondary", key="nav_step_2"):
                st.session_state.wizard_step = 2
                st.rerun()
        with col_steps[2]:
            if st.button("Etapa 3: Prova Final", use_container_width=True, type="primary" if step == 3 else "secondary", key="nav_step_3"):
                st.session_state.wizard_step = 3
                st.rerun()

        st.divider()

        if step == 1:
            st.header("Passo 1 – Seleção de exercícios")
            st.write("Selecione os exercícios na primeira coluna.")

            if exercises.empty:
                st.info("Não há exercícios cadastrados para seleção.")
                selecionados = []
            else:
                todos_codigos = exercises["Código"].tolist()
                todos_marcados = (
                    len(st.session_state.wizard_selected) == len(todos_codigos)
                    and len(todos_codigos) > 0
                )
                marcar_todos = st.checkbox(
                    "Selecionar todos",
                    value=todos_marcados,
                    key="wizard_toggle_all",
                )

                estado_anterior = st.session_state.get("wizard_toggle_all_prev", todos_marcados)
                if marcar_todos != estado_anterior:
                    st.session_state.wizard_selected = todos_codigos.copy() if marcar_todos else []
                    for codigo in todos_codigos:
                        st.session_state[f"wizard_sel_{codigo}"] = marcar_todos
                    st.session_state.wizard_toggle_all_prev = marcar_todos
                    st.rerun()
                st.session_state.wizard_toggle_all_prev = marcar_todos

                cab = st.columns([0.6, 1.2, 3.5, 1.5, 0.8, 1.2])
                cab[0].write(" ")
                cab[1].write("Código")
                cab[2].write("Descrição")
                cab[3].write("Fonte")
                cab[4].write("Ano")
                cab[5].write("Dificuldade")

                selecionados = []
                for _, row in exercises.iterrows():
                    codigo = row["Código"]
                    chave_checkbox = f"wizard_sel_{codigo}"
                    if chave_checkbox not in st.session_state:
                        st.session_state[chave_checkbox] = codigo in st.session_state.wizard_selected

                    cols = st.columns([0.6, 1.2, 3.5, 1.5, 0.8, 1.2])
                    marcado = cols[0].checkbox("", key=chave_checkbox)
                    cols[1].write(codigo)
                    cols[2].write(row["Descrição"])
                    cols[3].write(row["Fonte"])
                    cols[4].write(row["Ano"])
                    cols[5].write(row["Dificuldade"])

                    if marcado:
                        selecionados.append(codigo)

            st.session_state.wizard_selected = selecionados

            st.divider()
            col_buttons = st.columns([1, 4, 1])
            with col_buttons[0]:
                if st.button("Voltar", use_container_width=True, key="step1_back"):
                    st.session_state.wizard_step = 0
                    st.session_state.wizard_selected = []
                    st.session_state.wizard_order = []
                    st.rerun()
            with col_buttons[2]:
                if st.button("Próximo", use_container_width=True, key="step1_next"):
                    st.session_state.wizard_order = selecionados.copy()
                    st.session_state.wizard_step = 2
                    st.rerun()

        elif step == 2:
            st.header("Passo 2 – Ordenação")
            
            # Se wizard_order estiver vazio, copia dos selecionados
            if len(st.session_state.wizard_order) == 0 and len(st.session_state.wizard_selected) > 0:
                st.session_state.wizard_order = st.session_state.wizard_selected.copy()
                st.rerun()
            
            # Verifica se nenhum item foi selecionado
            if len(st.session_state.wizard_order) == 0:
                st.warning("⚠️ Você deve selecionar ao menos um exercício na Etapa 1 para continuar.")
                st.divider()
                col_buttons = st.columns([1, 4, 1])
                with col_buttons[0]:
                    if st.button("Voltar", use_container_width=True, key="step2_back_no_items"):
                        st.session_state.wizard_step = 1
                        st.rerun()
                return
            
            order = [codigo for codigo in st.session_state.wizard_order if codigo in descricao_por_codigo]
            st.session_state.wizard_order = order

            for i, codigo in enumerate(order):
                cols = st.columns([4, 1, 1])
                cols[0].write(f"{codigo} - {descricao_por_codigo.get(codigo, '')}")
                if cols[1].button("↑", key=f"up_{i}") and i > 0:
                    order[i], order[i-1] = order[i-1], order[i]
                    st.session_state.wizard_order = order
                    st.rerun()
                if cols[2].button("↓", key=f"down_{i}") and i < len(order)-1:
                    order[i], order[i+1] = order[i+1], order[i]
                    st.session_state.wizard_order = order
                    st.rerun()
            
            st.divider()
            col_buttons = st.columns([1, 4, 1])
            with col_buttons[0]:
                if st.button("Voltar", use_container_width=True, key="step2_back"):
                    st.session_state.wizard_step = 1
                    st.rerun()
            with col_buttons[2]:
                if st.button("Próximo", use_container_width=True, key="step2_next"):
                    st.session_state.wizard_step = 3
                    st.rerun()

        elif step == 3:
            st.header("Passo 3 – Prova final")
            for idx, codigo in enumerate(st.session_state.wizard_order, start=1):
                descricao = descricao_por_codigo.get(codigo, "")
                st.write(f"{idx}. {codigo} - {descricao}")
            
            st.divider()
            col_buttons = st.columns([1, 4, 1])
            with col_buttons[0]:
                if st.button("Voltar", use_container_width=True, key="step3_back"):
                    st.session_state.wizard_step = 2
                    st.rerun()
            with col_buttons[2]:
                if st.button("Salvar", use_container_width=True, key="step3_save"):
                    novo = {
                        "Título": f"Avaliação {len(st.session_state.avaliacoes_df)+1}",
                        "Data": pd.Timestamp.today().strftime("%Y-%m-%d"),
                        "Disciplina": "",
                        "ODS": "",
                    }
                    st.session_state.avaliacoes_df = pd.concat([
                        st.session_state.avaliacoes_df,
                        pd.DataFrame([novo])
                    ], ignore_index=True)
                    st.session_state.wizard_step = 0
                    st.session_state.wizard_selected = []
                    st.session_state.wizard_order = []
                    st.session_state.modo_avaliacoes = "lista"
                    st.rerun()

        return

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
