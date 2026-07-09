import os
from dotenv import load_dotenv
import assemblyai as aai
from groq import Groq

load_dotenv()

aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def transcribe_audio(filepath):
    """Takes an audio file path, returns the transcribed text."""
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(filepath)
    return transcript.text

def summarize_transcript(transcript_text):
    """Takes transcript text, returns a structured summary."""
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

# ---- Main flow ----
if __name__ == "__main__":
    audio_file = "test_audio.mp4"

    print("Transcribing...")
    transcript = transcribe_audio(audio_file)
    with open("transcript_output.txt", "w") as f:
        f.write(transcript)
    print("Transcript saved.\n")

    print("Summarizing...")
    summary = summarize_transcript(transcript)
    with open("summary_output.txt", "w") as f:
        f.write(summary)

    print("----- FINAL SUMMARY -----")
    print(summary)