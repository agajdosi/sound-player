from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_file("1.wav", format="wav")
play(sound)

