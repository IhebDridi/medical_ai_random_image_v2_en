import streamlit as st
from tipi import calculate_scores
import json

def submit_survey():
    st.session_state["survey_completed"] = True
    st.session_state["tipi_scores"] = calculate_scores(st.session_state["survey"])
    st.session_state["page"] = "chat"

def survey():
    if "survey" not in st.session_state:
        st.session_state["survey"] = {}

    st.title("Umfrage")

    options_final = [
      "Strongly disagree",  "disagree", "Neutral",  "Agree", "Strongly agree"

             ]

    #st.subheader("Fragebogen", divider='gray')
    st.markdown("Please provide the following personal details.")
    

    with st.form(key="my_form"):
        st.markdown("Please enter your ID")
        uuid = st.text_input("ID", value=st.session_state["survey"].get("ID", ""))


        submit_button = st.form_submit_button("Submit")

    if submit_button:
        
        if uuid == "":
            st.error("Please enter your ID.")

        
        else:
            st.session_state['uuid']=uuid
            st.session_state["survey"]["uuid"] = uuid
            #st.session_state["survey"]["gender"] = gender
            #st.session_state["survey"]["skin_color"] = skin_color
            st.session_state["page"] = "chat"
            st.success("Thank you very much for your answers!")
            st.write("### Your selection:")
            st.session_state["page"] = "chat"
            print('Survey Data: ',st.session_state["survey"] )
            st.rerun()
