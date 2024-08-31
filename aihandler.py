import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyD5_exF1FXndIBKEOKQsyfL7pPXug0ZGcs")
# Create the model
generation_config = {
"temperature": 1,
"top_p": 0.95,
"top_k": 64,
"max_output_tokens": 8192,
"response_mime_type": "text/plain",
}
# set up model
model = genai.GenerativeModel(
model_name="gemini-1.5-flash",
generation_config=generation_config,
# safety_settings = Adjust safety settings
# See https://ai.google.dev/gemini-api/docs/safety-settings
system_instruction="You are a helpful tech support agent for Adobe Connect users. Below are the dialog options, along with IDs, that you can return:\nMIC: No one can hear the client\nDISPL: The client can't see anyone\nCAM: No one can see the client\nSND: Client can't hear anything\nINT: Client is having internet problem (e.g. video freezing)\nHave a short conversation (1-4) message exchanged with the client to pinpoint the issue they are experiencing, then send a final message that only contains the ID of the correct dialog to show.\n",
)

def get_history(st_hist):
    history = []
    role_map = {"user": "user", "assistant": "model"}
    for x in st_hist:
        item = {"role": role_map[x["role"]], "parts": [x["content"]]}
        history.append(item)
    return history   

def get_response(input, st_hist):
    chat_session = model.start_chat(history=get_history(st_hist))
    response = chat_session.send_message(input)
    return response.text 

responses = {
"MIC": """
**If a ~~tree falls~~ you talk and no one hears it, did it really happen?**
It looks like there’s an issue with your microphone. If no one can hear you, make sure you have selected the right microphone and try a few different ones in our microphone testing tool.
""",
"DISPL": """
**Hmmmm. Try glasses?**
If you can’t see anyone, make sure your display is set to the one you’re currently looking at (e.g. the one you’re filling out this form on). If you’re sure that you’re looking at the right display, try signing out and signing back in, or using the desktop version (or browser version if you’re using the desktop one).
""",
"CAM": """
**If no one can see you, it’s a ‘them’ problem.**
All jokes aside though, it appears that your camera isn’t functioning. Make sure you have selected the right camera and try a few different ones in our camera testing tool.
""",
"SND": """
**Contact a hearing specialist.**
If you can’t hear anything, the most likely problem is that your speaker is muted. (Trust us, this is the case 90% of the time.) Otherwise, make sure you have selected the right speaker and try a few different ones in our speaker testing tool.
""",
"INT": """
**Try Ferizon Internet. Use [this affiliate link](ferizon.com) to get 10% off.**
It appears your bandwidth is not up to par. (You can confirm this by checking our bandwidth testing tool). The fastest hack to save on bandwidth is to select the three dots on your camera pod in AC then click “Pause incoming video.” This will freeze the video of all other participants (including your instructor), and should greatly reduce your network usage.
 For the long term, talk to your parents or guardians about a faster wifi plan or using wired internet (Ethernet); if those options aren’t possible, try switching to the desktop version of Adobe Connect, which is less network-demanding. 
""",
}
links = {
"MIC": ["microphone", "test-your-microphone"],
"DISPL": ["", "https://helpx.adobe.com/adobe-connect/connect-downloads-updates.html"],
"CAM": ["camera", "test-your-camera"],
"SND": ["speakers", "test-your-speakers"],
"INT": ["internet", "test-your-internet"],
}