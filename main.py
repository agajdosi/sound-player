import os, sys
from pydub import AudioSegment
from pydub.playback import play
from apscheduler.schedulers.background import BlockingScheduler
import git 


def Play(file):
  sound = AudioSegment.from_file(file, format="wav")
  play(sound)

def Update():
  print("Going to update!")
  g = git.cmd.Git(".")
  g.pull()
  print("Going to restart!")
  os.execv(sys.executable, ['python'] + sys.argv)

sounds = [
  ["1.wav", 22, 56, 00],
  ["1.wav", 22, 57, 15],
  ["1.wav", 22, 57, 30],
  ["1.wav", 22, 57, 45],
]

sched = BlockingScheduler()
sched.add_job(Update, 'cron', hour=4, minute="35")

for sound in sounds:
  #sched.add_job(Play, 'cron', args=[sound[0]], hour=sound[1], minuted=sound[2], second=sound[3])
  sched.add_job(Play, 'cron', args=[sound[0]], second=sound[3])

sched.start()
