#!/usr/bin/python
import I2C.py

def main():
    i2c = i2cMaster()
    i2c.init(100,0,0)
    i2c.Start()

if __name__ == "__main__":
    main()
