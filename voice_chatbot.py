import speech_recognition as sr
import pyttsx3
from textblob import TextBlob

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    print("ChatBot:", text)
    engine.say(text)
    engine.runAndWait()

# Initializing the recognizer

recognizer = sr.Recognizer()

speak("Hello! I am your voice-enabled chatbot. Say something or say 'bye' to exit.")

while True:
    try:
        with sr.Microphone() as source:
            print("\nListening...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            user_input = recognizer.recognize_google(audio)
            user_input = user_input.lower()
            print("You:", user_input)

            if "bye" in user_input:
                speak("Goodbye! Have a great day.")
                break

            blob = TextBlob(user_input)
            polarity = blob.sentiment.polarity

            if "your name" in user_input:
                speak("I am VoiceBot, your Python chatbot.")
            elif "how are you" in user_input:
                speak("I'm doing great. Thanks for asking!")
            elif polarity > 0.3:
                speak("You sound happy! ")
            elif polarity < -0.3:
                speak("I'm here for you. Things will get better.")
            else:
                speak("Thanks for sharing. What else would you like to talk about?")

    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand that.")
    except sr.RequestError:
        speak("Sorry, there was an issue with the speech service.")
    except Exception as e:
        speak(f"Oops! Something went wrong: {str(e)}")
