import streamlit as st

#
# SPEAKER
#
def speaker_tool():
    st.write("speaker "*100)

#
# MICROPHONE
#
def mic_tool():
    st.write("microphone "*100)

#
# CAMERA
#
from streamlit_webrtc import webrtc_streamer, WebRtcMode
import numpy as np
import av
def camera_tool():
    st.session_state.x = 0
    st.write("Click 'Start' to see a streamed output from your default camera. If the output isn't showing or is lower quality than you expect, try the 'Select device' menu (which also shows a preview of camera output) and go through the options available.")
    webrtc_ctx = webrtc_streamer(
        key="object-detection",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
        media_stream_constraints={"video": True, "audio": False},
        async_processing=True,
        audio_frame_callback=process_audio,
    )
    st.write("count = ", st.session_state.x)

def process_audio(frame: av.AudioFrame) -> av.AudioFrame:
    raw_samples = frame.to_ndarray()
    st.session_state.x = np.size(raw_samples)
    return frame



#
# INTERNET
#
def bandwidth_tool():
    st.write("internet "*100)


"""
from streamlit_webrtc import webrtc_streamer, WebRtcMode
def camera_tool():
    st.write("Click 'Start' to see a streamed output from your default camera. If the output isn't showing or is lower quality than you expect, try the 'Select device' menu (which also shows a preview of camera output) and go through the options available.")
    webrtc_ctx = webrtc_streamer(
        key="object-detection",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
        media_stream_constraints={"video": True, "audio": False},
        async_processing=True
    )
"""