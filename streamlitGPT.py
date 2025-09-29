import streamlit as st
from openai import OpenAI

st.title("ChatGPT Like")

client = OpenAI(api_key = st.secrets['OPENAI_API_KEY'])

if "openai_models" is not st.session_state:
    st.session_state["openai_models"] = 'gpt-3.5-turbo'

if "messages" is not st.session_state:
    st.session_state["messages"] = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if prompt := st.chat_input("What's up?"):
    instructions = """Você é um secretário de uma clínica médica. Vocês atendem várias especialidades médicas. Interaja com o usuário e responda normalmente as perguntas dele. Quando ele quiser marcar uma consulta pergunte na ordem. 1.Qual o seu plano de saúde. 2.Melhor data e horário para a consulta. E se o plano de saúde for Notredame, informe ao usuário que não atendemos esse plano. """

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_models"],
            messages=[
                {"role": "user", "content": prompt},
                {"role": "system", "content": instructions}
            ],
            stream = True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistent", "content": response})
