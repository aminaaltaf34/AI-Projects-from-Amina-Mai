import streamlit as st

from chatbot import FAQS, get_answer

st.set_page_config(page_title="FAQ Chatbot", page_icon="🤖")
st.title("🤖 ShopEasy FAQ Chatbot")
st.caption("Ask me about orders, shipping, returns and payments.")

# Sidebar mn sample questions
with st.sidebar:
    st.subheader("Try asking")
    for faq in FAQS[:6]:
        st.write("•", faq["question"])

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! 👋 How can I help you today?"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
if prompt := st.chat_input("Type your question here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    answer, score = get_answer(prompt)
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.write(answer)
