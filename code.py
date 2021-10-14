#importing libraries
import mendeleev
import speech_recognition as sr
import pyttsx3
import pyaudio
import random
import sphinxbase
import pocketsphinx


#initializing
listener=sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
name=[]
for i in range(1,119):
    a=mendeleev.element(i)
    name.append(a.name.lower())

#input
def take_command():
    with sr.Microphone() as source:
        listener.pause_threshold = 0.8
        listener.energy_threshold = 300
        listener.adjust_for_ambient_noise(source, duration=1)
        print("listening...")
        voice = listener.listen(source, timeout=5, phrase_time_limit=5)
        command = listener.recognize_sphinx(voice, language='en-In')
        command = command.lower()
        return command
    '''except:
        talk("cant hear you, say again")
        return take_command()'''

#output
def talk(text):
    rate = 130
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

#learning
def learning():
    talk("What Element you want to know ?")
    s = take_command()
    print(s)
    if s in name:
        print("Properties:")
        n = name.index(s) + 1
        el = mendeleev.element(n)
        talk("Symbol " + str(el.symbol))
        print("Symbol:",str(el.symbol))
        talk("atomic number " + str(el.atomic_number))
        print("atomic number: "+ str(el.atomic_number))
        talk("atomic weight " + str(el.atomic_weight))
        print("atomic weight: "+str(el.atomic_weight))
        talk("Block " + str(el.block))
        print("block: "+ str(el.block))
        talk("cas " + str(el.cas))
        print("cas: "+ str(el.cas))
        talk("electrons " + str(el.electrons))
        print("electrons: "+str(el.electrons))
        talk("electronic configuration " + str(el.ec))
        print("elctronic configuration: "+str(el.ec))
        talk("neutrons " + str(el.neutrons))
        print("neutrons: "+ str(el.neutrons))
        talk("period " + str(el.period))
        print("Period: "+ str(el.period))
        talk("protons " + str(el.protons))
        print("Protons: "+str(el.protons))
        talk("series " + str(el.series))
        print("series: "+ str(el.series))
    else:
        talk("Give a valid Element Name please")
        return learning()

#Quiz
def quiz():
    q=random.choice(name)
    index=name.index(q)+1
    el=mendeleev.element(index)
    talk(q)
    print(q)
    talk("symbol of "+q)
    print("symbol of "+q)
    symbol=take_command()
    if symbol== el.symbol.lower():
        talk("correct answer")
        print("correct answer")
    else:
        talk("wrong answer, the correct answer is "+el.symbol)
        print("wrong anser, the correct answer is "+el.symbol)
    talk("atomic number of "+q)
    print("atomic number of "+q)
    an=take_command()
    if an==str(el.atomic_number):
        talk("correct answer")
        print("correct answer")
    else:
        talk("wrong answer, the correct answer is "+ str(el.atomic_number))
        print("wrong anser, the correct answer is "+ str(el.atomic_number))
    talk("Mass number of "+q)
    print("mass number of "+q)
    mn=take_command()
    if mn==str(round(el.atomic_weight)):
        talk("correct answer")
        print("correct answer")
    else:
        talk("wrong answer, the correct answer is "+str(round(el.atomic_weight)))
        print("wrong answer, the correct answer is "+str(round(el.atomic_weight)))

#periodic table
def periodictable():
    pass


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
        print(command)

