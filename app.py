
import requests
import streamlit as st

MODEL = "gemma3:1b"
OLLAMA_URL = "http://localhost:11434/api/generate"

st.set_page_config(
    page_title="StudyEase AI",
    page_icon="📚",
    layout="centered"
)

st.title("📚 StudyEase AI")
st.write("Turn long study notes into useful revision material.")

notes = st.text_area(
    "Paste your study notes here",
    height=220,
    placeholder="Paste a paragraph from your lecture notes..."
)

task = st.selectbox(
    "What do you want to create?",
    [
        "Short summary",
        "Key revision points",
        "Practice questions"
    ]
)

if st.button("Generate", type="primary"):
    if not notes.strip():
        st.warning("Please paste some study notes first.")
    else:
        prompt = f"""
You are StudyEase AI, a helpful study assistant.

Use only the study notes provided below.
Do not invent facts that are not in the notes.
If information is missing, say so.

Task: Create {task.lower()}.
Write in clear, simple language.
Keep the response organized and useful for revision.

Study notes:
{notes}
"""

        try:
            with st.spinner("The AI is working..."):
                response = requests.post(
                    OLLAMA_URL,
                    json={
                        "model": MODEL,
                        "prompt": prompt,
                        "stream": False
                    },
                    timeout=240
                )
                response.raise_for_status()
                result = response.json()["response"]

            st.subheader("Your study material")
            st.markdown(result)

        except requests.exceptions.ConnectionError:
            st.error(
                "Ollama is not running. Open Ollama and try again."
            )
        except requests.exceptions.Timeout:
            st.error(
                "The model took too long to respond. "
                "Try shorter notes."
            )
        except (requests.RequestException, KeyError, ValueError) as error:
            st.error(f"Could not generate the result: {error}")

st.caption(
    "AI-generated answers can contain mistakes. "
    "Check important facts against your original notes."
)
