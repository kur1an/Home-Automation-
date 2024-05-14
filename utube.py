import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import smtplib
import psutil
import time
import nltk
import random
import tkinter
from tkinter import *
from parse import *
from math import factorial


root = tkinter.Tk()

def hello ():
    global mike
    top= tkinter.Toplevel()
    top.title("Voice Recorder")
    top.geometry('1366x716')
    top.configure(background='#D0312d')
    mylabel = tkinter.Label(top, text="Click on Microphone to Ask your Query", font=("Arial ",10))
    mylabel.place(x=560,y=350)
    mike = tkinter.PhotoImage(file="C:\\Users\\Admin\\Desktop\\Microphone.png")
    image_label= tkinter.Label(top,image= mike)
    button_3= tkinter.Button (top ,image=mike,command=lambda:[main()],borderwidth=3)
    button_3.pack(pady=150)
    button_4= tkinter.Button (top ,text = 'Exit',font=("Arial Bold",13),command=top.destroy)
    button_4.pack(pady=20)

def hide ():
    root.withdraw()

Image = tkinter.PhotoImage(file="C:\\Users\\Ami\\Desktop\\welcome.png")
labelphoto = tkinter.Label (root , image= Image)
labelphoto.place(x=535,y=194)
root.configure(background='#856ff8')  
root.title("Welcome")
mylabel = tkinter.Label(root, text="Welcome to Chatbot", font=("Arial Bold",20))
mylabel.place(x=530,y=100)
mylabel = tkinter.Label(root, text="Developed By Mayank, Rayvanth & Steve", font=("Arial Bold",12))
root.geometry('1366x716')
mylabel.place(x=520,y=550)

button= tkinter.Button (root ,text = 'Exit',font=("Arial Bold",11),command=root.destroy)
button.place (x=700 ,y=480)

button_1= tkinter.Button (root ,text = 'Enter',font=("Arial Bold",11),command=lambda:[hello(),hide()])
button_1.place (x=600 ,y=480)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def delay():
    delay=input("to continue press enter: ")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am orchestra and i am here to help you ")
    feeling = speak("How are you today? ")
    feeling = input("How are you today? ")
    time.sleep(2)

    if "good" in feeling.lower() or "fine" in feeling.lower():
        print("I'm feeling good too!")
        speak("I'm feeling good too!")
        
    elif "great" in feeling.lower():
        print("I'm feeling awesome too!")
        speak("I'm feeling awesome too!")
    
    else:
        print("I'm sorry to hear that. What can I do to cheer you up?")
        speak("I'm sorry to hear that. What can I do to cheer you up?")
        time.sleep(5)
 
    favcolour = speak("What is your favourite colour? ")
    favcolour = input("What is your favourite colour? ")
    time.sleep(3)
    speak("My favourite colour is red")
    print("My favourite colour is red")

def stop():
    if 'stop listening' in query:
        a,b=0,0
        print("Stopped Listening")
        speak("Stopped Listening")
        delay()
        qr=takeCommand().lower()       
        if 'start listening' in qr:
            a,b=1,2

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("How can I help you?")
        speak('How can I help you?')
        print("Listening ...")
        speak('Listening ')       
        r.adjust_for_ambient_noise(source)

        try:
            audio = r.listen(source,timeout=10)
            
        except sr.UnknownValueError:
            exec()
            
    try:
        speak("Recognizing...")
        print("Recognizing...")    
        query = r.recognize_google(audio,language='en-in')
        query=query.lower()
        print("User said: \n",query)      

    except Exception as e:
        print("could you repeat that")
        speak("could you repeat that")
        return "None"
        
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('helloworld1213141@gmail.com', 'pythonisgood')
    server.sendmail('helloworld1213141@gmail.com', to, content)
    server.close()

