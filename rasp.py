#importing libraries
import mendeleev
import speech_recognition as sr
import random
import os
import RPi.GPIO as GPIO
import time
import pygame
import playsound



#initializing
led= 16
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)
listener=sr.Recognizer()
name=[]
for i in range(1,119):
    a=mendeleev.element(i)
    name.append(a.name.lower())


#input
def take_command():
    try:
        with sr.Microphone() as source:
            GPIO.output(led, GPIO.HIGH)
            listener.pause_threshold = 1
            voice = listener.listen(source,timeout=5,phrase_time_limit=5)
            GPIO.output(led, GPIO.LOW)
            command=listener.recognize_google(voice)
            command=command.lower()
            return command
    except:
        talk("cant hear you, say again")
        return take_command()

#output
def talk(key):
    sm="pico2wave -w lookdave.wav \""+key+"\" && aplay lookdave.wav"
    os.system(sm)


#learning
def learning():
    talk("What Element you want to know ?")
    s = take_command()
    if s in name:
        n = name.index(s) + 1
        el = mendeleev.element(n)
        talk("Symbol " + str(el.symbol))
        talk("atomic number " + str(el.atomic_number))
        talk("atomic weight " + str(el.atomic_weight))
        talk("Block " + str(el.block))
        talk("cas " + str(el.cas))
        talk("electrons " + str(el.electrons))
        talk("electronic configuration " + str(el.ec))
        talk("neutrons " + str(el.neutrons))
        talk("period " + str(el.period))
        talk("protons " + str(el.protons))
        talk("series " + str(el.series))
    else:
        talk("Give a valid Element Name please")
        return learning()

#Quiz
def quiz():
    q=random.choice(name)
    index=name.index(q)+1
    el=mendeleev.element(index)
    talk(q)
    talk("symbol of "+q)
    symbol=take_command()
    if symbol== el.symbol.lower():
        talk("correct answer")
    else:
        talk("wrong answer, the correct answer is "+el.symbol)
    talk("atomic number of "+q)
    an=take_command()
    if an==str(el.atomic_number):
        talk("correct answer")
    else:
        talk("wrong answer, the correct answer is "+ str(el.atomic_number))
    talk("Mass number of "+q)
    mn=take_command()
    if mn==str(round(el.atomic_weight)):
        talk("correct answer")
    else:
        talk("wrong answer, the correct answer is "+str(round(el.atomic_weight)))

#periodic table
def periodictable():
    playsound.playsound("music.mp3")


#main function
talk("Elementiqua is On")
while(True):
    talk("Hello kid what do you want ?")
    command = take_command()
    if "properties" in command or "know" in command:
        learning()
    elif "quiz" in command or "practice" in command:
        quiz()
    elif "periodic" in command or "table" in command:
        periodictable()
    elif "sleep" in command:
        talk("thank you for useing me, bye")
        break
    else:
        talk("You can know any properties of an element or you can attend quiz or you can know the periodic table elements")

