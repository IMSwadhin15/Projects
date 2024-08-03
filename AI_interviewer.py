import speech_recognition as sr
import os
import win32com.client

'''
chatStr = ""
def chat(querry):
    global chatStr      # declare charStr as global
    chatStr += querry
    print(f"chat:{chatStr}")
    speaker.Speak(querry)
'''

# take inputs as voice commands
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1  # time to wait
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")  # hi-in is hindi, but it cannot say hindi
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Sorry, Can you repeat please !"


# speaker to speak our inputs
speaker = win32com.client.Dispatch("SAPI.SpVoice")
# main

while 1:
    st = "Hallo Sir, which subject you want to get prepare \n\
    subjects code are\n\
        OS for operating systems \n\
        DBMS for database management"
    speaker.Speak(st)
    while True:
        print("Listening...")
        s = takecommand()

        if "thank you".lower() in s.lower():
            speaker.Speak("thank you sir")
            exit()

        elif "DBMS".lower() in s.lower():
            speaker.Speak("Certainly Sir")
            q1 = "here is the first question. what is dbms ?"
            speaker.Speak(q1)
# DBMS 1
        D1 = ["database management system","vaious operations on data","store data","queries on data"]
        for d1 in D1:
            if f"{d1}".lower() in s.lower():
                ans1 = "off course, It is Database Management Systems are software systems used to store, retrieve, and run queries on data. It is an interface between end user and database."
                speaker.Speak(ans1)
                
                q2 = "second question, what is the conceptual level of 3 level architecture."
                speaker.Speak(q2)
        
# DBMS 2
        D2 = ["logical level","relationship between entities and attributes", "logical structure","logical framework"]
        for d2 in D2:
            if f"{d2}".lower() in s.lower():
                ans2="Indeed, The conceptual level is also known as logical level, which represents the logical framework of the database."
                speaker.Speak(ans2)
                break
         
'''
        elif "OS".lower() in s.lower():
            speaker.Speak("Certainly Sir")
            # promt pass to the open ai api
            # response received and 
            q1 = "here is the first question. what is operating system and what are it's  important functions."
            speaker.Speak(q1)
'''
'''
        Os = ["maintain relation between software and hardware",
              "maintain relation between hardware and software",
              "manage computer hardware and software",
               "manage computer software and hardware",
               "manage resource",
               "resource management"]

        for O in Os:
            if f"{O}".lower() in s.lower():
                ans1 = f"great, indeed it {O}. An operating system is a software program that manages computer hardware and software resources and provides common services for computer programs.\n\
                important functions are\n\
                Process Management,\n\
                Memory Management,\n\
                File System Management"
                speaker.Speak(ans1)

                q2 = "second question, what is real time operating system"
                speaker.Speak(q2)

        rts = ["real time applications","real time computation", "strict time","specified deadline", "time specific", "specific time","time boundry" , "critical system"]
        for r in rts:
            if f"{r}".lower() in s.lower():
                ans2 = "Off course. A real-time operating system is an operating system designed complete task within a strict time interval"
                speaker.Speak(ans2)
'''

        
        # what in Speak, it speaks that
        # speaker.Speak(s)

'''
        if "swadhin".lower() in s.lower():
            speaker.Speak("good boy swadhin")

        elif "reset".lower() in s.lower():
            print("hi")
            chatStr = ""

        else:
            chat(s)
'''