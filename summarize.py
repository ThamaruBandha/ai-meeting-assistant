import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Read the transcript we saved in Step 5
with open("transcript_output.txt", "r") as f:
    transcript_text = f.read()

# This is the actual "prompt" — the instruction telling the AI exactly
# how to summarize. Being specific here makes the output far more useful.
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

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    max_tokens=500,
    messages=[{"role": "user", "content": prompt}]
)

summary = response.choices[0].message.content

print("----- SUMMARY -----")
print(summary)

# Save it so we can use it later in our web interface
with open("summary_output.txt", "w") as f:
    f.write(summary)

print("\nSaved to summary_output.txt")