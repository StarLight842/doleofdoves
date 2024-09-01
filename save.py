import streamlit as st
from aihandler import Conversation


def save_screen():
    st.markdown("# We'll save you from ~~certain death~~ a functional absence")

    if "ai_state" not in st.session_state or st.button("Restart chat"):
        st.session_state["ai_state"] = Conversation()  
    # Display chat messages from history on app rerun
    if st.session_state["ai_state"].solved_id != "":
        st.markdown(st.session_state["ai_state"].get_ai_dialog())
    else:
        for message in st.session_state["ai_state"].messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    # React to user input
    if prompt := st.chat_input("Type here..."):
        if st.session_state["ai_state"].solved_id == "":
            st.session_state["ai_state"].update(prompt)
            st.rerun()
