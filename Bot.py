
import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr # pip install SpeechRecognition
import sys
import wikipedia # pip install wikipedia
import webbrowser as wb
import os
import psutil # pip install psutil
import pyjokes # pip insatll pyjokes

engine=pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
# Function to tell time
def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(time)
    
# Function to tell date
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)
    
# Function for greeting
def wishme():
    speak("Welcome back sir")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good Morning sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir")
    elif hour >=18 and hour<24:
        speak("Good Evening sir")
    else:
        speak("Good Night Sir")
    speak("Alexa at your service. Please tell me how can i help you")

# Function to take your commands
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language="en-in")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query

# Function for Cpu and Battery usage
def cpu():
    usage = str(psutil.cpu_percent())
    speak("cpu is at"+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent )

# Function for jokes
def jokes():
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)
   
# Main function
if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        
        if 'time' in query:
            time()
            
        elif 'date' in query:
            date()
            
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
            
        elif 'search in chrome' in query:
            speak("What should i search ?")
            chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
            
        elif 'logout' in query: # Logout function
            os.system("Shutdown -l")
            
        elif 'remember that' in query:
            speak("what should i remember?")
            data = takeCommand()
            speak("you said me to remember that"+data)
            remember = open('data.txt','w') # First create a empty data.txt file
            remember.write(data)
            remember.close()
            
        elif 'do you remember anything' in query:
            remember = open('data.txt','r')
            speak("you said to remember that" +remember.read())
            
        elif 'cpu' in query:
            cpu()
            
        elif 'joke' in query:
            jokes()
            
        elif 'offline' in query: # Function to terminate the program
            sys.exit()
            


        
        
        
        
        
        
        
        
        
        
        
        
        
        