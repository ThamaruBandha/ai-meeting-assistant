import os
from dotenv import load_dotenv
import assemblyai as aai

load_dotenv()

# Set your AssemblyAI key for this session
aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")

# Create a "transcriber" — our tool for sending audio off to be converted to text
transcriber = aai.Transcriber()

# The actual request: "here's an audio file, please transcribe it"
# This uploads the file, waits for processing, and returns the text
transcript = transcriber.transcribe("test_audio.mp4")

print("----- TRANSCRIPT -----")
print(transcript.text)

# Save it to a file so Step 6 can read it
with open("transcript_output.txt", "w") as f:
    f.write(transcript.text)

print("\nSaved to transcript_output.txt")