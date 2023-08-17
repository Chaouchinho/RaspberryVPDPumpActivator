from tkinter import * 
from tkinter import messagebox
import os


def readConfigManual():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + "/config/sensors.txt") as file:
        lines = [line.rstrip() for line in file]
    temp = {}
    for elem in lines:
        temp[elem.split("=")[0]] = elem.split("=")[1]
    return temp

def saveDataManual():
    global configurationManual
    global fenetreConfigManual
    global entryFrequency
    global entryDuration
    
    dir_path = os.path.dirname(os.path.realpath(__file__))

    configurationManual["manualFrequencySec"] = entryFrequency.get()
    configurationManual["manualDurationSec"] = entryDuration.get()
    keysList = list(configurationManual.keys())

    with open(dir_path + "/config/sensors.txt", 'w+') as f:
        for key in keysList:
            f.write(key + "=" + configurationManual[key]+"\n")

    messagebox.showinfo(title="Data Saved", message="Your data has been saved, it will be effective on next reboot")
    fenetreConfigManual.destroy()

global configurationManual
global fenetreConfigManual
global entryFrequency
global entryDuration

def startManuConf():
    global configurationManual
    global fenetreConfigManual
    global entryFrequency
    global entryDuration

    configurationManual = readConfigManual()
    
    fenetreConfigManual = Tk()

    labelTitleConfigManual = Label(fenetreConfigManual, text="Manual Configurator")

    labelFrequency = Label(fenetreConfigManual, text="Frequency (seconds)")
    entryFrequency_text = StringVar()
    entryFrequency_text.set("")
    entryFrequency = Entry(fenetreConfigManual, textvariable=entryFrequency_text, width=15)
    entryFrequency.insert(END,configurationManual["manualFrequencySec"])

    labelDuration = Label(fenetreConfigManual, text="Duration (seconds)")
    entryDuration_text = StringVar()
    entryDuration_text.set("")
    
    entryDuration = Entry(fenetreConfigManual, textvariable=entryDuration_text, width=15)
    entryDuration.insert(END,configurationManual["manualDurationSec"])
    exempleManualConfig = Label(fenetreConfigManual, text="Exemple : Every " + configurationManual["manualFrequencySec"] + " seconds turn ON the\npump for a duration of "+configurationManual["manualDurationSec"]+" seconds")

    saveButtonManual = Button(fenetreConfigManual, text="Save", command=saveDataManual)
    cancelButtonManual = Button(fenetreConfigManual, text="Cancel", command=fenetreConfigManual.destroy)

    labelTitleConfigManual.grid(row=0, column=0, columnspan=2, pady=10)
    labelFrequency.grid(row=1, column=0, pady=10)
    entryFrequency.grid(row=1, column=1, pady=10)
    labelDuration.grid(row=2, column=0, pady=10)
    entryDuration.grid(row=2, column=1, pady=10)
    exempleManualConfig.grid(row=3, column=0, columnspan=2, pady=10)

    saveButtonManual.grid(row=4, column=0, pady=10)
    cancelButtonManual.grid(row=4, column=1, pady=10)

    fenetreConfigManual.mainloop()

