import streamlit as st
import os
from dotenv import load_dotenv
import assemblyai as aai
from groq import Groq

load_dotenv()
aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="AI Meeting Assistant", page_icon="🎙️", layout="centered")

def transcribe_audio(filepath):
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(filepath)
    return transcript.text

def summarize_transcript(transcript_text):
    prompt = f"""You are a helpful meeting assistant. Read the transcript below carefully and produce a structured summary.

Format your response EXACTLY like this:

## Summary
(3-4 sentences capturing what the meeting was about and its outcome)

## Key Decisions
(Bullet list. If no explicit decisions were made, write "No formal decisions — status update only.")

## Action Items
(Bullet list in the format: "- [Owner if known]: Task". If no owner is mentioned, write "- Unassigned: Task")

## Open Questions
(Anything left unresolved or that needs follow-up — infer this even if not explicitly stated, based on what's incomplete)

Transcript:
{transcript_text}
"""
    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# ---------- WEBSITE STARTS HERE ----------

st.title("🎙️ AI Meeting Assistant")
st.write("Upload a meeting recording and get an instant transcript + summary.")

# This creates a real file upload button on the webpage
uploaded_file = st.file_uploader("Upload your audio file", type=["mp3", "wav", "m4a", "mp4"])

# This creates a button; the code below only runs when it's clicked
if uploaded_file is not None:
    if st.button("Generate Summary"):
        # Save the uploaded file temporarily so AssemblyAI can read it
        # Save the uploaded file temporarily, keeping its original extension
        file_extension = uploaded_file.name.split(".")[-1]
        temp_filename = f"temp_audio.{file_extension}"
        with open(temp_filename, "wb") as f:
            f.write(uploaded_file.getbuffer())

        with st.spinner("Transcribing... this may take a moment"):
            transcript = transcribe_audio(temp_filename)

        with st.spinner("Summarizing..."):
            summary = summarize_transcript(transcript)
        
        st.subheader("📝 Summary")
        st.markdown(summary)

        st.subheader("📄 Full Transcript")
        st.text_area("Transcript", transcript, height=250, key="transcript_display")

        st.download_button("Download Summary", summary, file_name="meeting_summary.txt")
        st.download_button("Download Transcript", transcript, file_name="meeting_transcript.txt")

    
