# 📘 avaliacao_ia_generativa_etapa1  
# 🚀 ExerciseFlow  
### 🗂️ Sistema de Gestão de Exercícios Técnicos

---

## 🎯 Problema

Docentes de cursos técnicos enfrentam dificuldades na organização e reutilização de exercícios avaliativos. Entre os principais desafios estão:

- 📂 Fragmentação de questões em múltiplas fontes e arquivos;  
- 🔄 Ausência de controle estruturado sobre alterações realizadas;  
- 🧩 Dificuldade em adaptar exercícios para diferentes contextos;  
- 🌍 Inclusão manual e não padronizada de temas relacionados aos Objetivos de Desenvolvimento Sustentável (ODS);  
- ⏳ Alto tempo dedicado à organização e montagem de avaliações.  

Esse cenário gera:

- 🔁 Retrabalho  
- 🔎 Baixa rastreabilidade  
- 📉 Pouca padronização no processo de elaboração de provas e listas  

---

## 💡 Solução

O **ExerciseFlow** é uma aplicação web desenvolvida para centralizar e estruturar a gestão de exercícios técnicos.

A plataforma permite:

- ⬆️ Upload de bases de exercícios;  
- ✏️ Edição e adaptação de questões existentes;  
- 🌱 Inclusão e associação de temas ODS aos exercícios;  
- 🗃️ Organização estruturada das questões cadastradas;  
- 📝 Geração de avaliações a partir da seleção de exercícios.  

### 🎯 Objetivos da Proposta

- Reduzir o tempo de preparação de avaliações;  
- Aumentar a organização do acervo de questões;  
- Garantir maior controle sobre modificações realizadas.  

---

## 🧠 Metodologia de Desenvolvimento

O desenvolvimento da interface foi conduzido em **três etapas distintas**, utilizando diferentes modelos de LLM para análise comparativa de resultados.

| Etapa | Ferramenta Utilizada | Objetivo | Procedimento | Resultado Observado | Nº da Imagem | Inferências de UX |
|-------|----------------------|----------|--------------|--------------------|--------------|------------------|
| **Etapa 1** | ChatGPT | 🧩 Estruturar a problemática | Reformulação e organização da descrição do problema | Texto claro e organizado | — | Boa organização conceitual |
| **Etapa 2** | ChatGPT + Google LLM Stitch | 🎨 Gerar interface gráfica | ChatGPT → estrutura única e pouco organizada. <br> Stitch → hierarquia visual superior | Stitch apresentou melhor organização sequencial | Imagem 1 (ChatGPT) <br> Imagem 2 (Stitch) | Interfaces sequenciais favorecem clareza |
| **Etapa 3** | OpenAI Codex | 🛠️ Implementação prática | Primeira tentativa com descrição extensa → resultado intermediário. <br> Segunda tentativa com instruções curtas e progressivas | Estrutura modular superior e melhor controle de layout | Imagem 3 | Iteração incremental melhora UX |

---

## ⚙️ Observações Técnicas do Processo com Codex

Durante a implementação com o OpenAI Codex, verificou-se que a qualidade do resultado está diretamente relacionada ao nível de detalhamento das instruções.

### 🔎 Diagnóstico Inicial

Instruções genéricas produziram:

- Interfaces inconsistentes  
- Estrutura pouco organizada  

Especificações claras e segmentadas produziram:

- 🧱 Melhor arquitetura  
- 🧩 Componentização adequada  
- 🔀 Melhor definição de fluxos  

Foi necessário mapear explicitamente os fluxos da aplicação:

- 🏠 Interface principal (gestão e visualização de exercícios)  
- ➕ Fluxo interno de geração de nova avaliação  

Sem essa definição, ocorreu:

- 🔄 Alternância estrutural não controlada  
- 📌 Sobreposição de responsabilidades  

### ✅ Ajustes Aplicados

- 📍 Definição explícita de cada fluxo  
- 🔐 Separação entre interface principal e fluxos internos  
- 🪜 Implementação incremental  
- ✂️ Instruções curtas e sequenciais  

