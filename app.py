import streamlit as st
import random
import pandas as pd

# ---------- Page config ----------
st.set_page_config(page_title="US Civics Test Flashcards", layout="centered")

# ---------- CSS Styling ----------
st.markdown("""
<style>
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

.flashcard {
    background-color: var(--secondary-background-color);
    padding: 25px;
    border-radius: 16px;
    border: 1px solid #adb5bd;
    font-size: 22px;
    line-height: 1.5;
    text-align: center;
    user-select: none;
    cursor: pointer;
    min-height: 160px;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    max-width: 600px;
}

.answerbox {
    background-color: var(--secondary-background-color);
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #dee2e6;
    font-size: 20px;
    margin: 0 0 1rem 0;
    color: var(--text-color);
}

.stButton button {
    font-size: 22px;
    height: 60px;
    border-radius: 16px;
    border: 1px solid #adb5bd;
    background-color: var(--secondary-background-color);
}

/* fix width only for the flashcard button itself by selecting the
   first stButton container directly under the page block.  navigation
   buttons live inside column divs and thus aren't matched. */
.block-container > .stButton:first-of-type button {
    display: block;
    width: 600px;
    max-width: 600px;
    margin: 0 auto;
}
</style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.title("US Civics Test Flashcards")

# ---------- Load questions ----------
CIVIC_QUESTIONS = pd.read_csv("civics_questions.csv").to_dict(orient="records")

# ---------- Session state ----------
if "questions" not in st.session_state:
    st.session_state.questions = []

if "current_index" not in st.session_state:
    st.session_state.current_index = 0

if "show_answer" not in st.session_state:
    st.session_state.show_answer = False

if "num_questions" not in st.session_state:
    st.session_state.num_questions = 20

if "quiz_setup" not in st.session_state:
    st.session_state.quiz_setup = True

# ---------- Functions ----------
def start_quiz():
    num_q = st.session_state.get("num_questions", 20)
    n = min(num_q, len(CIVIC_QUESTIONS))
    st.session_state.questions = random.sample(CIVIC_QUESTIONS, n)
    st.session_state.current_index = 0
    st.session_state.show_answer = False
    st.session_state.quiz_setup = False

def new_quiz():
    st.session_state.quiz_setup = True
    st.session_state.questions = []
    st.session_state.show_answer = False
    st.session_state.current_index = 0

def next_question():
    if st.session_state.current_index < len(st.session_state.questions) - 1:
        st.session_state.current_index += 1
        st.session_state.show_answer = False

def previous_question():
    if st.session_state.current_index > 0:
        st.session_state.current_index -= 1
        st.session_state.show_answer = False

def reveal_answer():
    st.session_state.show_answer = not st.session_state.show_answer

# ---------- Quiz setup screen ----------
if st.session_state.quiz_setup:
    st.subheader("Start a New Quiz")
    st.selectbox(
        "Number of questions",
        [10, 20, 30, 50, 100],
        key="num_questions"
    )
    st.button("Start Quiz", on_click=start_quiz)
    st.stop()

# ---------- Current question ----------
idx = st.session_state.current_index
q = st.session_state.questions[idx]

# ---------- Progress ----------
progress = (idx + 1) / len(st.session_state.questions)
st.progress(progress)
st.caption(f"Question {idx + 1} of {len(st.session_state.questions)}")

# ---------- Tap hint ----------
st.info("💡 Tap the question to reveal the answer.")

# ---------- Flashcard ----------
if st.button(q["question"], key=f"card_{idx}"):
    reveal_answer()

# ---------- Show answer ----------
if st.session_state.show_answer:
    st.markdown(
        f"""
        <div class="answerbox">
        <strong>Answer:</strong><br>{q['answer']}
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------- Navigation buttons ----------
col1, col2 = st.columns(2)
with col1:
    st.button("⬅️ Previous", key=f"prev_{idx}", on_click=previous_question, use_container_width=True)
with col2:
    st.button("Next ➡️", key=f"next_{idx}", on_click=next_question, use_container_width=True)

# ---------- New Quiz ----------
st.divider()
st.button("🔄 New Quiz", on_click=new_quiz)