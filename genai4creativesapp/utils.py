import html
import streamlit as st
from pinecone import Pinecone
from pinecone_plugins.assistant.models.chat import Message
from dotenv import load_dotenv
import os

def get_key():
    load_dotenv()
    return os.getenv('PINECONE_API_KEY')

def clean_response(raw_text: str) -> str:
    # Unescape HTML and escaped characters
    text = html.unescape(raw_text)

    # Remove enclosing quotes if present (from tuple or representation)
    if text.startswith("('") and text.endswith("')"):
        text = text[2:-2]

    # Replace double backslashes and newlines
    text = text.replace("\\n", "\n").replace("\\'", "'").replace('\\"', '"')

    # Normalize extra newlines
    text = text.replace("\n\n\n", "\n\n").strip()

    return text 

def query_assistant(query):
    key = get_key()
    pc = Pinecone(api_key=key)
    assistant = pc.assistant.Assistant(assistant_name="genai-assistant")
    msg = Message(role="user", content=query)
    response = assistant.chat(messages=[msg])
    return clean_response(response['message']['content'])

def global_chat(title="💬 Ask the AI assistant"):
    """Renders a chat history + input; call this once per page."""

    # Keep one history list across the whole app
    if "chat_hist" not in st.session_state:
        st.session_state.chat_hist = []

    st.sidebar.divider()          # place chat toggle in the sidebar
    if st.sidebar.checkbox("Show chat", value=True):
        st.sidebar.markdown(f"### {title}")

        # show previous messages
        for role, msg in st.session_state.chat_hist:
            with st.sidebar.chat_message(role):
                st.markdown(msg, unsafe_allow_html=True)

        # input box
        if prompt := st.sidebar.chat_input("Type here…"):
            with st.sidebar.chat_message("user"):
                st.markdown(prompt)

            # === call your Pinecone assistant here =========================
    
            reply = query_assistant(prompt)
            # ===============================================================

            with st.sidebar.chat_message("assistant"):
                st.markdown(reply)

            # save to history
            st.session_state.chat_hist.append(("user", prompt))
            st.session_state.chat_hist.append(("assistant", reply))
 