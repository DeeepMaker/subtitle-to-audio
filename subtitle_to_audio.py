import sys
import pyttsx3
from gtts import gTTS

def generate_audio(file_name, lib):
    print("generating audio file for {} with {}".format(file_name, lib))    

if __name__ == "__main__":      
  n_args = len(sys.argv) - 1
  if n_args == 1:
      file_name = sys.argv[1]
      lib = "pyttsx3"
  elif n_args == 2:
      file_name = sys.argv[1]
      lib = sys.argv[2]
  else:
      print("Proper usage text place holder")   
      sys.exit()

  generate_audio(file_name=file_name, lib=lib)    

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

"""
from gtts import gTTS
tts = gTTS('This is the first text', lang='en')
tts.save('hello.mp3')
"""