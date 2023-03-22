# subtitle-to-audio
This script generates an audio file (.wav) from a .srt file with timings. There can be unwanted shifts in the final audio if a time interval of a text is not adequate for dubbing. 
# Table of Contents

# Dependencies
* [pydub](https://github.com/jiaaro/pydub): Used for audio segment manipulations.
* [pysub-parser](https://pypi.org/project/pysub-parser/): Used for parsing .srt files.
* [pyttsx3](https://github.com/nateshmbhat/pyttsx3): An offline text-to-speech library used for dubbing.

# Installation
Clone the repository and than install the requirements with the following command.
```bash
pip install -r requirements.txt
```
# Usage
Here is an example usage. with command line options.
```
python subtitle_to_audio.py -p test/test.srt -r 120 -v 1
```
