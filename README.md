# Halloween-Control
Python code for the Pi to trigger a video projector for a singing pumpkins
Halloween display. This code plays two files which project heads onto 3 pumpkins.
The first is Monster Bash and the second is Thriller. These can be bought off the internet
or created by yourself. I chose the former so I can't include the files into this 
repository. The video is triggered from an IR detector. 
I have also added code to operate a couple of relays that can be used to trigger a fog 
machine or other devices. I had a fog machine on pin 17 and a talking Pirate head on pin 23. 
The fog machine and pirate will operate randomly during a 15 minute period even if no video has not been played.
The code logs the time the video was played and the fog machine, pirate have turned on.
The code can be run from a ssh session or made to run at boot time by adding it to  the cron jobs
table. There are web articles on how to do this. Search crontab -e.


For the hardware setup you need:

1) A Raspberry Pi with an OS and the Adafruit GPIO libraries installed. 

2) The IR detector is connected to Pin 18

3) Relay board that is connected to Pin 17. Both IR detector and relay will require
5V and ground. I used some small relay boards designed for the Arduino and had to 
connect the relay to 3.3v to get it to work correctly. Also a 0 turns the relay on and a 1
turns it off. Using the PowerTail from Adafruit works fine connected to the 5V line.
I updated the relay board to a board with 4 relays and added control of a second relay via pin 23.

4) An animation of  singing pumpkins synced to an audio track.

5) A HDMI projector. I use a small pocket laser  and configure the Pi for VGA. Sound comes
out of the HDMI/VGA adaptor and is plugged into some cheap PC speakers.

6) Fog machine and any other animated electronic device you want to activate.

7) Don't forget the pumpkins. Real or plastic. 
