import subprocess
from webbrowser import open_new

import pyttsx3
import speech_recognition as sr
from speech_recognition import Recognizer

r: Recognizer = sr.Recognizer ( )
with sr.Microphone ( ) as source :
    print ( 'Silence please !! , Calibrating the background noise' )
    engine = pyttsx3.init ( )
    engine.say ( 'Silence please !! , Calibrating the background noise' )
    engine.runAndWait ( )
    r.adjust_for_ambient_noise ( source )
    print ( 'Calibrated..... Now you can speak' )
    engine.say ( 'Calibrated..... Now you can speak' )
    engine.runAndWait ( )

    audio = r.listen( source )

text = r.recognize_google ( audio )
text = text.lower ( )

if text == 'hello jarvis' :
    print ( 'Hi' )
    print ( 'May I  know your name ??' )
    engine.say ( 'Hi' )
    engine.runAndWait ( )
    engine.say ( 'May I know your name ??' )
    engine.runAndWait ( )

r = sr.Recognizer ( )
with sr.Microphone ( ) as source :
    print ( '(.... Listening ....)' )

    audio = r.listen ( source )

    text = r.recognize_google ( audio )
    text = text.lower ( )


    print ( 'Hello' , str ( text ) )
    print ( 'How can I help you ???' )
    engine.say ( 'Hello' + text )
    engine.runAndWait ( )
    engine.say ( 'How can I help you ???' )
    engine.runAndWait ( )

r = sr.Recognizer ( )
with sr.Microphone ( ) as source :
    print ( '(.... Listening ....)' )

    audio = r.listen ( source )

    text = r.recognize_google ( audio )
    text = text.lower ( )

    print ( '(.... Opening ....)' )
    engine.say ( 'Opening' )
    engine.runAndWait ()

if text == 'open google' :
    open_new ( 'https://google.com' )
elif text == 'open youtube' :
    open_new ( 'https://youtube.com' )
elif text == 'open amazon' :
    open_new ( 'https://google.in' )
elif text == 'open gmail' :
    open_new ( 'https://gmail.com' )
elif text == 'open calculator':
    subprocess.call('calc.exe')
