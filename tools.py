import streamlit as st

# SPEAKER
#
#
import sounddevice as sd
import numpy as np


def play_tone(frequency=1000, duration=3, samplerate=44100, device=None):
    """Play a tone through the specified audio output device."""
    t = np.linspace(0, duration, int(samplerate * duration), endpoint=False)
    signal = 0.5 * np.sin(2 * np.pi * frequency * t)
    if device is not None:
        sd.default.device = device
    sd.play(signal, samplerate)
    sd.wait()  
def speaker_tool():
    # get list of available output devices
    devices = sd.query_devices()
    output_devices = [device['name'] for device in devices if device['max_output_channels'] > 0]
    device_ids = [device['index'] for device in devices if device['max_output_channels'] > 0]


    if not output_devices:
        st.error("No output devices found.")
        return


    # adding the select box thing
    selected_device_name = st.selectbox("Select your speaker:", output_devices)
    selected_device_id = device_ids[output_devices.index(selected_device_name)]


    if st.button("Play Tone"):
        play_tone(device=selected_device_id)
        st.write("Listen for the tone.")
        heard = st.radio("Did you hear the tone?", ("Yes", "No"))


        if heard == "Yes":
            st.success(f"Great, change the speaker on Adobe Connect to {selected_device_name}! ")
        else:
            st.write("Try another speaker.")
