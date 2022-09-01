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
engine.say('Hello ')
engine.say('I am your virtual assistant alexa')
engine.say('How can i help you')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
   try:
       with sr.Microphone() as source:
          print('Your Alexa is Listening...')
          voice = listener.listen(source)
          command = listener.recognize_google(voice)
          command = command.lower()
          if 'alexa' in command:
            command = command.replace('alexa', '')
            print(command)

   except:
       pass
   return command


def run_alexa():
    command = take_command()
    print((command))
    if 'play' in command:
        song = command.replace('play','')
        talk('Playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('The time is' + time)
        talk('current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'a date' in command:
        print('Go to hell, I am in a relationship with wifi')
        talk('Go to hell, I am in a relationship with wifi')
    elif 'joke' in command:
        talk('Haha, yes sure here you go')
        talk((pyjokes.get_joke()))
    elif 'send a message' in command:
        a = datetime.datetime.now().strftime('%I, %M+1')
        print(a)
        print('Please, enter the time you want to send the message')
        talk('Please, enter the time you want to send the message')
        hour = int(input("Enter hour: "))
        min = int(input("Enter minute: "))
        print('please enter the phone number you want to send the message')
        talk('please enter the phone number you want to send the message')
        phnoa = str(input("Enter the phone number: "))
        print("Please enter your message")
        talk("Please enter your message")
        mesa = str(input("Enter the message: "))

        pywhatkit.sendwhatmsg(phnoa,mesa,hour, min)

    else:
        talk('Please say the command again, I could not recognize it properly')
        print('Please say the command again, I could not recognize it properly')


while True:
    run_alexa()