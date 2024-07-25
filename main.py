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
    


text= takeCommand() # This function returns the text after recongnising the voice. (Uses google api)
speak(text)# This function takes in the text and returns the voice. (Uses own voice system of the laptop)
        
    


      
