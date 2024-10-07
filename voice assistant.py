
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Sky Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open netflix' in query:
            webbrowser.open("netflix.com")

        elif 'open amazon' in query:
            webbrowser.open("amazon.com")

        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")

        elif 'open microsoft' in query:
            webbrowser.open("microsoft.com")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'open maps' in query:
            webbrowser.open("maps.google.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open twitter' in query:
            webbrowser.open("twitter.com")

        elif 'open microsoft office' in query:
            webbrowser.open("office.com")

        elif 'open apple' in query:
            webbrowser.open("apple.com")

        elif 'open prime video' in query:
            webbrowser.open("primevideo.com")

        elif 'open spotify' in query:
            webbrowser.open("spotify.com")

        elif 'open gaana' in query:
            webbrowser.open("gaana.com")

        elif 'open sbi' in query:
            webbrowser.open("onlinesbi.com")

        elif 'open hotstar' in query:
            webbrowser.open("hotstar.com")

        elif 'open outlook' in query:
            webbrowser.open("outlook.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open calculator' in query:
            webbrowser.open("calculator.net")

        elif 'open excel' in query:
            webbrowser.open("office.live.com/start/Excel.aspx?auth=2")


        elif 'play music' in query:
            music_dir = 'D:\\song'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")