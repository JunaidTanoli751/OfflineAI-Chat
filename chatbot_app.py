import streamlit as st
import ollama

st.set_page_config(page_title="Local Chatbot", page_icon="🤖", layout="centered")

st.title("💬 Local Chatbot (Ollama + Phi-3 Mini)")
st.write("Chat locally — no API, no internet required!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display previous chat messages
for role, content in st.session_state["messages"]:
    with st.chat_message(role):
        st.markdown(content)

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state["messages"].append(("user", user_input))

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = ollama.chat(model="phi3:mini-128k", messages=[
                {"role": "user", "content": user_input}
            ])
            reply = response["message"]["content"]
            st.markdown(reply)

    st.session_state["messages"].append(("assistant", reply))
