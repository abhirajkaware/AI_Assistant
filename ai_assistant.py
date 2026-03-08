import speech_recognition as sr
import datetime
import webbrowser
import os
import google.generativeai as genai
from dotenv import load_dotenv
import pyttsx3

instruction = """
Give very short answers in plain text.
Do not use symbols, stars, bullet points, or formatting.
"""

load_dotenv()
genai.configure(api_key=os.getenv('gemini_api_key'))
model = genai.GenerativeModel("gemini-2.5-flash", system_instruction=instruction)




def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 185)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    print("Nexa:", text)
    engine.say(text)
    engine.runAndWait()


def save_history(user, assistant):
    with open("history.txt", "a", encoding="utf-8") as f:
        f.write(f"You: {user}\n")
        f.write(f"Nexa: {assistant}\n")
        f.write("-" * 40 + "\n")


def wait_for_wake_word():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Waiting for wake word 'Nexa'...")
        r.adjust_for_ambient_noise(source)

        while True:
            audio = r.listen(source)

            try:
                text = r.recognize_google(audio, language='en-in').lower()
                if "hello nexa" in text:
                    speak("Yes Abhiraj")
                    return
            except:
                pass


def take_command():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio, language='en-in')
        print("You:", command)
        return command.lower()

    except:
        speak("Sorry, I didn't understand.")
        return "none"


def wish():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning Abhiraj. I am Nexa.")
    elif hour < 18:
        speak("Good Afternoon Abhiraj. I am Nexa.")
    else:
        speak("Good Evening Abhiraj. I am Nexa.")


wish()
wait_for_wake_word()

while True:

    command = take_command()

    if command == "none":
        continue

    if "exit" in command or "stop" in command:
        speak("Goodbye Abhiraj")
        save_history(command, "Goodbye")
        break

    elif "time" in command:
        time_now = datetime.datetime.now().strftime("%H:%M")
        response = f"The time is {time_now}"
        speak(response)
        save_history(command, response)

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        response = "Opening YouTube"
        speak(response)
        save_history(command, response)

    elif "open google" in command:
        webbrowser.open("https://google.com")
        response = "Opening Google"
        speak(response)
        save_history(command, response)

    elif "open github" in command:
        webbrowser.open("https://github.com")
        response = "Opening GitHub"
        speak(response)
        save_history(command, response)

    elif "open notepad" in command:
        os.system("notepad")
        response = "Opening Notepad"
        speak(response)
        save_history(command, response)

    elif "joke" in command:
        response = "Why do programmers prefer dark mode? Because light attracts bugs."
        speak(response)
        save_history(command, response)
    elif "name" in command:
        response = "My name is Nexa, your AI assistant."
        speak(response)
        save_history(command, response)
    else:
        try:
            response = model.generate_content(command).text
        except:
            response = "I cannot access AI right now"

        speak(response)
        save_history(command, response)
        