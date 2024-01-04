from gtts import gTTS
import os
import playsound
import speech_recognition as sr

LANG="ar"

def speak(text):
    gts = gTTS(text=text,lang='ar')
    gts.save('ohi.mp3')
    os.system('ohi.mp3')
    #os.remove('ohi.mp3')

listener = sr.Recognizer()

def listen():

    try:
        with sr.Microphone() as source:

            voice = listener.listen(source)
            comond = listener.recognize_google(voice , language=LANG)
            if 'ألكسا' in comond:
                speak(comond)
                print(comond)
                return comond
            else:
                return ""

           
    except:
        speak('من فضلك ,أعد ما قلته')



def run():
    v = True
    while v :
        comond = listen()
        if 'إنهاء' in comond:
            v= False
            speak('مع السلامة')
run()







