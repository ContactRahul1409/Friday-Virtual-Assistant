# FRIDAY VIRTUAL ASSISTANT

import speech_recognition as sr
import webbrowser
import pyttsx3
import random
import pywhatkit
import pyjokes
import cv2
import pyautogui
from datetime import datetime
from news import news_data
from weather import weather_data
import wikipedia

recognizer = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        command = recognizer.recognize_google(audio).lower()
        print("You said : ",command)
        return command


# Get the current date and time
now = datetime.now()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def image_capturing(ic):
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("webcam")
    img_counter = 0
    while True:
            ret,frame = cam.read()
            if not ret:
                print("failed to grab frame")
                break


    cam.release()
    cam.destroyAllWindows()


def game():
    while True:
        choices = ["rock", "paper", "scissors"]
        speak("What is your choice? Rock, paper, or scissors?")
        friday_choice = random.choice(choices)
        input_choice = listen()

        if input_choice not in choices:
            speak("Please say rock, paper, or scissors.")
            return

        print(f"Friday chose: {friday_choice}")

        if input_choice == friday_choice:
            speak("Tie")
        elif (input_choice == "rock" and friday_choice == "scissors") or \
         (input_choice == "paper" and friday_choice == "rock") or \
         (input_choice == "scissors" and friday_choice == "paper"):
            speak("You Won")
        else:
            speak("Yayy, I Won")
 


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    elif c.lower().endswith("friday"):
        name =  "FRIDAY is basically Female Replacement Intelligent Digital Assistant Youth, I am a virtual assistant named friday skilled in general conversations and tasks like alexa and google assistant"
        speak(name)       
    elif "joke" in c.lower():
        joke = pyjokes.get_joke() 
        speak(joke)    
    elif "play" in c.lower():
        song = c.replace('play', '')
        speak('playing' + song)
        pywhatkit.playonyt(song)
    elif "screenshot" in c.lower():
        ss = pyautogui.hotkey('printscreen')
        speak("sure")
        print(ss)    
    elif "open webcam" in c.lower():
        speak("Sure")
        camera = image_capturing(command)
        print(camera)
    elif "game" in c.lower():
        game()
    elif "date today" in c.lower():
        date = now.strftime("'day'%d-'month'%m-'year'%Y")
        speak(f"Date: {date}")
    elif "time" in c.lower():
        time = now.strftime("%H'hours':%M'minutes':%S'seconds'")
        speak(f"Time: {time}")
    elif "news" in c.lower():
        for article in news_data['articles']:
            speak(article['title'])
    elif "weather" in c.lower():
        speak(f"Location: {weather_data['location']['name']}, {weather_data['location']['country']}")
        speak(f"Temperature: {weather_data['current']['temp_c']}°C")
        speak(f"Condition: {weather_data['current']['condition']['text']}")        
    else:
        results = wikipedia.summary(c.lower(), sentences=2)
        speak(results)


if __name__ == "__main__":
    speak("Initializing Friday...")
    while True:
        # Listen wake up word "friday"
        r = sr.Recognizer()
        print("recognizing...")    
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
            word = r.recognize_google(audio, language='en-in')
            options = ["Hi, how can I help you today?","What can I do for you?","Hello! What would you like to know?"]
            if(word.lower() == "friday"):
                speak(random.choice(options))
                with sr.Microphone() as source:
                    print("Friday Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio, language='en-in')

            print(command + "?")    #Ensuring the command
            processCommand(command)
        except sr.UnknownValueError:
            print("Friday could not understand your command")

        except Exception as e:
            print("Error; {0}".format(e))
        
        