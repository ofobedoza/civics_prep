import streamlit as st
import random
import pandas as pd

# Page title
st.title("Civics Test Reviewer")

# Load civics questions CSV
CIVIC_QUESTIONS = pd.read_csv("civics_questions.csv").to_dict(orient="records")

# Initialize session state
if "questions" not in st.session_state:
    st.session_state.questions = []
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
if "show_answer" not in st.session_state:
    st.session_state.show_answer = False

# Sidebar: number of questions
num_questions = st.sidebar.selectbox("Number of questions", [10, 20, 30, 50, 100])
def start_quiz():
    n = min(num_questions, len(CIVIC_QUESTIONS))
    st.session_state.questions = random.sample(CIVIC_QUESTIONS, n)
    st.session_state.current_index = 0
    st.session_state.show_answer = False
st.sidebar.button("Go", on_click=start_quiz)

# Stop if quiz not started
if not st.session_state.questions:
    st.write("Click 'Go' to start the quiz.")
    st.stop()

# Current question
idx = st.session_state.current_index
q = st.session_state.questions[idx]

# Progress bar
progress = (idx + 1) / len(st.session_state.questions)
st.progress(progress)
st.markdown(f"**Question {idx + 1} of {len(st.session_state.questions)}**")
st.write(q["question"])

# Show answer in highlighted box
if st.session_state.show_answer:
    st.markdown(
        f"""
        <div style="
            background-color: #fff2b3;
            padding: 15px;
            border-radius: 8px;
            border: 1px solid #ffd966;
            margin-bottom: 10px;
        ">
        <strong>Answer:</strong> {q['answer']}
        </div>
        """,
        unsafe_allow_html=True
    )

# Button callbacks
def show_answer():
    st.session_state.show_answer = True

def next_question():
    if st.session_state.current_index < len(st.session_state.questions) - 1:
        st.session_state.current_index += 1
        st.session_state.show_answer = False

def previous_question():
    if st.session_state.current_index > 0:
        st.session_state.current_index -= 1
        st.session_state.show_answer = False

# Three buttons: Previous, Show Answer, Next
col1, col2, col3 = st.columns(3)
with col1:
    st.button("Previous Question", on_click=previous_question, key=f"prev_{idx}")
with col2:
    st.button("Show Answer", on_click=show_answer, key=f"show_{idx}")
with col3:
    st.button("Next Question", on_click=next_question, key=f"next_{idx}")