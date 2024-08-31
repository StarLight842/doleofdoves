# import streamlit as st
# import prep, save as save

# st.session_state.messages = [{
#         "role": "assistant",
#         "content": "Welcome to DoveAI! What seems to be your problem today?"
# }]
# st.session_state.solved = False 
# pages = {
#     "Dole of Doves": [
#         st.Page(prep.prep_screen, title="Prepare for a meeting"),
#         st.Page(save.save_screen, title="SAVE ME I'M DYING"),
#     ]
# }
# st.caption("TEAM DOLE OF DOVES: LABOR DAY HACKATHON SUBMISSION")
# pg = st.navigation(pages)
# pg.run()
import av
import numpy as np
import pydub
import streamlit as st
from streamlit_webrtc import WebRtcMode, webrtc_streamer

if "x" not in st.session_state:
    st.session_state.x = 0

def process_audio(frame: av.AudioFrame) -> av.AudioFrame:
    raw_samples = frame.to_ndarray()
    st.write("count", np.size(raw_samples))
    return av.AudioFrame()


webrtc_streamer(
    key="audio-filter",
    mode=WebRtcMode.SENDRECV,
    audio_frame_callback=process_audio,
    async_processing=True,
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
)
st.write("x = ", st.session_state.x)