import streamlit as st
import save as save
import tools
def prep_screen():
    st.title("Prepare for a meeting")
    st.write("Below are all of the tools that you can use to test your hardware.")

    st.markdown("""[Test your microphone](#test-your-microphone)""")
    st.markdown("""[Test your camera](#test-your-camera)""")
    st.markdown("""[Test your speakers](#test-your-speakers)""")
    st.markdown("""[Test your internet](#test-your-internet)""")
    
    st.markdown("## Test your microphone")
    tools.mic_tool()
    st.markdown("## Test your camera")
    tools.camera_tool()
    st.markdown("## Test your speakers")
    tools.speaker_tool()
    st.markdown("## Test your internet")
    tools.bandwidth_tool()