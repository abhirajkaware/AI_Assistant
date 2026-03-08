# Nexa AI Voice Assistant

Nexa is a Python based AI voice assistant that listens to voice commands and responds using text to speech. It uses speech recognition to understand the user and Google Gemini AI to generate answers.

## Features

- Wake word activation using "Hello Nexa"
- Speech recognition using microphone
- Text to speech responses
- AI responses using Google Gemini
- Opens websites like YouTube, Google, and GitHub
- Opens system applications like Notepad
- Tells the current time
- Tells jokes
- Saves conversation history to a text file

## Technologies Used

- Python
- SpeechRecognition
- pyttsx3
- Google Generative AI (Gemini)
- python-dotenv
- Webbrowser module

## Installation

1. Clone the repository

git clone https://github.com/yourusername/nexa-ai-assistant.git

2. Navigate to the project folder

cd nexa-ai-assistant

3. Install required libraries

pip install SpeechRecognition pyttsx3 python-dotenv google-generativeai pyaudio

## Setup API Key

Create a `.env` file in the project folder and add your Gemini API key.

gemini_api_key=your_api_key_here

## How to Run

Run the Python file:

python assistant.py

The assistant will start and wait for the wake word.

Say:

Hello Nexa

Then speak your command.

## Example Commands

- What is the time
- Open YouTube
- Open Google
- Open GitHub
- Open Notepad
- Tell me a joke
- What is artificial intelligence

## Project Structure

assistant.py  
history.txt  
.env  
README.md  

## Author

Abhiraj Kaware  
Diploma in Computer Engineering Student

## Future Improvements

- Add graphical user interface
- Add more voice commands
- Improve AI response handling
- Add more system controls
