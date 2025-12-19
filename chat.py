import streamlit as st    
import time 

#@st.dialog("Sind Sie sicher?")
def appointment_dialog():
    with st.popover("End chat"):
        st.markdown("Are you sure?")
        if st.button("Yes"):
            st.session_state["button_clicked"] = "Yes"
            # ✅ DO NOT clear messages here; allow saving first
            st.session_state.conversation_started = False
            st.session_state["page"] = "thanks"
            st.rerun()
    
        if st.button("No"):
            st.session_state["button_clicked"] = "No"
            st.rerun()


def create_appointment_bttns(): 
    with st.popover('Would you like to make an appointment with a doctor?', use_container_width=True):
        st.button(
            "Yes",
            key="btn1",
            on_click=lambda: st.session_state.update(button_clicked="Make an appointment"),
            use_container_width=True
        )
        st.button(
            "No",
            key="btn2",
            on_click=lambda: st.session_state.update(button_clicked="Do not make appointment"),
            use_container_width=True
        )


def get_assistant_response(prompt: str):
    # ✅ Unified interface (no direct access to assistant.messages)
    return st.session_state.assistant.chat(prompt)


def chat_page(): 
    # ---------------------------------
    # Conversation lifecycle flag
    # ---------------------------------
    if "conversation_started" not in st.session_state:
        st.session_state.conversation_started = False

    # ---------------------------------
    # Initialize message history once
    # ---------------------------------
    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.subheader("Chat", divider="gray")
    st.markdown(
        "There may be delays in the responses from the artificial intelligence assistant."
    )

    # ---------------------------------
    # Initial assistant greeting (ONCE)
    # ---------------------------------
    if not st.session_state.conversation_started:
        with st.chat_message("assistant"):
            st.markdown("Hello! How may I help you?")

    # ---------------------------------
    # Render full chat history
    # ---------------------------------
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    
    # ---------------------------------
    # Chat input
    # ---------------------------------
    if prompt := st.chat_input("Ask a question"):
        st.session_state.conversation_started = True

        # ✅ Store and render user message
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })
        with st.chat_message("user"):
            st.markdown(prompt)

        # ✅ Get assistant response
        with st.spinner("One moment, please"):
            assistant_response = get_assistant_response(prompt)

        # ✅ Store and render assistant response
        st.session_state.messages.append({
            "role": "assistant",
            "content": assistant_response
        })
        with st.chat_message("assistant"):
            st.markdown(assistant_response)

    # ---------------------------------
    # End-chat dropdown (popover)
    # ---------------------------------
    if st.session_state.messages or st.session_state.conversation_started:
        appointment_dialog()