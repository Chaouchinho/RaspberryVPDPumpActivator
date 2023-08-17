from tkinter import * 
from tkinter import messagebox
from threading import Thread
import nidoData as nidolib
import manualConfigurator as manu
import semiAutoConfigurator as semiaut
import setGpioOut as gpioOut
import numpy as np
import time
import os
import datetime
import pytz
from tzlocal import get_localzone
import dateutil.parser



debugingMode = False

if( not debugingMode):
    import luxSensor as luxSens
    import sht21 as tempHumidSens


#import setGpioOut


global wantedFont
global sensors
global elemSensors
global fenetre
global activeMode #1 Manual - #2 SemiAuto - #3 Auto
global nidoData
global nidoElems
global configuration
global threadmainAlgo


def readConfig():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + "/config/sensors.txt") as file:
        lines = [line.rstrip() for line in file]
    temp = {}
    for elem in lines:
        temp[elem.split("=")[0]] = elem.split("=")[1]
    return temp
configuration = readConfig()


def threaded_nidoData():
    global nidoData
    global nidoElems

    while True:
        nidoData = nidolib.getLastNidoValue()
        for i in range(len(nidoElems)):
            for j in range(len(nidoElems[i])):
                nidoElems[i][j]["text"] = nidoData[i][j]
                nidoElems[i][j].grid(row = i, column=j)
        time.sleep(30)

def turnOnForXSec(onDurationSec):
    global sensors
    sensors[4][1] = "On"
    gpioOut.startGPIO()
    updateData()
    if(onDurationSec > -99):
        time.sleep(onDurationSec)
        sensors[4][1] = "Off"
        gpioOut.stopGPIO()
    updateData()

def turnOff():
    global sensors
    sensors[4][1] = "Off"
    gpioOut.stopGPIO()
    updateData()
    
def threaded_mainAlgo():
    global activeMode
    global configuration
    global sensors
    while True:
        if(activeMode == 1):
            sleepingTime = int(configuration["manualFrequencySec"]) - int(configuration["manualDurationSec"])
            for i in range(0,sleepingTime):
                if(activeMode == 1):
                    time.sleep(1)

            if(activeMode ==1):
                #turnOnForXSec(int(configuration["manualDurationSec"]))
                Thread(target=turnOnForXSec, args=(int(configuration["manualDurationSec"]),)).start()
                sleepingTime = int(configuration["manualDurationSec"])
                for i in range(0,sleepingTime):
                    if(activeMode == 1):
                        time.sleep(1)

        elif(activeMode == 2):
            cuurentH = int(datetime.datetime.now().strftime('%H'))
            nextH = cuurentH + 1 
            if(int(configuration["semiAutoFrequency"+str(cuurentH)+"_" + str(nextH)]) != -1):
                if(int(configuration["semiAutoFrequency"+str(cuurentH)+"_" + str(nextH)]) > int(configuration["semiAutoDuration"+str(cuurentH)+"_" + str(nextH)])):
                    sleepingTime = int(configuration["semiAutoFrequency"+str(cuurentH)+"_" + str(nextH)]) - int(configuration["semiAutoDuration"+str(cuurentH)+"_" + str(nextH)])
                    for i in range(0,sleepingTime):
                        if(activeMode == 2):
                            time.sleep(1)
                else:
                    time.sleep(1)
                if(activeMode ==2):
                    Thread(target=turnOnForXSec, args=(int(configuration["semiAutoDuration"+str(cuurentH)+"_" + str(nextH)]),)).start()
                    sleepingTime = int(int(configuration["semiAutoDuration"+str(cuurentH)+"_" + str(nextH)]))
                    for i in range(0,sleepingTime):
                        if(activeMode == 2):
                            time.sleep(1)
            else:
                time.sleep(1)
        elif(activeMode == 4):
            Thread(target=turnOnForXSec, args=(-99,)).start()
            time.sleep(1)
        elif(activeMode == 5):
            Thread(target=turnOff).start()
            time.sleep(1)
        else:
            time.sleep(1)

