import smbus
import time

device = 0x23

bus = smbus.SMBus(1)
counter = 0

def convertToNumber(data):
    return ((data[1] + (256 * data[0])) /1.2)

def readLight():
    data = bus.read_block_data(device, 0x20)
    return convertToNumber(data)

while True:
    print("Light level: " + str(readLight()))
    time.sleep(0.5)
    
 