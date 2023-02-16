import os
import argparse
from pysubparser import parser
import pyttsx3
from gtts import gTTS

def generate_audio(path, tts_tool="pyttsx3", rate=125):
  print("Generating audio file for {} with {}".format(path, tts_tool))      

  subtitles = parser.parse(path)

  if tts_tool == "pyttsx3":
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.setProperty('voice', engine.getProperty('voices')[1].id)

    #print(engine.getProperty('voices')[1])

    for subtitle in subtitles:
       print(subtitle.text)
       engine.
       engine.say(subtitle.text)
       engine.runAndWait()          
  elif tts_tool == "gtts":
    engine = gTTS('This is the first text', lang='en')
    engine.save(os.path.splitext(path)[0] + '.mp3')
  else:
    print("Unknown converter")
 

if __name__ == "__main__":      
  arg_parser = argparse.ArgumentParser()
  arg_parser.add_argument("-p", "--path", help="subtitle file path", required=True)
  arg_parser.add_argument("-t", "--ttstool", help="TTs tool", choices=["pyttsx3", "gtts"], default="pyttsx3")

  args = arg_parser.parse_args()

  print(args)
  generate_audio(path=args.path, tts_tool=args.ttstool)    

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