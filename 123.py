
import speech_recognition as sr
import RPi.GPIO as GPIO



#obtain audio from the microphone
r=sr.Recognizer() 
with sr.Microphone() as source:
    print("Please wait. Calibrating microphone...") 
    #listen for 5 seconds and create the ambient noise energy level 
    r.adjust_for_ambient_noise(source, duration=5) 
    print("Say something!")
    audio=r.listen(source)

# recognize speech using Google Speech Recognition 
try:
    print("Google Speech Recognition thinks you said:")
    a=r.recognize_google(audio, language="zh-TW")
    print(a)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("No response from Google Speech Recognition service: {0}".format(e))    

def __init__(self):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)
    pass

def Hello():
    LEDon = GPIO.output(4.1)
    print("燈已經打開")
    
if a=="開燈":
        Hello()



def Hello():
    print("燈已經打開")

if a=="開燈":
    Hello()


#上面程式是利用 SpeechRecognition 模組中的 recognixe_google() 函數透過 Google 語音辨識 API 來將麥克風收到的語音物件 audio 辨識成指定語系的文字 :
