#Python 2.x program for Speech Recognition 
  
import speech_recognition as sr
import os
from gtts import gTTS
import subprocess
import time
from tkinter import *
import tkinter.messagebox as tkMessageBox
from PIL import ImageTk, Image
from tkinter import filedialog
import re
import winsound
import webbrowser
import subprocess

def callback():
  root.destroy()
  os.system("exit")

#enter the name of usb microphone that you found 
#using lsusb 
#the following name is only used as an example 
mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"
#Sample rate is how often values are recorded 
sample_rate = 48000
#Chunk is like a buffer. It stores 2048 samples (bytes of data) 
#here.  
#it is advisable to use powers of 2 such as 1024 or 2048 
chunk_size = 2048
#Initialize the recognizer 
r = sr.Recognizer()
# m = sr.microphone()
#set threhold level
en_lang = "EN"
language_speak = "TH"
#generate a list of all audio cards/microphones 
mic_list = sr.Microphone.list_microphone_names() 

#the following loop aims to set the device ID of the mic that 
#we specifically want to use to avoid ambiguity. 
for i, microphone_name in enumerate(mic_list): 
    if microphone_name == mic_name: 
        device_id = i 
  
#use the microphone as source for input. Here, we also specify  
#which device ID to specifically look for incase the microphone  
#is not working, an error will pop up saying "device_id undefined" 
with sr.Microphone(device_index = 0, sample_rate = sample_rate,  
                        chunk_size = chunk_size) as source:
    #wait for a second to let the recognizer adjust the  
    #energy threshold based on the surrounding noise level 
    r.adjust_for_ambient_noise(source) 
    print("Speak function you want to access : ") 
    #listens for the user's input 
    audio = r.listen(source) 
          
    try: 
        text = r.recognize_google(audio, language="th-TH")
  
        # myobj = gTTS(text="คุณพูดว่า "+text, lang=language_speak, slow=False) 
        print("you said: " + text.replace(" ", ""))
        #ดัก pattern ของ inpout 
        if re.match("[0-9]{10}", text.replace(" ", "")):
          print("is matched") 
          std_id = text.replace(" ", "")[:9] + '-' + text.replace(" ", "")[9:]
          print(std_id)
          winsound.PlaySound("72871__tim-kahn__saved.wav", winsound.SND_ASYNC)
          
        root = Tk()
        root.title("Face recognition")
        root.geometry("500x100+300+300") #X*Y+right(ซ้ายมาขวา)+down(บนลงล่าง)
        #--- show text after speak in voice command ---
        Label(root, text="you said", fg="green", wraplength=700,font= "Verdana 20").pack()
        Label(root, text=text, fg="green", wraplength=700,font= "Verdana 20 underline").pack()  #wraplength จัดบรรรทัดให้อัตโนมัติ  400 ก็อาจจะตัดคำสั้น 700 ก็ตัดคำยาวกว่า justify แล้วแต่จะจัดชิดซ้ายหรือขวา
        root.after(2000, callback)  #หลังจาก 2 วิให้ call function
        
        root.mainloop()

        if "ปิดโปรแกรมเสียง" in text : 
          gTTS(text=text, lang=language_speak, slow=False)
          os.system("exit")
        elif "เปิดเครื่องคิดเลข" in text:
          subprocess.run(['D:\\python_exe\\python.exe', 'C:\\Users\\Thanachot\\Anaconda3\\envs\\opencv-env\\calculator\\calculator.py'])

          
        elif "ล้างข้อมูล" in text:
          os.system("cls")
        else:
          time.sleep(1)
          os.system("python speechtotext.py")

    except sr.UnknownValueError: 
        print("Google Speech Recognition could not understand audio") 
        os.system("python speechtotext.py")
    except sr.RequestError as e: 
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        os.system("python speechtotext.py")