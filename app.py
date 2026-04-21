import streamlit as st
from responses import get_response

st.set_page_config(page_title="Chatbot AI Dasar", page_icon="🤖")

st.title("🤖 Chatbot AI Dasar")
st.caption("Chatbot sederhana untuk menjawab pertanyaan dasar tentang Artificial Intelligence.")

with st.sidebar:
    st.header("Menu")
    st.write("Contoh pertanyaan:")
    st.write("- Apa itu AI?")
    st.write("- Apa itu Machine Learning?")
    st.write("- Apa itu Deep Learning?")
    st.write("- Apa itu NLP?")
    st.write("- Apa itu Computer Vision?")

    if st.button("Hapus Riwayat Chat"):
        st.session_state.messages = [
            {"role": "assistant", "content": "Halo, saya siap membantu menjawab pertanyaan tentang AI dasar."}
        ]
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Halo, saya siap membantu menjawab pertanyaan tentang AI dasar."}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Tulis pertanyaan Anda di sini...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = get_response(prompt)

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()