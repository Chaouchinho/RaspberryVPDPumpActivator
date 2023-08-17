import RPi.GPIO as GPIO
from time import sleep
import os 



global pinNb
global configGPIOOut

def readConfigGPIO():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + "/config/gpio.txt") as file:
        lines = [line.rstrip() for line in file]
    temp = {}
    for elem in lines:
        temp[elem.split("=")[0]] = elem.split("=")[1]
    return temp

configGPIOOut = readConfigGPIO()
pinNb = int(configGPIOOut["relayGPIO"])


def setOutputOnForXSec(durationSec):
    global pinNb
    GPIO.setmode(GPIO.BOARD)
    try:
        GPIO.setup(pinNb, GPIO.OUT)
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)
    except:
        print("Error cleaning up GPIO")
    GPIO.setup(pinNb, GPIO.OUT)
    GPIO.output(pinNb, GPIO.HIGH)
    sleep(durationSec)
    GPIO.output(pinNb, GPIO.LOW)
    GPIO.cleanup()


def stopGPIO():
    global pinNb
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pinNb, GPIO.OUT)
    GPIO.output(pinNb,GPIO.LOW)
    print("Off")

def cleanup():
    GPIO.setup(pinNb, GPIO.OUT)
    GPIO.cleanup()
    
    
def startGPIO():
    global pinNb
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pinNb, GPIO.OUT)
    GPIO.output(pinNb,GPIO.HIGH)
    print("On")
    


#GPIO.cleanup()

