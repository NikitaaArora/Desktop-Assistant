# __init__.py is the constructor file that you add in the folder to tell any operating system or cloud that it is a local package 
# such that when we write
# from source.helper import functionname [source.helper path is recognised.]


import speech_recognition as sr
import google.generativeai as genai #to use gemini model 
import os
from gtts import gTTS #text to speech conversion #saves the speech file as audio unlike pyttx3

GOOGLE_API_KEY = "AIzaSyDnPZKvu7ENB3wAaaEM21UkDm66FLaPdLM"
os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY #set the google_api_key as the environment variable. 


def voice_input():

    """This function converts voice to text
    """
    #Create a recogniser instance
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)

    try:
        text= r.recognise_google(audio)
        print("You said: ", text)
        return text
    
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio")

    except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


def text_to_speech(text):
     
    """This function converts text to speech
    """
     
    #create a gTTS object
    tts = gTTS(text=text, lang='en') #Language can be chnaged

    tts.save("speech.mp3")



def llm_model_object(user_text):
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(user_text)
    result = response.text

    return result