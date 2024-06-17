import pyttsx3
engine = pyttsx3.init()
engine.say("Good morning , can I be your virtual assistant")
engine.runAndWait()



""" RATE"""
rate = engine.getProperty('rate')  
print (rate)                        
engine.setProperty('rate', 125)     


"""VOLUME"""
volume = engine.getProperty('volume')   
print (volume)                          
engine.setProperty('volume',1.0)    

"""VOICE"""
voices = engine.getProperty('voices')     
engine.setProperty('voice', voices[1].id)   #1 for female , 0 for male

engine.say("Hello , am I speaking too fast?")
engine.say('My current speaking rate is ' + str(rate))
engine.say(" I have many features , can be altered to your needs , thanks to my master SARTHAK")
engine.say("what is there for breakfast?")
engine.runAndWait()
engine.stop()

