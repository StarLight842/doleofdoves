import streamlit as st
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase, WebRtcMode, WebRtcStreamerContext
import time
from aiortc.contrib.media import MediaPlayer
import numpy as np
#
# SPEAKER
#
def speaker_tool():
    st.write("Click 'Start' to play a test sound. If you can't hear anything, then try changing your speaker in your computer settings. Here are instructions to do so for: [MacOS](https://support.apple.com/en-qa/guide/mac-help/mchlp2256), [Windows](https://www.dell.com/support/kbdoc/en-us/000189443/how-to-select-different-audio-output-devices-in-windows-10), and [ChromeOS](https://support.google.com/chromebook/answer/10045949?hl=en).")
    webrtc_streamer(
        key="streaming",
        mode=WebRtcMode.RECVONLY,
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
        media_stream_constraints={
            "video": False,
            "audio": True,
        },
        player_factory=lambda: MediaPlayer("rick.mp3"),
    )

#
# MICROPHONE
#
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
    st.write("Below is an external [site](https://www.fast.com) that automatically will measure your bandwidth upon launching this webpage. Click the refresh icon as needed to determine your internet speed; make sure that space them apart so that traffic will not be throttled, and the other devices on your network are using traffic approximately like they would during class time. We recommend speeds of at least 30-50 mbps or higher for OHS classes in Adobe Connect.")
    st.components.v1.iframe("https://fast.com", height=500)