Resultado:

- 📐 Maior previsibilidade  
- 🧩 Organização modular  
- 🧱 Coerência estrutural  

---

## ✅ O que deu certo

- ⚡ Desenvolvimento rápido de componentes (formulários, tabelas, fluxos)  
- 🐞 Identificação de falhas no código  
- 🔧 Correções estruturais pontuais  
- ✍️ Auto completar acelerando produtividade  

---

## ⚠️ O que não deu certo

O sistema apresentou dificuldade para desenvolver interfaces:

- ❌ Não descritas em detalhe  
- ❌ Sem especificação explícita de componentes  

Houve exceções em interfaces simples.

Observou-se maior dificuldade nas seguintes regras de usabilidade:

---

## 📊 Avaliação segundo as Heurísticas de Nielsen

| Heurística | Descrição Sintética | Observação no Projeto |
|------------|--------------------|------------------------|
| 👁️ **Visibilidade do status do sistema** | Informar o usuário sobre o que está acontecendo | Falta de indicadores claros de estado |
| 🌍 **Correspondência com o mundo real** | Linguagem alinhada ao usuário | Estrutura conceitual adequada, mas organização visual limitada |
| 🔄 **Controle e liberdade** | Permitir desfazer/refazer ações | Ausência de mecanismos automáticos |
| 📏 **Consistência e padrões** | Padronização visual e comportamental | Dificuldade nas primeiras iterações |
| 🚫 **Prevenção de erros** | Evitar erros antes que ocorram | Validações não implementadas sem instrução explícita |
| 🧠 **Reconhecimento > Memorização** | Minimizar carga cognitiva | Algumas estruturas exigiam interpretação adicional |
| ⚡ **Flexibilidade e eficiência** | Usuários experientes devem operar mais rápido | Eficiência melhorou com instruções curtas |
| 🎨 **Estética minimalista** | Evitar excesso de informação | Primeiras versões pouco organizadas |
| 🛠️ **Diagnóstico e recuperação de erros** | Mensagens claras de erro | Ausência de mensagens orientativas |
| 📘 **Ajuda e documentação** | Documentação acessível | Não houve geração automática |

---

## 📐 Avaliação segundo Leis e Princípios de Usabilidade

| Lei / Princípio | Descrição Sintética | Observação no Projeto |
|-----------------|--------------------|------------------------|
| 🧭 **Lei de Jacob** | Expectativa de padrões familiares | Não aderiu totalmente ao modelo mental específico |
| 🎯 **Lei de Fitts** | Distância e tamanho impactam tempo de ação | Elementos interativos distantes |
| 🧮 **Lei de Miller** | Limite cognitivo ≈ 7±2 elementos | Respeitada, exceto em bases extensas |
| 📈 **Regra do Pico-Fim** | Experiência avaliada por picos e final | Aplicação superficial |
| 💎 **Efeito Estética-Usabilidade** | Interfaces bonitas parecem mais usáveis | Organização visual inconsistente |
| ⏱️ **Limiar de Doherty** | Resposta < 400ms mantém engajamento | Sem preocupação explícita com performance |

---

## 🧾 Conclusão

O trabalho demonstrou que modelos de IA generativa são viáveis para apoiar o desenvolvimento técnico de aplicações web, especialmente para:

- 🧱 Estruturação inicial de interfaces  
- ⚡ Construção rápida de componentes  
- 🐞 Identificação de falhas no código  

Contudo, foram observadas limitações relacionadas a:

- ⏳ Controle de estado  
- 🔀 Gerenciamento de múltiplos fluxos  
- 📏 Padronização progressiva  
- 🚀 Otimização de desempenho  

Conclui-se que a IA apresenta potencial consistente como ferramenta assistiva, desde que:

- 📌 Receba instruções claras  
- 🗺️ Tenha fluxos previamente definidos  
- 👩‍💻 Seja supervisionada por desenvolvedor  

A qualidade do resultado depende diretamente da clareza das especificações e da validação arquitetural contínua.
