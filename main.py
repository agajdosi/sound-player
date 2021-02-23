import os, sys
from pydub import AudioSegment
from pydub.playback import play
from apscheduler.schedulers.background import BlockingScheduler
import git 


def Play(file):
  sound = AudioSegment.from_file(file, format="wav")
  play(sound)

def Restart():
  print("Going to restart!")
  os.execv(sys.executable, ['python'] + sys.argv)

def Update():
  g = git.cmd.Git(".")
  g.pull()

sounds = [
  ["1.wav", "22", "56", "30"],
  ["1.wav", "22", "57", "01"],
]

sched = BlockingScheduler()
sched.add_job(Restart, 'cron', minute="26")

for sound in sounds:
  #sched.add_job(Play, 'cron', args=[sound[0]], hour=sound[1], minuted=sound[2], second=sound[3])
  sched.add_job(Play, 'cron', args=[sound[0]], second=sound[3])

Update()

sched.start()
