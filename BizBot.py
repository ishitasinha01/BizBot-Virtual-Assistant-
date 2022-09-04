import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib
# dict={"ishita":"ishitasinha@gmail.com","prachi":"prachilohani33@gmail.com","mahiman":"mahimanjain189nblock@gmail.com"}
# can create this type of dict if we want to send email based on name to many or any one from list
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices)
engine.setProperty("vioces", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning")
    elif hour >= 12 and hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")

    speak("iam biz-bot . please tell me how may i help you")


def takeCommand():
    # it takes microphone return from user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        # print(e)

        print("say that again please...")
        return " None"
    return query
# go to less secure apps in gmail enable
# uncoment this to send email
# def sendEmail(to,content):
#     server=smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo()
#     server.starttls()
#     server.login('ishitasinha@gmail.com','passoword')
#     server.sendmail('ishitasinha106@gmail.com',to,content)
#     server.close()
    # can write password as it is
    # to secure password write password in txt file and read password from txt file and put that file in some where safe


if __name__ == "__main__":
  wishMe()
  while True:

    query= takeCommand().lower()

    # logic for executing task based on query
    if 'wikipedia' in query:
        speak('Searching wikipedia...')
        query=query.replace("wikipedia","")
        results= wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
    elif'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open youtube' in query:
        webbrowser.open("google.com")
    elif 'paly music' in query:
        music_dir="D:\\Ishita Sinha\\Music"
        songs=os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))
        # ths will paly the first song
    # \\ to escape char
    # can add additonal freature to play only mp3
    # can install random module and play the o to n any song in the given range
    elif 'the time' in query:
        strTime:datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strTime}")
    # elif 'open code' in query:
    #     codePath"...."
    #     os.startfile(codePath)
    #       to open and editor
    # uncommen this to send email
    # elif 'send email to ishita' in query:
    #     try:
    #         speak("what should i say?")
    #         content = takeCommand()
    #         to ="ishitasinha@gamil.com"
    #         sendEmail(to,content)
    #         speak("email has been sent")
    #     except Exception as e:
    #         print(e)
    #         speak("sorry not able to send this email")
# installed speechrecognition as it was not beig with the terminal went to Settings -> Project:(nameofyourproject)-> Python: Interpreter. Click on plus and find SpeechRecognition, install it.
# or any other package
# webbrowser and datetime pre installed
# can do many other functions