def threaded_luxSensor():
    global sensors
    
    lumId = -1
    for i in range(len(sensors)):
        if(sensors[i][0].lower() == "luminosity"):
            lumId = i
            break
    
    while True:
        tempLux = round(luxSens.readAnPrintLight(),2)
        if(tempLux == -1):
            sensors[lumId][1] = "Error"
            sensors[lumId][2] = ""  
        else:
            sensors[lumId][1] = tempLux
            sensors[lumId][2] = "Lux"

        updateData()
        time.sleep(int(configuration["refreshLuxSensorMS"])/1000)

def threaded_tempAndHumiditySensor():
    global sensors
    global elemSensors

    tempId = -1
    humidityId = -1
    vpdId = -1
    for i in range(len(sensors)):
        if(sensors[i][0].lower() == "temperature"):
            tempId = i
        if(sensors[i][0].lower() == "humidity"):
            humidityId = i
        if(sensors[i][0].lower() == "vpd"):
            vpdId = i
    
    while True:
        rawTemp = tempHumidSens.getTemperature()
        rawHumi = tempHumidSens.getHumidity()
        if(rawTemp == -1):
            sensors[tempId][1] = "Error"
            sensors[tempId][2] = ""
        else:
            sensors[tempId][1] = round(rawTemp,2)
            sensors[tempId][2] = "°C"
            if(round(rawTemp,2) < int(configuration["greenTempThresholdMin"])):
                elemSensors[tempId][1].config(fg="blue")
                elemSensors[tempId][2].config(fg="blue")
            elif(round(rawTemp,2) > int(configuration["greenTempThresholdMax"])):
                elemSensors[tempId][1].config(fg="red")
                elemSensors[tempId][2].config(fg="red")
            else:
                elemSensors[tempId][1].config(fg="green")
                elemSensors[tempId][2].config(fg="green")
            

        if(rawTemp == -1):
            sensors[humidityId][1] = "Error"
            sensors[humidityId][2] = ""
        else:
            sensors[humidityId][1] = round(rawHumi,2)
            sensors[humidityId][2] = "%"
            if(round(rawHumi,2) < int(configuration["greenHumiThresholdMin"])):
                elemSensors[humidityId][1].config(fg="blue")
                elemSensors[humidityId][2].config(fg="blue")
            elif(round(rawHumi,2) > int(configuration["greenHumiThresholdMax"])):
                elemSensors[humidityId][1].config(fg="red")
                elemSensors[humidityId][2].config(fg="red")
            else:
                elemSensors[humidityId][1].config(fg="green")
                elemSensors[humidityId][2].config(fg="green")

            
        if((rawTemp != -1) and (rawHumi != -1) ):
            sensors[vpdId][1] = round(vpdfun(rawTemp,rawHumi),3)
            sensors[vpdId][2] = "kPa"
        else:
            sensors[vpdId][1] = "Error"
            sensors[vpdId][2] = ""

        updateData()
        time.sleep(int(configuration["refreshTempAndHumiditySensorMS"])/1000)

def vpdfun(T,RH):
    e_sat = 0.611 * np.exp((17.502*T)/(T + 240.97)); # kPa
    e_act = e_sat * RH/100; # kPa
    return np.round(e_sat - e_act, 2)

def setModeAuto():
    if messagebox.askyesno('Changing status', 'Are you sure you want to change the config to [Automatic]'):
        updateData()
        global activeMode
        activeMode = 3
        printConfig()
        
        ### To do Auto

def setModeManual():
    if messagebox.askyesno('Changing status', 'Are you sure you want to change the config to [Manual]'):
        updateData()
        global activeMode
        activeMode = 1
        printConfig()
        ### To do setModeManual

def setModeSemiAuto():
    if messagebox.askyesno('Changing status', 'Are you sure you want to change the config to [Semi-Automatic]'):
        global activeMode
        activeMode = 2
        printConfig()
        ### To do setModeSemiAuto

def setModeForcedOn():
    if messagebox.askyesno('Changing status', 'Are you sure you want to change the config to [ForceMode-On]'):
        global activeMode
        activeMode = 4
        printConfig()
        ### To do setModeSemiAuto

