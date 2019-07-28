import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import os
import smtplib
import fbchat



engine = pyttsx3.init('sapi5')

email_list = ['Shubhjain56854@gmail.com','Djain5888@gmail.com','Utkarsharvind@gmail.com','Siddhantsharma615@gmail.com','khantwalsukirti@gmail.com']

rate = engine.setProperty('rate',200)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe(audio):
    time = int(datetime.datetime.now().hour)
    if time>0 and time<12:
        speak("Good Morning Sir!")
    elif  time>12 and time<18:
        speak("Good After noon Sir!!")
    else:
        speak("Good Evening Sir!!")
    speak("Hi, I am Sukirti How can I help you??")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language = 'en-in')
        print("User said:" , query)
    except Exception as e:
        print("Can you say that again please..")
        return "None"
    return query
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("Siddhant.17504@sscbs.du.ac.in", '')
    server.sendmail("Siddhant.17504@sscbs.du.ac.in",to,content)
    server.close()
if __name__ == "__main__":
    wishMe(".")
    while 1:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching on wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open facebook" in query:
            webbrowser.open("facebook.com")
        elif "play music"  in query:
            music_dir = "D:\\siddhant e\\Songs2"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[2]))
        elif "send an email" in query:
            speak("Whom do you want to send")
            email_r = takeCommand().lower()
            try:
                if "shubh" in email_r:
                    to = email_list[0]
                elif "utkarsh" in email_r:
                    to = email_list[2]
                elif "deepak" in email_r:
                    to = email_list[1]
                elif "siddhant" in email_r:
                    to = email_list[3]
                elif "sukirti" in email_r:
                    to = email_list[4]
                speak("What should i send")
                content = takeCommand()
                speak("You want to send")
                speak(content)
                speak("To")
                speak(email_r)
                speak("You wanna send it or cancel it?")
                result = takeCommand().lower()
                if "send" in result:
                    sendEmail(to,content)
                    speak("Email sent succesfully!!")
                elif "cancel" in result:
                    speak("Ok!!")
                    break
            except Exception as e:
                print(e)
                speak("sorry brother i was unable to send the email")
        elif "How are you" in query:
            speak("I'm good sir")
        elif "send facebook message" in query:
            try:
                username = "siddhant.sharma.77920"
                password = ""
                client = fbchat.Client(username,password)
                speak("Whom do you want to send the message")
                mess_to = takeCommand().lower()
                if "sukirti" in mess_to:
                    message_to = "sukirti.khantwal"
                speak("What is the message")
                message = takeCommand()
                speak("You want to send")
                speak(message)
                speak("To")
                speak(mess_to)
                speak("You wanna send it or cancel it?")
                res = takeCommand().lower()
                if "send" in res:
                    sent = client.send(message_to,message)
                    if sent:
                        speak("Message sent successfully")
                elif "cancel" in res:
                    speak("Ok!!")
                    break
            except Exception as e:
                print(e)
                speak("Sorry i was unable to send the message!")



        



        
        elif "exit" in query:
            speak("Until next time , Bye!")
            break
            
       




