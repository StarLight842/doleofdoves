import streamlit as st
import aihandler

st.session_state.messages = [{
        "role": "assistant",
        "content": "Welcome to DoveAI! What seems to be your problem today?"
}]
st.session_state.solved = False 

def save_screen():   

    title = "# We'll save you from ~~certain death~~ a functional absence"
    st.markdown(f"{title}", unsafe_allow_html=True)
    # start chat
    if st.button("Restart chat"):
        st.session_state.messages = [{
            "role": "assistant",
            "content": "Welcome to DoveAI! What seems to be your problem today?"
        }]
        st.session_state.solved = False  
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("Type here..."):
        if not st.session_state.solved:
        
            # Display user message in chat message container
            with st.chat_message("user"):
                st.markdown(prompt)
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})

            response = aihandler.get_response(prompt, st.session_state.messages)
            for k in aihandler.responses.keys():
                if k in response:
                    response = aihandler.responses[k]
                    st.session_state.solved = True
                    st.session_state.id = k
                    break
            
            with st.chat_message("assistant"):
                st.markdown(response)
                if st.session_state.solved:
                    if st.session_state.id == "DISPL":
                        st.markdown("Download the desktop version of AC [here]("+aihandler.links['DISPL'][1]+")")
                    else:
                        st.markdown("Try our simple " + aihandler.links[st.session_state.id][0] + " testing tool [here](#"+aihandler.links[st.session_state.id][1]+")")
            st.session_state.messages.append({"role": "assistant", "content": response})
            print(st.session_state.messages)



            
