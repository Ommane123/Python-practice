import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open linkedin" in c.lower():
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

if __name__ == "__main__":
    speak("Initializing Jarvis......")
    while True:
        # Listen for the "Jarvis" keyword
        # obtain audio from the microphone
        r = sr.Recognizer()
        

        print("recognizing...")
        # recognize speech using 
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "hello"):
                speak("yes sir, how may I help you?")
                # listen for command
                with sr.Microphone() as source:
                    print("Jarvis Activated...")
                    audio = r.listen(source)
                command = r.recognize_google(audio)

                processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))