import pyttsx3
import speech_recognition as sr
import datetime
import time
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit as kit
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def arunavo():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    time.sleep(2)
    speak("hey arpan...... whats up, say how may i help u")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception :
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('arpanroy.cs2020@nsec.ac.in', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    arunavo()
    while True:
        query = takeCommand().lower()
        if 'what is meant' in query or 'stands for' in query or 'what is the meaning of' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            time.sleep(2)
            speak('if u think this does not match your answer try saying search for')

        elif 'open youtube and play the song' in query:
            zr=query.split(" ")
            a = zr[6::]
            z = ' '.join([str(elem) for elem in a])
            speak(f"playing,  {z}")
            kit.playonyt(z)
            break
        elif 'open youtube and play ' in query:
            zz=query.split(" ")
            a = zz[4::]
            z = ' '.join([str(elem) for elem in a])
            speak(f"playing,  {z}")
            kit.playonyt(z)
            break
        elif 'youtube' in query:
            zo=query
            kit.playonyt(zo)
            break
        elif 'search for' in query:
            kk=query.split(" ")
            aa=kk[2::]
            zx = ' '.join([str(elem) for elem in aa])
            kit.search(zx)
            break
        elif '.com' in query:
            ss=query.split(" ")
            dd=ss[1::]
            zc = ' '.join([str(elem) for elem in dd])
            webbrowser.open(zc)
            break
        elif 'play music' in query:
            music_dir = 'C:\\Users\\Arpan roy\\AppData\\Local\\Microsoft\\WindowsApps\\SpotifyAB.SpotifyMusic_zpdnekdrzrea0\\Spotify.exe'
            os.startfile(music_dir)
            break
        elif 'what is the time' in query or 'what is the time right now' in query or 'time right now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            break
        elif 'open windows 7' in query:
            codePath = "C:\\Users\\Arpan roy\\VirtualBox VMs\\windows 7\\windows 7.vbox"
            os.startfile(codePath)
            break
        elif 'open metasploitable 2' in query:
            codePath = "C:\\Users\\Arpan roy\\VirtualBox VMs\\metasploitable 2\\metasploitable 2.vbox"
            os.startfile(codePath)
            break
        elif 'open windows 10' in query:
            codePath = "C:\\Users\\Arpan roy\\VirtualBox VMs\\windows 10\\windows 10.vbox"
            os.startfile(codePath)
            break
        elif 'open kali linux' in query:
            codePath = "C:\\Users\\Arpan roy\\VirtualBox VMs\\kali\\kali.vbox"
            os.startfile(codePath)
            break
        elif 'open centos' in query:
            codePath = "C:\\Users\\Arpan roy\\VirtualBox VMs\\CentOS_8.3.2011_VBM_LinuxVMImages.COM\\CentOS_8.3.2011_VBM_LinuxVMImages.COM.vbox"
            os.startfile(codePath)
            break
        elif 'email to' in query:
            try:
                speak("What should I write in email")
                sp=input("enter what u want to send")
                to = "bajirao.arpan@gmail.com"
                sendEmail("arpanroy.cs2020@nsec.ac.in", sp)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry darling   arpan   , please sent the email by yourself")
        elif 'remember' in query:
            rem=query.split(" ")
            pi = rem[1::]
            ze = ' '.join([str(elem) for elem in pi])
            speak("ok...i will remember that")
        elif 'say what i told you to remember' in query:
            speak(ze)
        elif "none" in query:
            if len(query) > 4:
                speak("i found this on google")
                kit.search(query)
                break
            else:
                continue
        else:
            speak("i found this on google")
            kit.search(query)
            break
