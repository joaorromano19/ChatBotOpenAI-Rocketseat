# ChatBotOpenAI-Rocketseat

Este projeto é uma aplicação web interativa desenvolvida com [Streamlit](https://streamlit.io/) e [OpenAI API](https://platform.openai.com/docs), que simula um assistente virtual estilo ChatGPT. O assistente atua como um **secretário de clínica médica**, capaz de responder perguntas e auxiliar no agendamento de consultas.

## 💡 Funcionalidades

- Interface de chat estilo ChatGPT
- Persistência de mensagens na sessão
- Respostas geradas via modelo `gpt-3.5-turbo`
- Comportamento personalizado para agendamentos:
  - Pergunta sobre plano de saúde
  - Solicita data e horário preferido
  - Informa que **não atende o plano Notredame**

## 🛠️ Tecnologias Utilizadas

- Python
- Streamlit
- OpenAI API

## 🚀 Como Executar Localmente

1. **Clone o repositório:**

   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio

2. **Crie o arquivo de segredos:**

  No diretório .streamlit, crie o arquivo secrets.toml com sua chave da OpenAI:
  OPENAI_API_KEY = "sua-chave-aqui"

3. **Instale as dependências:**

   pip install streamlit openai

5. **Execute o app:**

  streamlit run app.py
