#Main code file with all the code which is further divided into helper.py and app.py


import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os


'''Main Functionalities of Desktop Assistant:

    #Speech recognition - speech to text
    #Speakfunction - text to speech

'''

''' SPEAK FUNCTION: Given a text we need to use our system's voice to convert that into voice. '''

# Taking the voice from my system 

engine = pyttsx3.init('sapi5') #To access any voice property in the system #voice engine
voices = engine.getProperty('voices')

# print(voices[1].id) #getting the first proprty
# print(type(voices)) #Its a list


engine.setProperty('voice',voices[0].id) #It tells python interpreter to take the male voice from the system.
engine.setProperty('rate', 200) #if rate property needs to be changed then this needs to be executed. 
#engine.setProperty('voice', voices[1].id) #female voice


# Speak function
def speak(text):
    """This function takes text and returns voice

    Args: 
        text(_type_): string
    
    """
    engine.say(text)
    engine.runAndWait() #after the voice is spoken close the object

#speak("Hello, I am a programmer. How are you?")



'''SPEECH RECOGNITION: VOICE TO TEXT'''

def takeCommand():
    """This function will recognise voice and returns text
    """
    r = sr.Recognizer()
    with sr.Microphone() as source: #To access my microphone successfully.
        print("Listening...")
        r.pause_threshold = 1 
        audio= r.listen(source) #activate listening using google api and getting this audio frequency. 
        #using try-except block as it will hit the google-api.
        try:
            print("Recognising...")
            query= r.recognize_google(audio, language= 'en-in')#indian english
            print(f"User said: {query}\n")

        except Exception as e:
            print("Say that again, pls....")
            return "None"
        
        return query
    



def wish_me():
    """This function greets the user according to the time of the day.
    """
    hour = datetime.datetime.now().hour
    if hour >=0 and hour <12:
        speak('Good morning.')
    elif hour>=12 and hour<18:
        speak('Good afternoon')
    else:
        speak('Good evening')

    speak("ahhhh I am jarvis. Tell me how can I help")


    

# text= takeCommand() # This function returns the text after recongnising the voice. (Uses google api)
# speak(text)# This function takes in the text and returns the voice. (Uses own voice system of the laptop)

 #Use this when a lot of functions are written in a particular code file. 
 #It helps in segregating the logic(that is functions logic) from the calling of fucntions


if __name__ == '__main__':     

    wish_me()        
    print("Welcome to the speech regognition")
    
    while True:  #This is required for continuous to-and-fro of questions and answers. 
    
        query= takeCommand().lower()  #instead of calling the function outside, we can call this function inside this construct. 
        print(query)                  # Convert all in lower characters. 
        
        if "wikipedia" in query:
            print("YES")
            speak("Searching wikipedia")
            query = query.replace('wikipedia',"")
            print(query)
            result= wikipedia.summary(query, sentences=2) #asking only 2 senetence summary.
            speak("Acc to wikipedia")
            print(result)
            speak(result)

        elif "youtube" in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com") #by default it opens edge browser. 

        elif "google" in query:
            speak("Opening google")
            webbrowser.open("google.com")

        elif "github" in query:
            speak("Opening github")
            webbrowser.open("github.com")

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'goodbye' in query:
            speak('ok. I am always here for you. Bye')
            exit() #This is used for exiting in python.The prgram gets terminated. 

    









        
    


      
