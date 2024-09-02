import streamlit as st
import prep, save as save

st.session_state.messages = [{
        "role": "assistant",
        "content": "Welcome to DoveAI! What seems to be your problem today?"
}]
st.session_state.solved = False 
pages = {
    "Dole of Doves": [
        st.Page(save.save_screen, title="SAVE ME"),
        st.Page(prep.prep_screen, title="Prepare for a meeting"),
    ]
}
st.image("resources/logo.png", width=200)
st.caption("TEAM DOLE OF DOVES: LABOR DAY HACKATHON SUBMISSION")
pg = st.navigation(pages)
pg.run()