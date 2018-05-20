# From https://www.raspberrypi.org/forums/viewtopic.php?f=32&t=88557
# Modified October 2015 to play alternate files. Also createsopens a file 
# to log timestamps and files played for debugging.
# If video is playing cntl-C will halt it and the program will wait for the next trigger.
# If you hit cntrl-C while wating for a trigger it will end the program.
#
# 
#
# Dave Robinson 11/1/15

# Added relay support 
# Dave Robinson  6/22/16


# Made a Fog function that accepts on/off and duration. Never really send an off as duration
# is used to turn off the machine.
# Fixed the file open issue (a+ creates the file if it isn't there and appends if it is! So simple!
# Dave Robinson 6/23/16



# Adding Meagio card - 8 relays!!  
# To do:
# change code relay  from gpio calls to medaio calls. It will still read in the PIR from the GPIO pin
# but all relay commands will be variations of the list below.

# Here are the commands to use the Megaio board. Must include the megaio.py file so need to add to github.
# >>> import megaio	#import libraries
# >>> megaio.set_relay(0, 2, 1)	#turn on relay 2 on stack level 0
# >>> megaio.set_relay(0, 2, 0)	#turn off relay 2 on stack level 0
# >>> megaio.set_relays(0,0xFF)	#turn on all relays
# >>> megaio.set_relays(0,0x00)	#turn off all relays
# Dave Robinson 5/17/18

# Added mega code based on standalone tetsing of PIR and the board. Had to change logic on fog machine.
# Pirate is on relay 2 and Fog is on relay 8...

#  Here's a link to megaio https://www.sequentmicrosystems.com/megaio/MEGA-IO-UsersGuide.pdf
# will need to compile on the Pi to support the board.




import RPi.GPIO as GPIO
import time
import os
import random
from random import randrange
import megaio     # New megaio library


PIR=18                                               # Set GPIO 18 as input for PIR trigger
POWER=17					     # Set GPIO 17 as output for relay.
Pirate=23
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR,GPIO.IN)
GPIO.setup(POWER,GPIO.OUT)
GPIO.setup(Pirate,GPIO.OUT)
Loop_count= 10
File_to_play = 1				     # Flag to alternate files to be played
now = time.localtime(time.time())
year, month, day, hour, minute, second, weekday, yearday, daylight = now
old_minute = minute + randrange(0,5,1)



def MyLog(logData):                                  # My logging function
        
        
        log.write(time.asctime( time.localtime(time.time()) ))   # Add time stamp
	
        log.write(logData)                           # Add padded in text - the cuurent playig/ending file
        log.flush()                                  # Needed to make sure file gets updated
#End of Log function
def Pirate_Talk():

            megaio.set_relay(0, 2, 1)               # Pirate on Relay 2
           # GPIO.output(Pirate,0)
            time.sleep(1)
           # GPIO.output(Pirate,1)
            megaio.set_relay(0, 2, 0)
            MyLog(" Pirate Talking!\n")
#End of Pirate

def Fog(sw_mode, Dur):                               # Fog function turns on fog machine for passed in "Dur"
                                                     # Turns off fog machine after "Dur" seconds. 
	                                                 # Switching modes due to megaio board.
            InFog=True
#            GPIO.output(Pirate,0)
#            time.sleep(1)
#            GPIO.output(Pirate,1)
#           GPIO.output(POWER,sw_mode)
        megaio.set_relay(0,8,sw_mode)
	    time.sleep(Dur)
	    if sw_mode == 0:
                FogText = " Fog Machine on for " + str(Dur) + " seconds.\n"
                MyLog(FogText)
	    if sw_mode == 1:
	        MyLog(" Fog machine off.\n")
	        megaio.set_relay(0,8,0)
#	    GPIO.output(POWER,1)
            InFog=False	        
#End of Fog function

os.system("clear")                                   # Clear Screen   
os.system("setterm -cursor off")                     # Hide Cursor  
log = open("song.log", "a+")			     # Open a file for logging. 
#Loop_count = 0

log.seek(0, 2)                                       # This will append new entries

HeaderText = "Starting Log at " + time.asctime( time.localtime(time.time()) ) + "\n"
log.write(HeaderText)
# log.flush()					     # Needed to make sure log file gets updated 
text_message= " Fog Random start time: " + str(old_minute) + "\n"
MyLog(text_message)
Fog(1,0)                                             # Make sure fog machine is off
while True:                                          # Looping until press Ctrl-C to break
  if (GPIO.input(PIR)==True):                        # Check PIR trigger
  
        Pirate_Talk()
        time.sleep(1)
        Fog(0, 5)                                    # Call for fog!!
    

        if File_to_play == 1:
	   MyLog(" Playing Pumpkin.\n")
           os.system("omxplayer Singing_Pumpkins.mp4 -b > /dev/null")
#        Python shell method. Makes sure console data  goes  to dev/null while playing  video
	   MyLog(" Pumpkin ended.\n")
	   Fog(0, 10)
	     
           File_to_play = 2                           # Flip to next file
           while (GPIO.input(PIR) == True): time.sleep(.2)
        else: 
          MyLog(" Playing Thriller\n")
          os.system("omxplayer Thriller-5Frames.mp4 -b > /dev/null ")         
          MyLog(" Thriller ended.\n")
          Fog(0, 10)

          File_to_play = 1                           # Flip to first file
          while (GPIO.input(PIR) == True): time.sleep(.2)  
        while (GPIO.input(PIR) == True):
         
#         log.flush() 				     # Needed this extra flush
         time.sleep(.2);                             # Loop until PIR is cleared

  now = time.localtime(time.time())
  year, month, day, hour, minute, second, weekday, yearday, daylight = now
  
  if minute <= 57:
     if minute > old_minute :
	old_minute = minute + randrange(1,15,1)
	timer_text = " New delay time < 57 @" + str(old_minute) + " minutes. \n"
        MyLog(timer_text)
        Pirate_Talk()
        Fog(0,randrange(5,15,1))
        if old_minute > 60 :
           old_minute =58
           timer_text = " New delay time > 60 @" + str(old_minute) + " minutes. \n"
           MyLog(timer_text)
        if minute == 59:
           old_minute = randrange(1,15,1)
           timer_text = " New delay time at the hour @" + str(old_minute) + " minutes. \n"
           MyLog(timer_text)
  else:
    old_minute = randrange(0,15,1)



# End of Program.

