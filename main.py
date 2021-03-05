import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def input_command():
    try:
        with sr.Microphone() as source:
            print('Listening.....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'friday' in command:
                command = command.replace('friday', '')
                print(command)

    except:
        pass
    return command

def run():
    command = input_command()

    if 'play' in command:
        song = command.replace('play','')
        talk('Ya sure enjoy ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('Time right now is' + time)

    elif 'search' in command:
        info = command.replace('search','')
        result = wikipedia.summary(info, 5)
        talk('Here is the result' + result)

    elif 'love' in command:
        talk('Thank you Aakriti I love you too')

    elif 'jokes' in command:
        talk(pyjokes.get_jokes())

    elif 'message' in command:
        mess = command.replace('message' ,'')
        chat = pywhatkit.sendwhatmsg('+918360387125','I LOVE YOU BABY', 20, 20)
        talk('Successfully send' + chat)

    else:
        talk('Sorry I did not understood say it again.')


while True:
    run()

