# voice_chatbot-using-python
I have created a voice chatbot using python and i am interested in this Artificial intelligence field.


This project is a simple Python-based voice chatbot that accepts voice input, analyzes the sentiment of the message using natural language processing (TextBlob), and responds using text-to-speech. It demonstrates the integration of speech recognition, NLP, and audio output — all useful skills in AI and chatbot development.

## Features

Accepts voice input from the user
Uses sentiment analysis (TextBlob) to understand mood
Responds via synthesized voice using pyttsx3
Basic rule-based conversational replies
Graceful error handling for unknown input or system errors

## Technologies Used

Python
SpeechRecognition
TextBlob (NLP)
Pyttsx3 (Text-to-Speech)
PyAudio (for microphone access)

## Installation

Install dependencies:

pip install -r requirements.txt

If TextBlob for the first time, also run:

python -m textblob.download_corpora

If `pyaudio` fails to install on Windows, try:

pip install pipwin
pipwin install pyaudio


## Usage

After installing dependencies, run the chatbot.

