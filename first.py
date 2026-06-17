import pyjokes
import pyttsx3
joke=pyjokes.get_joke()
engine=pyttsx3.init()
print(joke)
engine.say("I would do anything for you , you are my life , you are the reason of my life ")
engine.runAndWait()