
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


import RPi.GPIO as GPIO
import time
import os


PIR=18                                               # Set GPIO 18 as input for PIR trigger
POWER=17					     # Set GPIO 17 as output for relay.
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR,GPIO.IN)
GPIO.setup(POWER,GPIO.OUT)

File_to_play = 1				     # Flag to alternate files to be played





def MyLog(logData):                                  # My logging function
        
        
        log.write(time.asctime( time.localtime(time.time()) ))   # Add time stamp
	
        log.write(logData)                           # Add padded in text - the cuurent playig/ending file
        log.flush()                                  # Needed to make sure file gets updated
#End of Log function

def Fog(sw_mode, Dur):                               # Fog function turn s on fog mahie for passed in "Dur"
                                                     # Turns off fog machine after "Dur" seconds. 
	    InFog=True
            GPIO.output(POWER,sw_mode)
	    time.sleep(Dur)
	    if sw_mode == 0:
                FogText = " Fog Machine on for " + str(Dur) + " seconds.\n"
                MyLog(FogText)
	    if sw_mode == 1:
	        MyLog(" Fog machine off.\n")
	    GPIO.output(POWER,1)
            InFog=False	        
#End of Fog function

os.system("clear")                                   # Clear Screen   
os.system("setterm -cursor off")                     # Hide Cursor  
log = open("song.log", "a+")			     # Open a file for logging. 


log.seek(0, 2)                                       # This will append new entries

HeaderText = "Starting Log at " + time.asctime( time.localtime(time.time()) ) + "\n"
log.write(HeaderText)
# log.flush()					     # Needed to make sure log file gets updated 

Fog(1,0)                                             # Makre sure fog machine is off
while True:                                          # Looping until press Ctrl-C to break
  if (GPIO.input(PIR)==True):                        # Check PIR trigger
  

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
# End of Program.

