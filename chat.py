import streamlit as st    
import time 

# Ensure the assistant is initialized
if "assistant" not in st.session_state:
    from chatgpt_assistant import ChatGPTAssistant
    st.session_state.assistant = ChatGPTAssistant()

#@st.dialog("Sind Sie sicher?")
def appointment_dialog():
    with st.popover("End chat"):
        st.markdown("Are you sure?")
        if st.button("Yes"):
            st.session_state["button_clicked"] = "Yes"
            print("Button Clicked")
            st.write(f"You decided for: {st.session_state['button_clicked']}")
            st.session_state["page"] = "thanks"
            st.rerun()
        
        if st.button("No"):
            st.session_state["button_clicked"] = "No"
            st.rerun()


def create_appointment_bttns(): 
    with st.popover('Would you like to make an appointment with a doctor?', use_container_width=True):
        st.button("Yes", key="btn1",
                  on_click=lambda: st.session_state.update(button_clicked="Make an appointment"), use_container_width=True)
        st.button("No", key="btn2",
                  on_click=lambda: st.session_state.update(button_clicked="Do not make appointment"), use_container_width=True)


def get_assistant_response():
    # Get last user message string
    msg = st.session_state.messages[-1]["content"]
    response = st.session_state.assistant.chat(msg)
    return response


def chat_page(): 
    # Initialize messages if not present
    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.subheader("Chat", divider="gray")
    st.markdown("There may be delays in the responses from the artificial intelligence assistant.")

    # Initial assistant greeting
    if not st.session_state.messages:
        with st.chat_message("assistant"): 
            st.markdown("Hello! How may I help you?")
    
    # ✅ Display chat messages from session state
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask a question"):
        with st.chat_message("user"):
            st.markdown(prompt)

        # ✅ Append user message to session state
        st.session_state.messages.append({"role": "user", "content": prompt})

        # ✅ Get assistant response and store it
        with st.spinner("One moment, please"):
            assistant_response = get_assistant_response()
            st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        
        with st.chat_message("assistant"):
            st.markdown(assistant_response)

    # Appointment dialog popover
    with st.container():
        if st.session_state.messages: 
            appointment_dialog()
            #create_appointment_bttns()
