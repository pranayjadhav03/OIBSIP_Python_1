# OIBSIP Python Task 1: Voice Assistant 🗣️

## 🔍 Objective
To create a basic Python-based voice assistant that responds to voice commands such as telling the time/date, opening Google, or saying hello.

## 📋 Steps Performed
- Used microphone input (with error handling fallback)
- Converted voice to text using Google’s speech API
- Recognized simple commands like:
  - “Hello”
  - “What’s the time?”
  - “Open Google”
- Gave responses using `pyttsx3` text-to-speech
- Included graceful fallback if mic is unavailable

## 🧰 Tools & Technologies
- Python 3.x
- `speech_recognition`
- `pyttsx3` (TTS)
- `webbrowser`, `datetime`
- Error handling with `try-except`

## ✅ Outcome
A working voice assistant that:
- Listens to user commands
- Responds via voice
- Opens websites
- Exits cleanly
