import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
      speak("Good Morning! Abhishek")
    elif(hour>=12 and hour<18):
      speak("Good Afternoon! Abhishek")
    else:
      speak("Good Evening! Abhishek")
    speak("Hi!I am AKM Your Personal Assistent Please tell me how I may help you")



def takecommand():
      # take microphone input from the user and return string output...
      r=sr.Recognizer()
      with sr.Microphone() as source:
            print("Listening...........")
            r.pause_threshold=1
            audio=r.listen(source)
      try:
            print("Recognizing....")
            query=r.recognize_google(audio,language="en-in")
            print(f"user said:",(query),"\n")
      except Exception as e:
            speak("Say that again Please.....")
            return "None"
      return query

def sendEmail():
      server=smtplib.SMTP("smtp.gmail.com",587)
      server.ehlo()
      server.starttls()
      server.login("mishraabhi8924","1712010006")
      server.sentmail("mishraabhi8924",to,content)
      server.close()


if __name__=="__main__":                                                      
      wishMe()
      query=takecommand().lower()
      if "hi" in query:
            query=takecommand().lower()
            if "wikipedia" in query:
                    speak("Searching wikipedia Please wait")
                    query=query.replace("wikipedia","")
                    results=wikipedia.summary(query,sentences=3)
                    speak("According to wikipedia")
                    print(results)
                    speak(results)
                           

            elif "open youtube" in query:
                    webbrowser.open("youtube.com")

            elif "open google" in query:
                    webbrowser.open("google.com")
                            

            elif "open stackoverflow" in query:
                    webbrowser.open("stackoverflow.com")

            elif ("play music" or "play a song") in query:
                    music_dir="E:\\gajal\\New folder"
                    songs=os.listdir(music_dir)
                    print(songs)
                    ak=random.randint(0,len(songs))
                    os.startfile(os.path.join(music_dir,songs[ak]))
            elif "the time" in query:
                    strTime= datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f" Sir!The time is (strTime)")
                    

            elif "open code" in query:
                    speak("Please wait sir")
                    codePath="C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python37\\python.exe"
                    os.startfile(codePath)
                            

            elif "email to Abhishek" in query:
                    try:
                            speak("what should I say?")
                            content=takecommand()
                            to="mishraabhi8924@gmail.com"
                            sendEmail(to,content)
                            speak("Email successfully has been sent sir...")
                                
                    except Exception as e:
                            print(e)
                            speak("sorry sir I am not able to sent this email right now Please try after some time...")





