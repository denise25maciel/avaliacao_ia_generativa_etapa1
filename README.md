# ExerciseFlow  
### Sistema de Gestão de Exercícios Técnicos

---

## 📌 Visão Geral

O **ExerciseFlow** é uma aplicação web voltada à organização, adaptação e versionamento de exercícios técnicos, com suporte à associação aos Objetivos de Desenvolvimento Sustentável (ODS).

---

## 🎯 Problema Identificado

Docentes enfrentam:

- 🔎 Fragmentação de exercícios em múltiplos arquivos  
- 🔁 Retrabalho frequente  
- 🧩 Falta de versionamento estruturado  
- 🌱 Inclusão manual de temas ODS  
- ⏱ Alto tempo de preparação de avaliações  

**Impacto:** baixa rastreabilidade, pouca padronização e ineficiência operacional.

---

## 💡 Solução Proposta

A plataforma permite:

- 📤 Upload de bases de exercícios  
- ✏️ Edição e adaptação de questões  
- 🌍 Associação com ODS  
- 📚 Organização estruturada  
- 📝 Geração de avaliações personalizadas  

**Resultado esperado:**  
Redução de tempo, aumento de controle e melhor organização do acervo.

---

## 🧪 Metodologia de Desenvolvimento

O desenvolvimento da interface foi conduzido em três etapas, com análise comparativa entre ferramentas.

| Etapa | Ferramenta | Foco | Procedimento | Resultado | Evidência |
|------:|------------|------|--------------|----------|----------|
| **1** | ChatGPT | Estruturação do problema | Reformulação e organização da descrição do problema para especificação de interface | Texto claro e estruturado | — |
| **2** | ChatGPT + Google Stitch | Geração visual | Tentativa inicial no ChatGPT (resultado limitado). Repetição no Stitch com descrição adaptada | Melhor hierarquia visual e fluxo sequencial | Imagem 1 (ChatGPT) / Imagem 2 (Stitch) |
| **3** | OpenAI Codex | Implementação | Geração inicial intermediária. Depois, reinício com prompts curtos e sequenciais | Melhor modularização e previsibilidade de layout | Imagem 3 |

---

## 🔄 Fluxos Identificados (Codex)

Durante o desenvolvimento, foi necessário explicitar e separar fluxos para evitar alternância estrutural entre telas.

```text
[Gestão de Exercícios]
        ↓
[Seleção de Exercícios]
        ↓
[Geração de Avaliação]