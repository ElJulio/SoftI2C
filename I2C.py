#!/usr/bin/python

#Soft implementation of an i2c Master

import time
import RPi.GPIO as GPIO

class i2cMaster:

    int_clk = -1

    SDA = 17 #default sda
    SCL = 27 #default scl

    def tick(self):
        time.sleep(self.int_clk)

    def init(self,bitrate,SDAPIN,SCLPIN):
        if(SDAPIN != SCLPIN):
            self.SCL = SCLPIN
            self.SDA = SDAPIN

        else:
            print "SDA = GPIO"+str(self.SDA)+"  SCL = GPIO"+str(self.SCL)

        #configer SCL as output
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.SCL, GPIO.OUT)

        if bitrate == 100:
            self.int_clk = 0.0000025
        elif bitrate == 400:
            self.int_clk = 0.000000625
        elif bitrate == 1000:
            self.int_clk = 1
        elif bitrate == 3200:
            self.int_clk = 1

    def Start(self):
        #SCL
        #  ______
        #  |     |______
        #SDA
        #  ___
        #  |  |_________

        GPIO.setup(self.SDA, GPIO.OUT) #cnfigure SDA as output

        GPIO.output(self.SCL, GPIO.HIGH)
        GPIO.output(self.SDA, GPIO.HIGH)
        self.tick()
        GPIO.output(self.SDA, GPIO.LOW)
        self.tick()
        GPIO.output(self.SCL, GPIO.LOW)

        self.tick()
        self.tick()


    def ReadAck(self):
        self.tick()

    def ReadNack(self):
        self.tick()

    def Write(self):
        self.tick()

    def Stop(self):
        self.tick()
