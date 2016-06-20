#!/usr/bin/python
import I2C
import time


def main():
    i2c = I2C.i2cMaster()
    i2c.init(100,0,0)
    i2c.Start()
    i2c.WriteByte(0x46)
    i2c.WriteByte(0x10)
    i2c.Stop()
    time.sleep(0.180)
    i2c.Start()
    i2c.WriteByte(0x47)
    i2c.ReadAck()
    i2c.ReadNack()
    i2c.Stop()

if __name__ == "__main__":
    main()
