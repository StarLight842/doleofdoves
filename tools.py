import streamlit as st
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase, WebRtcMode
import time
import numpy as np
#
# SPEAKER
#
def speaker_tool():
    st.write("speaker "*100)

#
# MICROPHONE
#
import streamlit as st
def mic_tool():
    st.write("Click 'Start' to show a bar with the current volume level of your incoming mic (e.g. it should increase if you do something loud for a few seconds e.g. scream). It will be a little janky due to software limitations. If the volume isn't updating or is different than what you expect, try the 'Select device' menu and go through the options available.")

    webrtc_ctx = webrtc_streamer(
        key="speech-to-text",
        mode=WebRtcMode.SENDONLY,
        audio_receiver_size=1024,
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
        media_stream_constraints={"video": False, "audio": True},
    )

    status_indicator = st.empty()

    if not webrtc_ctx.state.playing:
        return

    status_indicator.write("Loading...")

    while 1==1:
        if webrtc_ctx.audio_receiver:
            try:
                audio_frames = webrtc_ctx.audio_receiver.get_frames(timeout=1)
                volumes = []
                for f in audio_frames:
                    volumes.append(np.average(f.to_ndarray()))
                with status_indicator:
                    volume = int(np.average(volumes))
                    st.slider("Volume input level", min_value=-50, max_value=200, value=volume)
            except:
                pass
        time.sleep(0.05)
#
# CAMERA
#
def camera_tool():
    st.write("Click 'Start' to see a streamed output from your default camera. If the output isn't showing or is lower quality than you expect, try the 'Select device' menu (which also shows a preview of camera output) and go through the options available.")
    webrtc_ctx = webrtc_streamer(
        key="object-detection",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
        media_stream_constraints={"video": True, "audio": False},
        async_processing=True
    )

#
# INTERNET
#
def bandwidth_tool():
    st.write("internet "*100)
