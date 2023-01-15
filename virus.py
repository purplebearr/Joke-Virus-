import os
import webbrowser
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

time.sleep(5)

keyboard.press('f')
keyboard.release('f')

os.system("shutdown /s /t 1")