def setModeForcedOff():
    if messagebox.askyesno('Changing status', 'Are you sure you want to change the config to [ForceMode-Off]'):
        global activeMode
        activeMode = 5
        printConfig()
        ### To do setModeSemiAuto

def updateData():
    for i in range(len(elemSensors)):
        for j in range(len(elemSensors[i])):
            elemSensors[i][j]["text"] = sensors[i][j]

            if(str(sensors[i][j]).lower() == "off"):
                elemSensors[i][j].config(bg="red")
            elif(str(sensors[i][j]).lower() == "on"):
                elemSensors[i][j].config(bg="green")
            
            if(str(elemSensors[i][j] != "")):
                if((j == 0) or (j == 2)):
                    elemSensors[i][j].grid(row = i, column=j, sticky = W)
                else:
                    if(str(sensors[i][j]).lower() in ["on", "off"]):
                        elemSensors[i][j].grid(row = i, column=j, columnspan=2)
                    else:
                        elemSensors[i][j].grid(row = i, column=j)

def updateNidoData():
    for i in range(len(nidoElems)):
        for j in range(len(nidoElems[i])):
            nidoElems[i][j]["text"] = nidoData[i][j]
            if(len(str(nidoElems[i][j]["text"]) )> 25):
                nidoElems[i][j]['font'] = wantedFontSmall
            nidoElems[i][j].grid(row = i, column=j)


def printConfig():

    if( activeMode==1):
        manualMode.config(fg="green", state="disabled")
        semiAutoMode.config(fg="black", state="normal")
        AutoMode.config(fg="black", state="normal")
        ForcedModeOn.config(fg="black", state="normal")
        ForcedModeOff.config(fg="black", state="normal")
    elif( activeMode==2):
        manualMode.config(fg="black", state="normal")
        semiAutoMode.config(fg="green", state="disabled")
        AutoMode.config(fg="black", state="normal")
        ForcedModeOn.config(fg="black", state="normal")
        ForcedModeOff.config(fg="black", state="normal")
    elif( activeMode==3):
        manualMode.config(fg="black", state="normal")
        semiAutoMode.config(fg="black", state="normal")
        AutoMode.config(fg="green", state="disabled")
        ForcedModeOn.config(fg="black", state="normal")
        ForcedModeOff.config(fg="black", state="normal")
    elif( activeMode==4):
        manualMode.config(fg="black", state="normal")
        semiAutoMode.config(fg="black", state="normal")
        AutoMode.config(fg="black", state="normal")
        ForcedModeOn.config(fg="green", state="disabled")
        ForcedModeOff.config(fg="black", state="normal")
    elif( activeMode==5):
        manualMode.config(fg="black", state="normal")
        semiAutoMode.config(fg="black", state="normal")
        AutoMode.config(fg="black", state="normal")
        ForcedModeOn.config(fg="black", state="normal")
        ForcedModeOff.config(fg="green", state="disabled")
    else:
        manualMode.config(fg="black", state="normal")
        semiAutoMode.config(fg="black", state="normal")
        AutoMode.config(fg="black", state="normal")
        ForcedModeOn.config(fg="black", state="normal")
        ForcedModeOff.config(fg="black", state="normal")

    manualMode.grid(row=1, column=0, pady=10, padx=10, sticky=N+S+E+W)
    manualModeConfig.grid(row=1, column=1, pady=10, padx=10, sticky=N+S+E+W)
    semiAutoMode.grid(row=2, column=0, pady=10, padx=10,sticky=N+S+E+W)
    semiAutoModeConfig.grid(row=2, column=1, pady=10, padx=10, sticky=N+S+E+W)
    AutoMode.grid(row=3, column=0, pady=10, padx=10,sticky=N+S+E+W)
    ForcedModeOn.grid(row=4, column=0, pady=10, padx=10,sticky=N+S+E+W)
    ForcedModeOff.grid(row=4, column=1, pady=10, padx=10,sticky=N+S+E+W)


wantedFont =("Google Sans,arial,sans-serif", 10)
wantedFontSmall =("Google Sans,arial,sans-serif", 5)
wantedFontBold =("Google Sans,arial,sans-serif", 10, "bold")


