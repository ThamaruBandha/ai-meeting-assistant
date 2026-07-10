# 🎙️ AI Meeting Assistant

An AI-powered web app that transcribes meeting recordings and generates structured summaries — including key decisions, action items, and open questions — in seconds.

**🔗 Live demo:** https://ai-meeting-assistant-vgeexwmwmthyqhuz87hs8d.streamlit.app/ 
## What it does
- Upload an audio recording (or record live in-browser)
- Get an accurate transcript powered by AssemblyAI's speech-to-text model
- Get a structured AI summary powered by Llama 3.3 (via Groq) — summary, key decisions, action items, and open questions
- Download both the transcript and summary as text files

## Why I built this
As a first-year CS/AI/Business student, I wanted a real, end-to-end AI project — not just a tutorial clone — to understand how modern AI tools like Otter.ai or Fireflies are actually built under the hood: audio capture → speech-to-text → LLM summarization, glued together into one working product.

## Tech stack
- **Python** — core logic
- **Streamlit** — web interface
- **AssemblyAI API** — speech-to-text transcription
- **Groq API (Llama 3.3 70B)** — AI summarization
- **Streamlit Community Cloud** — deployment

## How it works
1. User uploads an audio file or records live via microphone in the browser
2. Audio is sent to AssemblyAI's API, which returns a text transcript
3. The transcript is sent to Llama 3.3 (via Groq) with a structured prompt, returning a formatted summary
4. Results are displayed in the browser with download options

## Run it locally
```bash
git clone https://github.com/YOUR-USERNAME/ai-meeting-assistant.git
cd ai-meeting-assistant
python -m venv venv
venv\Scripts\activate        # Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
```
Create a `.env` file with:
```
ASSEMBLYAI_API_KEY=your_key_here
GROQ_API_KEY=your_key_here

```
Then run:
```bash
streamlit run app.py
```

## Roadmap / what's next
- [ ] Chrome extension to auto-capture live captions from Google Meet/Zoom (Tactiq-style, no bot required)
- [ ] Ask-a-question feature — chat with a past meeting's transcript
- [ ] Multi-meeting memory across sessions

## Author
Built by Thamaru Bandha | bandhathamaru@gmail.com | www.linkedin.com/in/thamaru-b-875a9230b |
