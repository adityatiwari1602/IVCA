import speech_recognition as sr #pip3 install speechRecognition
import pyttsx3
import GUI as gui
#pyttsx3 setup
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('en-in', voices[0].id)
white=gui.white            
def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        gui.message_display("Listening...")
        gui.sleep(2)
        gui.gameDisplay.fill(white)
        r.pause_threshold = 1
        #this is where the code breaks
        r.adjust_for_ambient_noise(source, duration=3)
        #print(r)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        gui.message_display("Recognizing...")
        gui.sleep(2)
        gui.gameDisplay.fill(white)
        query = r.recognize_google(audio)
        print("User said:" + query)
        gui.message_display("User said:" + query)
        gui.sleep(2)
        gui.gameDisplay.fill(white)

    except Exception as e:
        print(e)
        print("Say that again please...")
        gui.message_display("Say that again please...")
        speak("Say that again please...")
        gui.sleep(2)
        gui.gameDisplay.fill(white)
        return "None"
    return query
