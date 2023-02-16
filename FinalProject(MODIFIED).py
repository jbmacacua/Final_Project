#Import the packages needed
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

#Detect the input voices
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Create an empty dictionary to store data on song requests
song_data = {}

#Make alexa talk
def talk(text):
    engine.say(text)
    engine.runAndWait()

#Make alexa recogrize the commands
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

#Add bubble sort command
bubblelist = [97, 23, 100, 88, 66, 84, 7, 21, 52, 17]

for elements in range(len(bubblelist)-1):
    for element in range (len(bubblelist)-1):
        if bubblelist[element] > bubblelist[element+1]:
            bubblelist[element], bubblelist[element+1] = bubblelist[element+1], bubblelist[element]

#Add Selection sort command
sellist = [97, 23, 100, 88, 66, 84, 7, 21, 52, 17]
for element in range (len(sellist)):
    min_value = min(sellist[element:])
    min_index = sellist.index(min_value)
    sellist[element], sellist[min_index] = sellist[min_index], sellist[element]

#Give commands to alexza
def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')

#Run alexa continouosly
while True:
    run_alexa()