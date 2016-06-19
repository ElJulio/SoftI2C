#!/usr/bin/python

#Soft implementation of an i2c Master

import time
import RPi.GPIO as GPIO

class i2cMaster:
    bitrate = -1
    int_clk = -1

    SDA = 1 #default sda
    SCL = 2 #default scl

    def tick():
        time.sleep(self.int_clk)

    def init(bitrate,SDAPIN,SCLPIN):
        if(SDAPIN != SCLPIN):
            self.SCL = SCLPIN
            self.SDA = SDAPIN

        else
            print "SDA = GPIO1  SCL = GPIO2"

        #configer SCL as output
        GPIO.setup(SCL, GPIO.OUT)

        if bitrate == 100:
            self.int_clk = 0.0000025
        elif bitrate == 400:
            self.int_clk =
        elif bitrate == 1000:

        elif bitrate == 3200:

    def Start():
        #SCL
        #  ______
        #  |     |______
        #SDA
        #  ___
        #  |  |_________

        GPIO.setup(SDA, GPIO.OUT) #cnfigure SDA as output

        GPIO.output(SCL, GPIO.HIGH)
        GPIO.output(SDA, GPIO.HIGH)
        tick()
        GPIO.output(SDA, GPIO.LOW)
        tick()
        GPIO.output(SCL, GPIO.LOW)
        tick()
        tick()


    def ReadAck():
        tick()

    def ReadNack():
        tick()

    def Write():
        tick()

    def Stop():
        tick()
