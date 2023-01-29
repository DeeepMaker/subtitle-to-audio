# import pyttsx3
# engine = pyttsx3.init()

# voices = engine.getProperty('voices')       #getting details of current voice
# #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

# print(engine.getProperty("rate"))
# engine.setProperty('rate', 125)


# engine.say("I will speak this text")
# engine.save_to_file("This is the first text", "aud1.mp3")
# engine.save_to_file("This is the second text", "aud2.mp3")
# engine.runAndWait()

from gtts import gTTS
tts = gTTS('This is the first text', lang='en')
tts.save('hello.mp3')