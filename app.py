import streamlit as st
from responses import SUGGESTED_QUESTIONS, get_response

st.set_page_config(page_title="Chatbot AI Dasar", page_icon="🤖")

st.title("🤖 Chatbot AI Dasar")
st.caption("Chatbot sederhana untuk menjawab pertanyaan dasar tentang Artificial Intelligence.")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Halo, saya siap membantu menjawab pertanyaan tentang AI dasar."}
    ]


def add_chat_message(prompt):
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = get_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})


with st.sidebar:
    st.header("Menu")
    st.write("Contoh pertanyaan:")

    for question in SUGGESTED_QUESTIONS:
        if st.button(question, use_container_width=True):
            add_chat_message(question)
            st.rerun()

    if st.button("Hapus Riwayat Chat"):
        st.session_state.messages = [
            {"role": "assistant", "content": "Halo, saya siap membantu menjawab pertanyaan tentang AI dasar."}
        ]
        st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Tulis pertanyaan Anda di sini...")

if prompt:
    add_chat_message(prompt)
    st.rerun()
