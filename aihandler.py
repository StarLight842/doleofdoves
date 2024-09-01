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
system_instruction="You are a helpful tech support agent for Adobe Connect users named DoveAI.\nONLY IF NEEDED, have a short conversation (1-4 messages) with the client to pinpoint the issue they are experiencing; however in most cases the client will be direct and you should be able to identify the problem after the first message. Send a final message that only contains the ID of the correct dialog to show.\nBelow are the problems and corresponding IDs that you can return:\nMIC: No one can hear the client, or they are having microphone issues\nDISPL: The client can't see anyone, or they are having display issues\nCAM: No one can see the client, or they are having camera issues\nSND: Client can't hear anything, or they are having speaker issues\nINT: Client is having internet problems (e.g. video freezing), or they are having internet issues\nELSE: Another, distinct issue (e.g. with another aspect of the hardware)",
)

dialogs = {
"MIC": """
**If a ~~tree falls~~ you talk and no one hears it, did it really happen?**
It looks like there’s an issue with your microphone. If no one can hear you, make sure you have selected the right microphone and try a few different ones in our microphone testing tool. Once you've found the correct input device, navigate to the dropdown menu beneath the microphone icon in Adobe Connect and choose that device.
""",
"DISPL": """
**Hmmmm. Try glasses?**
If you can’t see anyone, make sure your display is set to the one you’re currently looking at (e.g. the one you’re filling out this form on). If you’re sure that you’re looking at the right display, try signing out and signing back in, or using the desktop version (or vice versa if you’re using the desktop one).

Download the desktop version of AC [here](https://helpx.adobe.com/adobe-connect/connect-downloads-updates.html)
""",
"CAM": """
**Just confirming: have you been using any invisibility spells recently?**
If you're not Harry Potter, it appears that your camera isn’t functioning. Make sure you have selected the right camera and try a few different ones in our camera testing tool. Once you've found the correct input device, navigate to the dropdown menu beneath the camera icon in Adobe Connect and choose that device.
""",
"SND": """
**Contact a hearing specialist.**
If you can’t hear anything, the most likely problem is that your speaker is muted. (Trust us, this is the case 90% of the time.) Otherwise, make sure you have selected the right speaker and try a few different ones in our speaker testing tool.
""",
"INT": """
**Maybe try wider bands?**
It appears your bandwidth is not up to par. (You can confirm this by checking our internet testing tool; we recommand 30-50 mbps or higher). The fastest hack to save on bandwidth is to select the three dots on your camera pod in AC then click “Pause incoming video.” This will freeze the video of all other participants (including your instructor), and should greatly reduce your network usage.
 For the long term, talk to your parents or guardians about a faster wifi plan or using wired internet (Ethernet); if those options aren’t possible, try switching to the desktop version of Adobe Connect, which is less network-demanding. 
""",
"ELSE": """
**Oops, you've exhausted our knowledge.**
It appears your problem is so rare (or we were so forgetful) that we didn't add a tool for it here. 

Fill out the [OHS tech support form](https://ohs.stanford.edu/techsupport) to get help from the professionals.
"""
}
links = {
"MIC": ["microphone", "test-your-microphone"],
"CAM": ["camera", "test-your-camera"],
"SND": ["speakers", "test-your-speakers"],
"INT": ["internet", "test-your-internet"],
}

class Conversation:
    def __init__(self):
        self.messages = [{
            "role": "assistant",
            "content": "Welcome to DoveAI! What seems to be your problem today?"
        }]
        self.solved_id = ""
        self.session = model.start_chat()
    def update(self, p):
        # get ai response
        response = self.session.send_message(p).text
        # check for solved
        for k in dialogs.keys():
            if k in response:
                self.solved_id = k
        # add to messages
        self.messages.append({"role": "user", "content": p})
        if self.solved_id == "":
            self.messages.append({"role": "assistant", "content": response})
    def get_ai_dialog(self):
        dialog = "✅ Problem solved by DoveAI"
        dialog += "\n\n" + dialogs[self.solved_id]
        if self.solved_id not in ["DISPL", "ELSE"]:
            dialog += "\n\n Try our simple " + links[self.solved_id][0] + " testing tool [here](https://doleofdoves.streamlit.app/prep_screen#"+links[self.solved_id][1]+")"
        if self.solved_id not in ["ELSE"]:
            dialog += "\n\n Still having issues? Fill out an [OHS tech support form](https://ohs.stanford.edu/techsupport) to get help from the professionals"
        return dialog