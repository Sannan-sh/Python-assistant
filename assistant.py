import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime

r = sr.Recognizer()

def speak(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(command)
    engine.runAndWait()
    
def commands():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print('Listening... Ask now...')
            audioin = r.listen(source)
            my_text = r.recognize_google(audioin)  # Changed to Google Web Speech API
            my_text = my_text.lower()
            print(my_text)
            
            #ask to play song
            if 'play' in my_text:
                my_text = my_text.replace('play', '')
                speak('playing '+my_text)
                pywhatkit.playonyt(my_text)
                commands()
                
            #ask date
            elif 'date' in my_text:
                today = datetime.date.today()
                formatted_date = today.strftime("%B %d, %Y")
                speak(f"Today is {formatted_date}")
                commands()
                
            #ask time
            elif 'time' in my_text:
                timenow = datetime.datetime.now().strftime('%H%M:')
                speak("The time right now is" +timenow)
                commands()
                
            #ask details about any person
            elif "who is " in my_text:
                person = my_text.replace('who is','')
                info = wikipedia.summary(person,3)
                speak(info)
                commands()
            
            #ask about anything
            elif 'what is' in my_text:
                knowledge = my_text.replace('what is','')
                info = wikipedia.summary(knowledge,5)
                speak(info)
                commands()
                
            #if no response 
            else:
                speak("Please give a proper command! I'm ready to help you")
                commands()

    except Exception as e:
        print(f'Error: {str(e)}')  # Print the specific error

#main program
speak("Hi! I'm Cosmos,your personal assistant! How can I help you" )
commands()

