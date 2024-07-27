from src.helper import voice_input,text_to_speech,llm_model_object
import wikipedia
import webbrowser
import os
import datetime
import streamlit as st



def main():
    st.title("Multilingual AI Assistant")

    if st.button("Ask me anything!"):
        with st.spinner("Listening..."):
            text= voice_input()
            response = llm_model_object(text)







# if __name__ == '__main__':     

#     wish_me()        
#     print("Welcome to the speech regognition")
    
#     while True:  #This is required for continuous to-and-fro of questions and answers. 

#         st.title("Desktop Assistant System")
    
#         query= takeCommand().lower()  #instead of calling the function outside, we can call this function inside this construct. 
#         print(query)                  # Convert all in lower characters. 
        
#         if "wikipedia" in query:
#             print("YES")
#             speak("Searching wikipedia")
#             query = query.replace('wikipedia',"")
#             print(query)
#             result= wikipedia.summary(query, sentences=2) #asking only 2 senetence summary.
#             speak("Acc to wikipedia")
#             print(result)
#             speak(result)

#         elif "youtube" in query:
#             speak("Opening Youtube")
#             webbrowser.open("youtube.com") #by default it opens edge browser. 

#         elif "google" in query:
#             speak("Opening google")
#             webbrowser.open("google.com")

#         elif "github" in query:
#             speak("Opening github")
#             webbrowser.open("github.com")

#         elif "time" in query:
#             strTime = datetime.datetime.now().strftime("%H:%M:%S")
#             speak(f"The time is {strTime}")

#         elif 'goodbye' in query:
#             speak('ok. I am always here for you. Bye')
#             exit() #This is used for exiting in python.The prgram gets terminated. 

    

