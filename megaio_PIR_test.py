import RPi.GPIO as GPIO
import time
import os
import random
from random import randrange
import megaio

valid = str("")

PIR=17                                               # Set GPIO 18 as input for PIR trigger
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR,GPIO.IN)
megaio.set_relays(0,0x00)



def Relay_step():

	for x in range (1,9):
	   megaio.set_relay(0,x,1)
           print("Relay", x)
           time.sleep(1)
        for x in range (1,9):
           megaio.set_relay(0,x,0)
           time.sleep(1)




def Relay(mode):

        if mode == 0:
	    megaio.set_relay(0,2,mode)
            print("setting mode =", mode)
        if mode == 1:
            megaio.set_relay(0,2,mode)
            print("setting mode =", mode)
        print("In Relay module",mode)
#        megaio.set_relays(0,0xFF)
        time.sleep(2)
#        megaio.set_relays(0,0x00)

# Testing for MegaIO software and then hardware.

valid_board = os.popen("megaio 0 board").read()
valid_software = os.popen("megaio -v").read()


P  = str("MegaIO ")
if P not  in valid_software :
	print("Need MegaIO software installing")
        exit()
P = str("MegaIO Hardware version")

if P not in valid_board :
        print("Need MegaIO Board installing")
        exit()

# If MegaIO correctly installed continue...

while True:
	if (GPIO.input(PIR) == True):
		print("Triggered")
                megaio.set_relay(0,8,1)
                time.sleep(10)
                megaio.set_relay(0,1,1)
                time.sleep(10)
                megaio.set_relay(0,8,0)
                megaio.set_relay(0,1,0)
                time.sleep(2)
                megaio.set_relays(0,0xFF)
                time.sleep(2)
                megaio.set_relays(0,0x00)
                print("Exiting trigger")
        time.sleep(5)
        Relay(1)
        print("Looping")
        Relay(0)
        time.sleep(2)
        Relay_step()

