import os
import eel
from engine.features import *
from engine.command import *


# this is to inform eel that our frontend files are in this folder
eel.init("www")


playAssistantSound()

#now this is to open our frontend Jarvis in App Mode with the help of Browser
# which pops a window just like an Application Window

os.system('start msedge.exe --app="http://localhost:8000/index.html"') #you can change the browser if you want

eel.start('index.html', mode=None, host= 'localhost',block=True)