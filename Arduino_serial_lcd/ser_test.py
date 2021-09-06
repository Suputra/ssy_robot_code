import serial
import time

ser = serial.Serial('/dev/cu.usbmodem14101',9600, timeout=1)

ser.flush() #flushes the incoming serial buffer, but not necessary (useful for duplex)

while True:
    input()
    ser.write(b"0 0 1 0 1 0")