def calculate1():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
        

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('You have not typed a valid operator, please run the program again.')
    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO. ''')

    if calc_again.upper() == 'Y':
        calculate1()

    elif calc_again.upper() == 'N':
        print('See you later.')

    else:
        again()

def main():
    a,b=1,2

    if a+b==3:
        wishMe()

        while a+b==3:
            query = takeCommand().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
                delay()

            elif 'open youtube' in query:
               webbrowser.open("youtube.com")
               delay()

            elif 'open google' in query:
                webbrowser.open("google.com")
                delay()

            elif 'open gmail' in query:
                webbrowser.open("https://gmail.com/")
                delay()

            elif 'discord' in query:
                webbrowser.open('discord.com')
                delay()

            elif 'adventure quest' in query:
                webbrowser.open('aq.com')
                delay()

            elif 'play music' in query:
                music_dir = 'C:\\Users\\5548-INS-0746\\Desktop\\amvs'
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))
                delay()

            elif 'tell me the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")
                print(f"Sir, the time is {strTime}")
                delay()

            elif 'open code' in query:
                codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
                delay()

            elif 'email to self' in query:

                try:
                    speak("What should I tell him?")
                    content = takeCommand()
                    to = "steve.joseph04@gmail.com"    
                    sendEmail(to, content)
                    speak("Email has been sent!")

                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")

            elif 'make a note' in query:
                print('making notes')
                speak('making notes')
                nfile=open('note.txt','a+')
                que=''
                while que != 'stop making notes':
                    que=takeCommand()
                    no=que
                    nfile.write(no)
                    nfile.write('/n')
                speak('stoping making notes')
                delay()

            elif 'show my notes' in query:
                nfile=open('note.txt','r')
                nf=nfile.readlines()
                print(nf)
                delay()

            elif 'reset my notes' in query:
                speak('are you sure')
                que=takeCommand()

                if que== 'yes':
                    que=takeCommand()
                    while que != 'stop making notes':
                        nfile=open('note.txt','w+')
                        nop=que
                        nfile.write(nop)
                        nfile.write('/n')                    
                else:
                    speak('notes not reset')
                delay()   

            elif 'battery' in query :
                battery = psutil.sensors_battery()
                plugged = battery.power_plugged
                percent = str(battery.percent)

                if plugged==False:
                    plugged="Not Plugged In"
                    print(plugged)

                else:
                    plugged="Plugged In"
                    print(plugged)
                    print(percent+'% | '+plugged)
                    speak(percent+'% | '+plugged)
                delay()

            elif 'shutdown' in query:
                speak("Want to shutdown your computer ? (yes or no): ")
                check=takeCommand()
                if check == 'no':
                    delay()
                else:
                    os.system("shutdown /s /t 1")
                exit()
                
            elif 'restart' in query:
                speak("Want to restart your computer ? (yes or no): ")
                check=takeCommand()
                if check == 'no':
                    delay();
                else:
                    os.system("shutdown /r /t 1")
                exit()

            elif 'stop listening' in query or 'rukja' in query:
                a,b=0,0
                print("Stopped listening")
                speak("Stopped listening")
                chgm=input('start listening? yes/no: ')
                if chgm=='yes':
                    a,b=1,2
                    qr=takeCommand().lower()
                else:
                    exit();

            elif "location of restaurant" in query:
                print("Getting Location......")
                speak("Getting Location......")
                print("Opening Google Maps")
                speak("Opening Google Maps")
                #open this link with the "place" and "the address" of the place
                webbrowser.open("https://www.google.co.in/maps/place/Restaurant/")
                delay()

            elif "location of store" in query:
                print("Getting Location......")
                speak("Getting Location......")
                print("Opening Google Maps")
                speak("Opening Google Maps")
                webbrowser.open("https://www.google.co.in/maps/place/Store/")
                delay()

            elif "location of shop" in query:
                print("Getting Location......")
                speak("Getting Location......")
                print("Opening Google Maps")
                speak("Opening Google Maps")
                webbrowser.open("https://www.google.co.in/maps/place/Shop/")
                delay()

            elif "location of mall" in query:
                print("Getting Location......")
                speak("Getting Location......")
                print("Opening Google Maps")
                speak("Opening Google Maps")
                webbrowser.open('https://www.google.co.in/maps/place/mall/')
                delay()

            elif "location of theme park" in query or "location of water park" in query:
                print("Getting Location......")
                speak("Getting Location......")
                print("Opening Google Maps")
                speak("Opening Google Maps")
                webbrowser.open('https://www.google.co.in/maps/place/Theme+Park/')
                delay()

            elif "greeting" in query or 'hello' in query or 'hi' in query:
                print("Hello!")
                speak("Hello!")
                print("How can i help you?")
                speak("How can i help you?")
                time.sleep(7)

            elif "ibm" in query:
                print("Opening IBM's official website.....")
                speak("Opening IBM's official website.....")
                print("For students, IBM Digital Nation is the right platform.")
                speak("For students, IBM Digital Nation is the right platform.")
                
                webbrowser.open("https://www.ibm.com/")
                webbrowser.open("https://developer.ibm.com/digitalnation/arabia/?lang=en")
                delay()

            elif "trampoline" in query:
                print('Okay sir, opening some reputed trampoline park attractions in the U.A.E......')
                speak('Okay sir, opening some reputed trampoline park attractions in the U.A.E......')
                print("Hope you get a good one and enjoy!")
                speak("Hope you get a good one and enjoy!")
                
                webbrowser.open("http://flipout.ae/")
                webbrowser.open("https://bounce.ae/")
                webbrowser.open("https://www.jump-boxx.com/")
                webbrowser.open("https://skyzone.ae/")
                webbrowser.open("https://www.magicplanetmena.com/en-ae/explore/gravity")
                delay()

            elif "TED" in query or "ted" in query:
                print("Opening the global platform of spreading ideas....")
                speak("Opening the global platform of spreading ideas....")
                webbrowser.open("https://www.ted.com/")
                delay()

            elif "food delivery" in query:
                print("Opening some food delivery companies' websites in the U.A.E.............")
                speak("Opening some food delivery companies' websites in the U.A.E.............")

                webbrowser.open("https://www.talabat.com/uae")
                webbrowser.open("https://www.zomato.com/")
                webbrowser.open("https://deliveroo.ae/")
                webbrowser.open("http://www.ubereats.com/")
                delay()

            elif "amazon" in query:
                print("Amazon is the World's largest e-commerce retailer. Opening it's website.........")
                speak("Amazon is the World's largest e-commerce retailer. Opening it's website.........")                

                webbrowser.open("https://www.amazon.ae/")
                delay()

            elif "e-commerce" in query or "online shopping" in query:
                print("Opening some global e-commerce websites for you........Please choose which one you wish to view in your browser")
                speak("Opening some global e-commerce websites for you........Please choose which one you wish to view in your browser")

                webbrowser.open("https://corporate.jd.com/")
                webbrowser.open("http://www.alibabagroup.com/")
                webbrowser.open("https://www.ebay.com/")
                webbrowser.open("https://www.rakuten.com/")
                webbrowser.open("http://ri.b2w.digital/")
                webbrowser.open("http://www.zalando.com/")
                webbrowser.open("https://www.groupon.ae/")
                delay()

            elif "movies" in query or "movie websites" in query:
                print("Opening some good movie websites to download them for free........Please choose which one you wish to view in your browser.")
                speak("Opening some good movie websites to download them for free........Please choose which one you wish to view in your browser.")

                webbrowser.open("https://archive.org/")
                webbrowser.open("https://www.youtube.com/")
                webbrowser.open("https://antmovies.tv/")
                webbrowser.open("https://yts.mx/")
                webbrowser.open("https://www.hotstar.com/in")
                webbrowser.open("https://en.savefrom.net/18/")
                delay()
                
            elif "online courses" in query or "online tutorials" in query or "online classes" in query:
                print("Opening some world-renowned, top online course sites for you........Please select which website to view in your browser.")
                speak("Opening some world-renowned, top online course sites for you........Please select which website to view in your browser.")

                webbrowser.open("https://alison.com/")
                webbrowser.open("https://www.udemy.com/")
                webbrowser.open("https://www.coursera.org/")
                webbrowser.open("https://www.edx.org/")
                webbrowser.open("https://www.udacity.com/")
                webbrowser.open("https://www.linkedin.com/learning/")
                webbrowser.open("https://www.skillshare.com/")
                webbrowser.open("https://generalassemb.ly/")
                webbrowser.open("https://www.learnsmartsystems.com/")
                webbrowser.open("https://www.codecademy.com/")
                webbrowser.open("https://www.pluralsight.com/")
                webbrowser.open("http://tv.adobe.com/")
                webbrowser.open("https://www.futurelearn.com/courses/upcoming")
                webbrowser.open("http://academicearth.org/online-college-courses/")
                delay()

            elif "academics" in query or "universities" in query or "colleges" in query:
                speak("Please enter the country in which you want to explore higher education options: USA, UK, CANADA, AUSTRALIA, DUBAI, INDIA")
                country=input("Please enter the country in which you want to explore higher education options: USA, UK, CANADA, AUSTRALIA, DUBAI, INDIA")
                query=country.lower()
                
                if "usa" in query or "us" in query or "united states" in query or "united states of america" in query:
                    print("Connecting you to the official websites of some top colleges in the USA...........")
                    speak("Connecting you to the official websites of some top colleges in the USA...........")
                    
                    webbrowser.open("https://www.princeton.edu/")
                    webbrowser.open("https://www.harvard.edu/")
                    webbrowser.open("https://www.mit.edu/")
                    webbrowser.open("https://www.stanford.edu/")
                    webbrowser.open("https://www.columbia.edu/")
                    webbrowser.open("https://www.yale.edu/")
                    webbrowser.open("https://www.upenn.edu/")
                    webbrowser.open("https://www.caltech.edu/")
                    webbrowser.open("https://www.nyit.edu/")
                    webbrowser.open("https://www.jhu.edu/")
                    webbrowser.open("https://www.gatech.edu/")
                    webbrowser.open("https://www.usf.edu/")
                    webbrowser.open("https://www.berkeley.edu/")
                    webbrowser.open("https://www.brown.edu/")
                    webbrowser.open("https://www.cornell.edu/")
                    webbrowser.open("https://www.cmu.edu/")
                    delay()

                elif "uk" in query or "great britain" in query or "united kingdom" in query or "england" in query:                    
                    print("Connecting you to the official websites of some top colleges in the UK...........")
                    speak("Connecting you to the official websites of some top colleges in the UK...........")
                    
                    webbrowser.open("https://www.ox.ac.uk/")
                    webbrowser.open("https://www.cam.ac.uk/")
                    webbrowser.open("https://www.imperial.ac.uk/")
                    webbrowser.open("https://www.kcl.ac.uk/")
                    webbrowser.open("https://www.ucl.ac.uk/")
                    webbrowser.open("https://www.ed.ac.uk/")
                    webbrowser.open("https://www.manchester.ac.uk/")
                    webbrowser.open("https://www.bristol.ac.uk/")
                    webbrowser.open("https://warwick.ac.uk/")
                    webbrowser.open("https://www.hw.ac.uk/")
                    webbrowser.open("https://www.gla.ac.uk/")
                    webbrowser.open("https://www.leeds.ac.uk/")
                    webbrowser.open("https://www.liverpool.ac.uk/")
                    webbrowser.open("https://www.birmingham.ac.uk/index.aspx")
                    webbrowser.open("https://www.mdx.ac.uk/")
                    webbrowser.open("https://www.uclan.ac.uk/")
                    delay()
                   
                elif "australia" in query or "aus" in query or "aussies" in query:                    
                    print("Connecting you to the official websites of some top colleges in Australia...........")
                    speak("Connecting you to the official websites of some top colleges in Australia...........")
                    
                    webbrowser.open("https://www.anu.edu.au/")
                    webbrowser.open("https://www.sydney.edu.au/")
                    webbrowser.open("https://www.unimelb.edu.au/")
                    webbrowser.open("https://www.unsw.com/")
                    webbrowser.open("https://www.uq.edu.au/")
                    webbrowser.open("https://www.monash.edu/")
                    webbrowser.open("https://www.adelaide.edu.au/")
                    webbrowser.open("https://www.uwa.edu.au/")
                    webbrowser.open("https://www.uow.edu.au/")
                    webbrowser.open("https://www.qut.edu.au/")
                    webbrowser.open("https://www.curtin.edu.au/")
                    webbrowser.open("https://www.deakin.edu.au/")
                    webbrowser.open("https://www.griffith.edu.au/")
                    webbrowser.open("https://www.newcastle.edu.au/")
                    webbrowser.open("https://www.swinburne.edu.au/")
                    webbrowser.open("https://www.canberra.edu.au/")
                    delay()

                elif "canada" in query or "the maple leaf country" in query:                    
                    print("Connecting you to the official websites of some top colleges in Canada...........")
                    speak("Connecting you to the official websites of some top colleges in Canada...........")
                    
                    webbrowser.open("https://www.utoronto.ca/")
                    webbrowser.open("https://www.ubc.ca/")
                    webbrowser.open("https://www.mcgill.ca/")
                    webbrowser.open("https://www.mcmaster.ca/")
                    webbrowser.open("https://www.umontreal.ca/")
                    webbrowser.open("https://www.ualberta.ca/index.html")
                    webbrowser.open("https://www.ucalgary.ca/")
                    webbrowser.open("https://www.uottawa.ca/en")
                    webbrowser.open("https://uwaterloo.ca/")
                    webbrowser.open("https://www.uwo.ca/")
                    webbrowser.open("https://www.dal.ca/")
                    webbrowser.open("https://www.ulaval.ca/en")
                    webbrowser.open("https://www.queensu.ca/")
                    webbrowser.open("https://www.sfu.ca/")
                    webbrowser.open("https://www.yorku.ca/")
                    webbrowser.open("https://umanitoba.ca/")
                    delay()

                elif "dubai" in query or "dxb" in query:                    
                    print("Connecting you to the official websites of some top colleges in Dubai...........")
                    speak("Connecting you to the official websites of some top colleges in Dubai...........")
                    
                    webbrowser.open("https://www.uaeu.ac.ae/en/")
                    webbrowser.open("https://recruit.hct.ac.ae/")
                    webbrowser.open("https://www.sharjah.ac.ae/")
                    webbrowser.open("https://www.aus.edu/")
                    webbrowser.open("https://www.nyit.edu/abu_dhabi")
                    webbrowser.open("https://www.ku.ac.ae/")
                    webbrowser.open("https://www.zu.ac.ae/main/en/")
                    webbrowser.open("https://www.aud.edu/")
                    webbrowser.open("https://www.adu.ac.ae/")
                    webbrowser.open("https://www.ajman.ac.ae/")
                    webbrowser.open("https://www.skylineuniversity.ac.ae/")
                    webbrowser.open("https://aau.ac.ae/")
                    webbrowser.open("https://ud.ac.ae/")
                    webbrowser.open("https://www.mdx.ac.ae/")
                    webbrowser.open("https://buid.ac.ae/")
                    webbrowser.open("https://www.hw.ac.uk/dubai/index.htm")
                    webbrowser.open("https://www.manipaldubai.com/")
                    webbrowser.open("https://www.bits-pilani.ac.in/Dubai/")
                    delay()

                elif "india" in query or "bharat" in query:                    
                    print("Connecting you to the official websites of some top colleges in India...........")
                    speak("Connecting you to the official websites of some top colleges in India...........")

                    webbrowser.open("https://www.iitb.ac.in/")
                    webbrowser.open("https://home.iitd.ac.in/")
                    webbrowser.open("https://www.iitm.ac.in/")
                    webbrowser.open("http://iitkgp.ac.in/")
                    webbrowser.open("https://www.iitg.ac.in/")
                    webbrowser.open("https://www.iitr.ac.in/")
                    webbrowser.open("https://iith.ac.in/")
                    webbrowser.open("https://www.bits-pilani.ac.in/")
                    webbrowser.open("https://manipal.edu/mu.html")
                    webbrowser.open("http://www.nitc.ac.in/")
                    webbrowser.open("https://www.nitw.ac.in/")
                    webbrowser.open("https://www.nitrkl.ac.in/")
                    webbrowser.open("https://www.nitt.edu/")
                    webbrowser.open("https://nitdelhi.ac.in/")
                    webbrowser.open("https://www.iimtu.com/")
                    webbrowser.open("https://www.iimb.ac.in/home")
                    delay() 

                else:
                    print("Sorry I could not recognize your choice")
                    speak("Sorry I could not recognize your choice")

            elif "hospital" in query or "hospitals in uae" in query or "clincs" in query or "clincs in uae" in query :
                speak("Are you looking for Goverment and private Hospitals and clinic. Please provide your choice ")
                hospitals=input("Are you looking for government or private hospitals. Please provide your choice ")
                
                if hospitals.lower() == "government":
                    print("Connecting you to the official websites of government hospitals in UAE...........")
                    speak("Connecting you to the official websites of government hospitals in UAE...........")
                    
                    webbrowser.open("https://www.dha.gov.ae/en/Pages/DHAHome.aspx")
                    webbrowser.open("https://www.mohap.gov.ae/en/Pages/default.aspx")
                    delay()

                elif hospitals.lower() == "private": 
                    print("Connecting you to the official websites of some private hospitals in UAE...........")
                    speak("Connecting you to the official websites of some private hospitals in UAE...........")
                          
                    webbrowser.open("https://nmc.ae/")
                    webbrowser.open("https://www.zulekhahospitals.com/")
                    webbrowser.open("https://asterclinic.ae/")
                    webbrowser.open("http://www.belhoulspeciality.com/")
                    webbrowser.open("http://www.ihd.ae/")
                    webbrowser.open("https://aiwa.ae/category/hospitals")
                    webbrowser.open("https://www.ahdubai.com/")
                    delay()

                else:
                    print("Sorry I could not recognize your choice")
                    speak("Sorry I could not recognize your choice")   
     
            elif "airlines" in query or "airlines booking" in query or "flight" in query or "flight booking" in query :   
                print("here are some online flight booking websites")
                speak("here are some online flight booking websites")                

                webbrowser.open("https://www.emirates.com/ae/english/")
                webbrowser.open("https://www.airarabia.com/en")
                webbrowser.open("https://www.flydubai.com/en/")
                webbrowser.open("https://www.etihad.com/en-ae/")
                webbrowser.open("https://wizzair.com/en-gb/#/")
                webbrowser.open("http://www.airindia.in/")
                webbrowser.open("https://www.goindigo.in/")
                webbrowser.open("https://www.spicejet.com/")
                webbrowser.open("https://www.airindiaexpress.in/en")
                webbrowser.open("https://www.britishairways.com/")
                delay()

            elif "online travel company " in query or "cheap travel" in query or "travel planner" in query :    
                print("here are some websites with cheap flight ticket options")
                speak("here are some websites with cheap flight ticket options")
                
                webbrowser.open("https://www.cleartrip.ae/")
                webbrowser.open("https://www.tajawal.ae/en")
                webbrowser.open("https://www.skyscanner.ae/")
                webbrowser.open("https://www.agoda.com/")
                webbrowser.open("https://www.tripsavvy.com/")
                webbrowser.open("https://discover.trivago.ae/")
                delay()
   
            elif "cinema booking" in query or "cinemas in uae" in query or "cinema" in query or "movie" in query or "theatre" in query : 
                print("here are some online booking websites for cinemas")
                speak("here are some online booking websites for cinemas")

                webbrowser.open("https://www.reelcinemas.ae/en/")
                webbrowser.open("https://www.novocinemas.com/")
                webbrowser.open("https://voxcinemas.com/regions")
                webbrowser.open("https://starcinemas.ae/")
                delay()

            elif "calculator" in query or "open calculator" in query :
                print("Welcome to Calculator")
                calculate1()
                delay()

            elif 'goodbye' in query :
                speak('goodbye dear sir')
                a,b=0,0
                exit()
                        
root.mainloop()









            



            
            
            

        

        
