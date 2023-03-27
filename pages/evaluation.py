import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

# HACK: This is to get rid of the sidebar
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)

with st.form("evaluation_form", clear_on_submit=True):
    # Parse our CSV file
    # TODO: Get this from a more reliable datasource
    df = pd.read_csv("evaluation.csv")
    # Get the questions, their choices and their correct answers
    questions = df["question"].tolist()
    choices = df["choices"].tolist()
    correct_answers = df["correct answer"].tolist()
    user_quiz_answers = []

    # Enumarate the questions and choices
    for i, (question, choice) in enumerate(zip(questions, choices)):
        # Then generate a radio button for each question
        user_answers = st.radio(question, choice, key=i)
        user_quiz_answers.append(user_answers)

    # Check if the user's answers are correct
    if st.form_submit_button("Submit"):
        evaluated_correct_answers = 0
        # Enumarate the user's answers and the correct answers
        for user_answer, correct_answer in zip(user_quiz_answers, correct_answers):
            # If the users' correct answer is the same as the correct answer, pass them
            if user_answer == correct_answer:
                evaluated_correct_answers += 1

        # If the user got all the answers correct, pass them
        if evaluated_correct_answers == len(correct_answers):
            st.success("You passed the evaluation! You can now register for the tournament.")
            switch_page("register")
        else:
            st.error("You did not pass the evaluation. Please try again.")
