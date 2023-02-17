import os
import tempfile
import argparse
from pysubparser import parser
from pydub import AudioSegment
import pyttsx3
from gtts import gTTS
from datetime import timedelta

def time_to_ms(time):
  return ((time.hour * 60 + time.minute) * 60 + time.second) * 1000 + time.microsecond / 1000

def generate_audio(path, tts_tool="pyttsx3", rate=200):  
  print("Generating audio file for {} with {}".format(path, tts_tool))      

  subtitles = parser.parse(path)

  if tts_tool == "pyttsx3":    
    tts_engine = pyttsx3.init()
    tts_engine.setProperty('rate', rate)
    tts_engine.setProperty('voice', tts_engine.getProperty('voices')[0].id)

  audio_sum = AudioSegment.empty()   
  
  with tempfile.TemporaryDirectory() as tmpdirname:          
    print('created temporary directory', tmpdirname)            

    temp_file_path = os.path.join(tmpdirname, "temp.wav")
    prev_subtitle = None
    prev_audio_duration_ms = 0
    for subtitle in subtitles:
      if tts_tool == "pyttsx3":              
        tts_engine.save_to_file(subtitle.text, temp_file_path)
        tts_engine.runAndWait()
      else:
        val = gTTS(subtitle.text, lang='en')
        val.save(temp_file_path)

      audio_segment = AudioSegment.from_wav(temp_file_path)         

      print(subtitle.start, subtitle.text)
      
      if prev_subtitle is None:
        silence_duration_ms = time_to_ms(subtitle.start)
      else:
        silence_duration_ms = time_to_ms(subtitle.start) - time_to_ms(prev_subtitle.start) - prev_audio_duration_ms

      audio_sum = audio_sum + AudioSegment.silent(duration=silence_duration_ms) + audio_segment                   
      
      prev_subtitle = subtitle
      prev_audio_duration_ms = len(audio_segment)

    with open(os.path.splitext(path)[0] + '.wav', 'wb') as out_f:
      audio_sum.export(out_f, format='wav')      
"""
  elif tts_tool == "gtts":
    engine = gTTS('This is the first text', lang='en')
    engine.save(os.path.splitext(path)[0] + '.mp3')  
"""
if __name__ == "__main__":      
  arg_parser = argparse.ArgumentParser()
  arg_parser.add_argument("-p", "--path", help="subtitle file path", required=True)
  arg_parser.add_argument("-t", "--ttstool", help="TTs tool", choices=["pyttsx3", "gtts"], default="pyttsx3")

  args = arg_parser.parse_args()

  print(args)
  generate_audio(path=args.path, tts_tool=args.ttstool)    

