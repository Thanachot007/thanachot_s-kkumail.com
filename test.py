import tkinter as tk
from tkinter import * 
import subprocess
import os

root = tk.Tk()
def open():
        subprocess.run(['D:\\python_exe\\python.exe', 'C:\\Users\\Thanachot\\Anaconda3\\envs\\opencv-env\\calculator\\calculator.py'])
def name():
        subprocess.run(['D:\\python_exe\\python.exe', 'C:\\Users\\Thanachot\\Anaconda3\\envs\\opencv-env\\calculator\\name.py'])
def voicecommand():
        subprocess.run(['D:\\python_exe\\python.exe', 'C:\\Users\\Thanachot\\Anaconda3\\envs\\opencv-env\\calculator\\speechtotext.py'])
        # os.system("python speechtotext.py")
        
btn = Button(root, text="calculator", command=open, bg="sky blue").grid()
btn2 = Button(root, text="name", command=name, bg="sky blue").grid()
btn3 = Button(root, text="voice", command=voicecommand, bg="sky blue").grid()

  
root.mainloop()
