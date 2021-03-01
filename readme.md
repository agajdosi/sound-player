### Create the service

Copy `raspi/sound-player.service` into `/etc/systemd/system` as root, for example:

`sudo cp sound-player.service /etc/systemd/system/sound-player.service`

Once this has been copied, you can attempt to start the service using the following command:

`sudo systemctl start sound-player.service`

Stop it using following command:

`sudo systemctl stop sound-player.service`

When you are happy that this starts and stops your app, you can have it start automatically on reboot by using this command:

`sudo systemctl enable myscript.service`
