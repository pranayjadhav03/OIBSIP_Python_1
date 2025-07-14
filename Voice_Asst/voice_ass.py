import pyttsx3
import datetime
import webbrowser
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty("rate", 150)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def mic_available():
    try:
        mics = sr.Microphone.list_microphone_names()
        return len(mics) > 0
    except:
        return False

def safe_exit():
    speak("Microphone is not available or not working properly.")
    speak("Please check your mic connection and try again.")
    exit()

if not mic_available():
    safe_exit()

recognizer = sr.Recognizer()

def listen():
    try:
        mic = sr.Microphone()
        with mic as source:
            print("🎤 Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)
            return command
    except Exception as e:
        speak("Mic failed during use. Exiting now.")
        print("Internal error:", e)
        exit()

def respond(command):
    if "hello" in command:
        speak("Hi, how can I help you?")
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")
    elif "date" in command:
        today = datetime.datetime.now().strftime("%A, %B %d")
        speak(f"Today is {today}")
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "search for" in command:
        query = command.replace("search for", "").strip()
        if query:
            speak(f"Searching for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            speak("What should I search for?")
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I don't know that command.")

speak("Voice Assistant is ready. Say something.")
while True:
    command = listen()
    respond(command)
