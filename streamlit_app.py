import streamlit as st
import prep, save as save

pages = {
    "Dole of Doves": [
        st.Page(prep.prep_screen, title="Prepare for a meeting"),
        st.Page(save.save_screen, title="SAVE ME I'M DYING"),
    ]
}
st.caption("TEAM DOLE OF DOVES: LABOR DAY HACKATHON SUBMISSION")
pg = st.navigation(pages)
pg.run()
