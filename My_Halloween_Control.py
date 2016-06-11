
# From https://www.raspberrypi.org/forums/viewtopic.php?f=32&t=88557
# Modified October 2015 to play alternate files. Also opened a file 
# to log timestamps and files played for debugging. Yu will have to create the file song.log first.
# If video is playing cntl-C will halt it and the program will wait for the next trigger.
# If you hit cntrl-C while wating for a trigger it will end the program.
#
# 
#
# Dave Robinson 11/1/15
#


import RPi.GPIO as GPIO
import time
import os


PIR=18                                               # Set GPIO 18 as input for PIR trigger
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR,GPIO.IN)
File_to_play = 1				     # Flag to alternate files to be played

def MyLog(logData):                                  # My logging function
        log.write(time.asctime( time.localtime(time.time()) ))   # Add time stamp
	log.write(logData)                           # Add padded in text - the cuurent playig/ending file
        log.flush()                                  # Needed to make sure file gets updated
#End of function

os.system("clear")                                   # Clear Screen   
os.system("setterm -cursor off")                     # Hide Cursor  
log = open("song.log", "rw+")			     # Open a file for logging. Must create  a blank file first
						     # in the same directory as this pyhton file called "song.log"


log.seek(0, 2)                                       # This will append new entries
log.write("Starting Log at ")                        # Creates a header so not using MyLog() for this.
log.write(time.asctime( time.localtime(time.time()) )) # Current time
log.write("\n")
log.flush()					     # Needed to make sure log file gets updated 

while True:                                          # Looping until press Ctrl-C to break
  if (GPIO.input(PIR)==True):                        # Check PIR trigger
    

      if File_to_play == 1:
	 MyLog(" Playing Pumpkin.\n")
         os.system("omxplayer Singing_Pumpkins.mp4 -b > /dev/null")
#        Python shell method. Makes sure console data  goes  to dev/null while playing  video
	 MyLog(" Pumpkin ended.\n")
         File_to_play = 2                           # Flip to next file
         while (GPIO.input(PIR) == True): time.sleep(.2)
      else: 
         MyLog(" Playing Thriller\n")
         os.system("omxplayer Thriller-5Frames.mp4 -b > /dev/null ")         
         MyLog(" Thriller ended.\n")
         File_to_play = 1                          # Flip to first file
         while (GPIO.input(PIR) == True): time.sleep(.2)  
      while (GPIO.input(PIR) == True):
         
#         log.flush() 				  # Needed this extra flush
         time.sleep(.2);                          # Loop until PIR is cleared
# End of Program.