import os, sys
from pydub import AudioSegment
from pydub.playback import play
from apscheduler.schedulers.background import BlockingScheduler
import git 


def Play(file, filetype):
  sound = AudioSegment.from_file(file, format=filetype)
  play(sound)

def Update():
  print("Going to update!")
  g = git.cmd.Git(".")
  g.pull()
  print("Going to restart!")
  os.execv(sys.executable, ['python'] + sys.argv)

sounds = [
  ["1.wav", "wav", 22, 56, 00],
  ["slogan1.mp3", "mp3", 22, 57, 15],
  ["slogan2.mp3", "mp3", 22, 57, 45],
]

sched = BlockingScheduler()
sched.add_job(Update, 'cron', hour=14, minute="15")

for sound in sounds:
  sched.add_job(Play, 'cron', args=[sound[0], sound[1]], second=sound[4])

sched.start()
