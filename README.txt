US Civics Test Flashcards
=========================

This is a simple Streamlit application that presents flashcards with US civics
questions and answers. Users can configure the number of questions in a quiz,
navigate through them, and reveal answers by tapping/clicking the card.

Requirements
------------

- Python 3.8+ (tested with 3.11)
- streamlit
- pandas

Install dependencies via:

```
pip install -r requirements.txt
```

Usage
-----

1. Clone the repository and navigate to the project folder.
2. Ensure the virtual environment is activated (optional but recommended):

   ```powershell
   .venv\Scripts\activate
   ```

3. Start the app:

   ```bash
   streamlit run app.py
   ```

4. In your browser, select the desired number of questions and click "Start
   Quiz". Tap the flashcard to reveal the answer and use the navigation
   buttons to move between questions. Click "New Quiz" to restart.

Data
----

Questions are loaded from `civics_questions.csv`. Each row should contain
`question` and `answer` fields.

Styling
-------

Custom CSS is injected via `st.markdown` at the top of `app.py`; it ensures
consistent theming and fixed widths for the flashcard and answer box.

Git
---

Commit your changes with your configured user name/email. Authentication for
pushes is handled by Git (SSH keys or credential helpers), not during commit.


