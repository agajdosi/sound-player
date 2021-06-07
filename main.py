from pydub import AudioSegment
from pydub.playback import play
from apscheduler.schedulers.background import BlockingScheduler

def Play(file, filetype):
  file = "audio/" + file
  sound = AudioSegment.from_file(file, format=filetype)
  play(sound)

sounds = [
  ["chudibranivesvobode.mp3", "mp3", 7, 00, 00],
  ["houbareni.mp3", "mp3", 7, 20, 00],
  ["bohativsechzemizbavmesekotvy.mp3", "mp3", 7, 40, 00],

  ["obcaniazvasnahradiroboti.mp3", "mp3", 8, 00, 00],
  ["nuzkyvyklidtepole.mp3", "mp3", 8, 20, 00],
  ["chesbonzbavitseutrpnechudoby.mp3", "mp3", 8, 40, 00],

  ["jsteplytvajicispotrebice.mp3", "mp3", 9, 00, 00],
  ["jehumoreskouprobyznys.mp3", "mp3", 9, 20, 00],
  ["8.mp3", "mp3", 9, 40, 00],

  ["doslanamtrpelivost.mp3", "mp3", 10, 00, 00],
  ["sikana.mp3", "mp3", 10, 20, 00],
  ["14.mp3", "mp3", 10, 40, 00],

  ["azprijdezmenasuchohlad.mp3", "mp3", 11, 00, 00],
  ["16.mp3", "mp3", 11, 20, 00],
  ["monopolybrnopraha.mp3", "mp3", 11, 40, 00],

  ["kdysankovalydeti.mp3", "mp3", 12, 00, 00],
  ["chudibranivesvobode.mp3", "mp3", 12, 20, 00],
  ["14.mp3", "mp3", 12, 40, 00],

  ["monopolybrnopraha.mp3", "mp3", 13, 00, 00],
  ["bohativsechzemizbavmesekotvy.mp3", "mp3", 13, 20, 00],
  ["obcaniazvasnahradiroboti.mp3", "mp3", 13, 40, 00],

  ["nuzkyvyklidtepole.mp3", "mp3", 14, 00, 00],
  ["kdysankovalydeti.mp3", "mp3", 14, 20, 00],
  ["jsteplytvajicispotrebice.mp3", "mp3", 14, 40, 00],

  ["jehumoreskouprobyznys.mp3", "mp3", 15, 00, 00],
  ["8.mp3", "mp3", 15, 20, 00],
  ["doslanamtrpelivost.mp3", "mp3", 15, 40, 00],

  ["sikana.mp3", "mp3", 16, 00, 00],
  ["azprijdezmenasuchohlad.mp3", "mp3", 16, 20, 00],
  ["16.mp3", "mp3", 16, 40, 00],

  ["houbareni.mp3", "mp3", 17, 00, 00],
  ["chesbonzbavitseutrpnechudoby.mp3", "mp3", 17, 20, 00],
  ["chudibranivesvobode.mp3", "mp3", 17, 40, 00],

  ["obcaniazvasnahradiroboti.mp3", "mp3", 18, 00, 00],
  ["monopolybrnopraha.mp3", "mp3", 18, 20, 00],
  ["jsteplytvajicispotrebice.mp3", "mp3", 18, 40, 00],
]

sched = BlockingScheduler()

for sound in sounds:
  sched.add_job(Play, 'cron', args=[sound[0], sound[1]], hour=sound[2], minute=sound[3])

Play("jehumoreskouprobyznys.mp3", "mp3")

sched.start()
