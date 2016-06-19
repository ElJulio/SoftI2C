#!/usr/bin/python
import I2C

def main():
    i2c = I2C.i2cMaster()
    i2c.init(100,0,0)
    i2c.Start()
    i2c.WriteByte(0xAA)
    i2c.Stop()

if __name__ == "__main__":
    main()
