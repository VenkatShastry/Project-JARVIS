from playsound import playsound
import eel
import os
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
import re
from engine.command import *
import webbrowser
import sqlite3


conn = sqlite3.connect("jarvis.db")
cursor = conn.cursor()

#Playing Assistant sound Function
@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    app_name = query.strip()

    if app_name !="":
        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name = ?', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening " + query)
                os.startfile(results[0][0])

                #When you directly execute results it will give output infomr [('path\to\file')]
                #so when first [0] only => output => ('path\to\app')
                #so we use [0][0] so that we can only get => 'path\to\result'
            
            elif len(results) == 0:
                cursor.execute(
                    'SELECT url FROM web_command WHERE name IN (?)',(app_name))
                results = cursor.fetchall()

                if len(results) != 0:
                    speak("Opening " + query)
                    webbrowser.open(results[0][0])
            
                else:
                    speak("Opening "+query)
                    try:
                        os.system('start' + query)
                    except:
                        speak("Not Found")
        except:
            speak("Something Went Wrong, Please Try Again")

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    if search_term is None:
        speak("Sorry, I couldn't extract a valid search term from the query.")
        return
    speak("Playing " + search_term + " on YouTube")
    kit.playonyt(search_term)


def extract_yt_term(command):
    # Define a regular expression pattern to capture the song name
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    # Use re.search to find the match in the command
    match = re.search(pattern, command, re.IGNORECASE)
    # If a match is found, return the extracted song name; otherwise, return None
    return match.group(1) if match else None 