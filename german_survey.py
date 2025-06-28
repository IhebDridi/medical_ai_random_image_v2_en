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
      "Starke Ablehnung",  "Ablehnung", "Neutral",  "Zustimmung", "Starke Zustimmung"

             ]

    #st.subheader("Fragebogen", divider='gray')
    st.markdown("Bitte machen Sie die folgenden Angaben zu Ihrer Person.")
    

    with st.form(key="my_form"):
        st.markdown("Bitte geben Sie Ihre ID ein")
        uuid = st.text_input("ID", value=st.session_state["survey"].get("ID", ""))


        submit_button = st.form_submit_button("Absenden")

    if submit_button:
        
        if uuid == "":
            st.error("Bitte geben Sie Ihre ID ein.")

        
        else:
            st.session_state['uuid']=uuid
            st.session_state["survey"]["uuid"] = uuid
            #st.session_state["survey"]["gender"] = gender
            #st.session_state["survey"]["skin_color"] = skin_color
            st.session_state["page"] = "chat"
            st.success("Vielen Dank für Ihre Antworten!")
            st.write("### Ihre Auswahl:")
            st.session_state["page"] = "chat"
            print('Survey Data: ',st.session_state["survey"] )
            st.rerun()
