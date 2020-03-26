import os
import subprocess

print(os.path.abspath('calculator.py'))
print(os.path.abspath('D:\python_exe\python.exe'))




print("y to open , n to close : ")
check = input()

if check == "y":
    # os.system('"D:\\python_exe\\python.exe" "C:\\Users\\Thanachot\\Anaconda3\\envs\\opencv-env\\calculator\\calculator.py"')
    subprocess.run(['D:\\python_exe\\python.exe', 'C:\\Users\\Thanachot\\Anaconda3\\envs\\opencv-env\\calculator\\calculator.py'])
    