sensors = [ ["Luminosity",-1,"Lux"],
            ["Temperature",20,"°C"],
            ["Humidity",35,"%"],
            ["VPD",1.2,"kPa"],
            ["Output", "Off",""] ]  
elemSensors = []

nidoData = nidolib.getLastNidoValue()
nidoElems = []

activeMode = 3

fenetre = Tk()

fenetre['bg']='white'


frameNidoData = Frame(fenetre, borderwidth=2, relief=GROOVE)
titreFrameNidoData = Label(frameNidoData, text="Nido Data", font=wantedFontBold).grid(row=0, column=0,padx=50, pady=10)
sensorNidoDataFrame = Frame(frameNidoData, borderwidth=2, relief=GROOVE)
sensorNidoDataFrame.grid(row = 1, column=0)
for i in range(len(nidoData)):
    nidoElems.append([])
    for j in range(len(nidoData[i])):
        padXcalc = 0
        if(j==0):
            padXcalc = 30
        nidoElems[i].append(Label(sensorNidoDataFrame, 
                                    text=nidoData[i][j],  
                                    font=wantedFont, 
                                    anchor='w', 
                                    justify="left", 
                                    padx=padXcalc, 
                                    pady=5) )

frameData = Frame(fenetre, borderwidth=2, relief=GROOVE)
titreFrameData = Label(frameData, text="Sensors Data", font=wantedFontBold).grid(row=0, column=0,padx=50, pady=10)
sensorDataFrame = Frame(frameData, borderwidth=2, relief=GROOVE)
sensorDataFrame.grid(row = 1, column=0, sticky="nsew")
for i in range(len(sensors)):
    elemSensors.append([])
    for j in range(len(sensors[i])):
        padXcalc = 0
        if(j==0):
            padXcalc = 30
        elemSensors[i].append(Label(sensorDataFrame, 
                                    text=sensors[i][j],  
                                    font=wantedFont, 
                                    anchor='w', 
                                    justify="left", 
                                    padx=padXcalc, 
                                    pady=5) )



frameConfig = Frame(fenetre, borderwidth=2, relief=GROOVE)
titreFrameConfig = Label(frameConfig, text="Config", font=wantedFontBold).grid(row=0, column=0, padx=50, pady=10, columnspan=2)
manualMode = Button(frameConfig, text="Manual Mode", borderwidth=4, font=wantedFont, command=setModeManual, disabledforeground="green")
manualModeConfig = Button(frameConfig, text="Config", borderwidth=4, font=wantedFont, command=manu.startManuConf, disabledforeground="green")
semiAutoMode = Button(frameConfig, text="Semi-Auto Mode", borderwidth=4, font=wantedFont, command=setModeSemiAuto, disabledforeground="green")
semiAutoModeConfig = Button(frameConfig, text="Config", borderwidth=4, font=wantedFont, command=semiaut.startSemiAutConf, disabledforeground="green")
AutoMode = Button(frameConfig, text="Automatic Mode", borderwidth=4, font=wantedFont, command=setModeAuto, disabledforeground="green")
ForcedModeOn = Button(frameConfig, text="Forced Mode On", borderwidth=4, font=wantedFont, command=setModeForcedOn, disabledforeground="green")
ForcedModeOff = Button(frameConfig, text="Forced Mode Off", borderwidth=4, font=wantedFont, command=setModeForcedOff, disabledforeground="green")



frameNidoData.grid(row = 0, column=0, padx=10, sticky="nsew")
frameData.grid(row = 0, column=1, padx=10, sticky="nsew")
frameConfig.grid(row = 0, column=2, padx=10, sticky="nsew")



updateData()
updateNidoData()
printConfig()

if(not debugingMode):
    threadNido = Thread(target = threaded_nidoData)
    threadNido.start()

    threadLux = Thread(target = threaded_luxSensor)
    threadLux.start()

    threadTempHumid = Thread(target = threaded_tempAndHumiditySensor)
    threadTempHumid.start()

threadmainAlgo = Thread(target = threaded_mainAlgo)
threadmainAlgo.start()

fenetre.geometry('800x420')

fenetre.mainloop()
gpioOut.cleanup()
