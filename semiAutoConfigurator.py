from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
import os


def readConfigSemiAuto():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + "/config/sensors.txt") as file:
        lines = [line.rstrip() for line in file]
    temp = {}
    for elem in lines:
        temp[elem.split("=")[0]] = elem.split("=")[1]
    return temp

def saveDataSemiAuto():
    global configurationSemiAuto
    global fenetreConfigSemiAuto
    global entryFrequency
    global entryDuration
    
    dir_path = os.path.dirname(os.path.realpath(__file__))

    configurationSemiAuto["semiAutoFrequency0_1"] = entrySemiAutoFrequency0_1.get()
    configurationSemiAuto["semiAutoFrequency1_2"] = entrySemiAutoFrequency1_2.get()
    configurationSemiAuto["semiAutoFrequency2_3"] = entrySemiAutoFrequency2_3.get()
    configurationSemiAuto["semiAutoFrequency3_4"] = entrySemiAutoFrequency3_4.get()
    configurationSemiAuto["semiAutoFrequency4_5"] = entrySemiAutoFrequency4_5.get()
    configurationSemiAuto["semiAutoFrequency5_6"] = entrySemiAutoFrequency5_6.get()
    configurationSemiAuto["semiAutoFrequency6_7"] = entrySemiAutoFrequency6_7.get()
    configurationSemiAuto["semiAutoFrequency7_8"] = entrySemiAutoFrequency7_8.get()
    configurationSemiAuto["semiAutoFrequency8_9"] = entrySemiAutoFrequency8_9.get()
    configurationSemiAuto["semiAutoFrequency9_10"] = entrySemiAutoFrequency9_10.get()
    configurationSemiAuto["semiAutoFrequency10_11"] = entrySemiAutoFrequency10_11.get()
    configurationSemiAuto["semiAutoFrequency11_12"] = entrySemiAutoFrequency11_12.get()
    configurationSemiAuto["semiAutoFrequency12_13"] = entrySemiAutoFrequency12_13.get()
    configurationSemiAuto["semiAutoFrequency13_14"] = entrySemiAutoFrequency13_14.get()
    configurationSemiAuto["semiAutoFrequency14_15"] = entrySemiAutoFrequency14_15.get()
    configurationSemiAuto["semiAutoFrequency15_16"] = entrySemiAutoFrequency15_16.get()
    configurationSemiAuto["semiAutoFrequency16_17"] = entrySemiAutoFrequency16_17.get()
    configurationSemiAuto["semiAutoFrequency17_18"] = entrySemiAutoFrequency17_18.get()
    configurationSemiAuto["semiAutoFrequency18_19"] = entrySemiAutoFrequency18_19.get()
    configurationSemiAuto["semiAutoFrequency19_20"] = entrySemiAutoFrequency19_20.get()
    configurationSemiAuto["semiAutoFrequency20_21"] = entrySemiAutoFrequency20_21.get()
    configurationSemiAuto["semiAutoFrequency21_22"] = entrySemiAutoFrequency21_22.get()
    configurationSemiAuto["semiAutoFrequency22_23"] = entrySemiAutoFrequency22_23.get()
    configurationSemiAuto["semiAutoFrequency23_24"] = entrySemiAutoFrequency23_24.get()
    configurationSemiAuto["semiAutoDuration0_1"] = entrySemiAutoDuration0_1.get()
    configurationSemiAuto["semiAutoDuration1_2"] = entrySemiAutoDuration1_2.get()
    configurationSemiAuto["semiAutoDuration2_3"] = entrySemiAutoDuration2_3.get()
    configurationSemiAuto["semiAutoDuration3_4"] = entrySemiAutoDuration3_4.get()
    configurationSemiAuto["semiAutoDuration4_5"] = entrySemiAutoDuration4_5.get()
    configurationSemiAuto["semiAutoDuration5_6"] = entrySemiAutoDuration5_6.get()
    configurationSemiAuto["semiAutoDuration6_7"] = entrySemiAutoDuration6_7.get()
    configurationSemiAuto["semiAutoDuration7_8"] = entrySemiAutoDuration7_8.get()
    configurationSemiAuto["semiAutoDuration8_9"] = entrySemiAutoDuration8_9.get()
    configurationSemiAuto["semiAutoDuration9_10"] = entrySemiAutoDuration9_10.get()
    configurationSemiAuto["semiAutoDuration10_11"] = entrySemiAutoDuration10_11.get()
    configurationSemiAuto["semiAutoDuration11_12"] = entrySemiAutoDuration11_12.get()
    configurationSemiAuto["semiAutoDuration12_13"] = entrySemiAutoDuration12_13.get()
    configurationSemiAuto["semiAutoDuration13_14"] = entrySemiAutoDuration13_14.get()
    configurationSemiAuto["semiAutoDuration14_15"] = entrySemiAutoDuration14_15.get()
    configurationSemiAuto["semiAutoDuration15_16"] = entrySemiAutoDuration15_16.get()
    configurationSemiAuto["semiAutoDuration16_17"] = entrySemiAutoDuration16_17.get()
    configurationSemiAuto["semiAutoDuration17_18"] = entrySemiAutoDuration17_18.get()
    configurationSemiAuto["semiAutoDuration18_19"] = entrySemiAutoDuration18_19.get()
    configurationSemiAuto["semiAutoDuration19_20"] = entrySemiAutoDuration19_20.get()
    configurationSemiAuto["semiAutoDuration20_21"] = entrySemiAutoDuration20_21.get()
    configurationSemiAuto["semiAutoDuration21_22"] = entrySemiAutoDuration21_22.get()
    configurationSemiAuto["semiAutoDuration22_23"] = entrySemiAutoDuration22_23.get()
    configurationSemiAuto["semiAutoDuration23_24"] = entrySemiAutoDuration23_24.get()

    keysList = list(configurationSemiAuto.keys())

    with open(dir_path + "/config/sensors.txt", 'w+') as f:
        for key in keysList:
            f.write(key + "=" + configurationSemiAuto[key]+"\n")

    messagebox.showinfo(title="Data Saved", message="Your data has been saved, it will be effective on next reboot")
    fenetreConfigSemiAuto.destroy()


global entrySemiAutoFrequency0_1
global entrySemiAutoFrequency1_2
global entrySemiAutoFrequency2_3
global entrySemiAutoFrequency3_4
global entrySemiAutoFrequency4_5
global entrySemiAutoFrequency5_6
global entrySemiAutoFrequency6_7
global entrySemiAutoFrequency7_8
global entrySemiAutoFrequency8_9
global entrySemiAutoFrequency9_10
global entrySemiAutoFrequency10_11
global entrySemiAutoFrequency11_12
global entrySemiAutoFrequency12_13
global entrySemiAutoFrequency13_14
global entrySemiAutoFrequency14_15
global entrySemiAutoFrequency15_16
global entrySemiAutoFrequency16_17
global entrySemiAutoFrequency17_18
global entrySemiAutoFrequency18_19
global entrySemiAutoFrequency19_20
global entrySemiAutoFrequency20_21
global entrySemiAutoFrequency21_22
global entrySemiAutoFrequency22_23
global entrySemiAutoFrequency23_24
global entrySemiAutoDuration0_1
global entrySemiAutoDuration1_2
global entrySemiAutoDuration2_3
global entrySemiAutoDuration3_4
global entrySemiAutoDuration4_5
global entrySemiAutoDuration5_6
global entrySemiAutoDuration6_7
global entrySemiAutoDuration7_8
global entrySemiAutoDuration8_9
global entrySemiAutoDuration9_10
global entrySemiAutoDuration10_11
global entrySemiAutoDuration11_12
global entrySemiAutoDuration12_13
global entrySemiAutoDuration13_14
global entrySemiAutoDuration14_15
global entrySemiAutoDuration15_16
global entrySemiAutoDuration16_17
global entrySemiAutoDuration17_18
global entrySemiAutoDuration18_19
global entrySemiAutoDuration19_20
global entrySemiAutoDuration20_21
global entrySemiAutoDuration21_22
global entrySemiAutoDuration22_23
global entrySemiAutoDuration23_24
global configurationSemiAuto
global fenetreConfigSemiAuto


def startSemiAutConf():
    global entrySemiAutoFrequency0_1
    global entrySemiAutoFrequency1_2
    global entrySemiAutoFrequency2_3
    global entrySemiAutoFrequency3_4
    global entrySemiAutoFrequency4_5
    global entrySemiAutoFrequency5_6
    global entrySemiAutoFrequency6_7
    global entrySemiAutoFrequency7_8
    global entrySemiAutoFrequency8_9
    global entrySemiAutoFrequency9_10
    global entrySemiAutoFrequency10_11
    global entrySemiAutoFrequency11_12
    global entrySemiAutoFrequency12_13
    global entrySemiAutoFrequency13_14
    global entrySemiAutoFrequency14_15
    global entrySemiAutoFrequency15_16
    global entrySemiAutoFrequency16_17
    global entrySemiAutoFrequency17_18
    global entrySemiAutoFrequency18_19
    global entrySemiAutoFrequency19_20
    global entrySemiAutoFrequency20_21
    global entrySemiAutoFrequency21_22
    global entrySemiAutoFrequency22_23
    global entrySemiAutoFrequency23_24
    global entrySemiAutoDuration0_1
    global entrySemiAutoDuration1_2
    global entrySemiAutoDuration2_3
    global entrySemiAutoDuration3_4
    global entrySemiAutoDuration4_5
    global entrySemiAutoDuration5_6
    global entrySemiAutoDuration6_7
    global entrySemiAutoDuration7_8
    global entrySemiAutoDuration8_9
    global entrySemiAutoDuration9_10
    global entrySemiAutoDuration10_11
    global entrySemiAutoDuration11_12
    global entrySemiAutoDuration12_13
    global entrySemiAutoDuration13_14
    global entrySemiAutoDuration14_15
    global entrySemiAutoDuration15_16
    global entrySemiAutoDuration16_17
    global entrySemiAutoDuration17_18
    global entrySemiAutoDuration18_19
    global entrySemiAutoDuration19_20
    global entrySemiAutoDuration20_21
    global entrySemiAutoDuration21_22
    global entrySemiAutoDuration22_23
    global entrySemiAutoDuration23_24
    global configurationSemiAuto
    global fenetreConfigSemiAuto

    configurationSemiAuto = readConfigSemiAuto()
    fenetreConfigSemiAuto = Tk()


    # create a notebook
    AMPMnotebook = ttk.Notebook(fenetreConfigSemiAuto)
    AMPMnotebook.grid(row=0, column=0)

    # create frames
    AMFrame = ttk.Frame(AMPMnotebook, width=400, height=280)
    PMFrame = ttk.Frame(AMPMnotebook, width=400, height=280)

    AMFrame.grid(row=0, column=0)
    PMFrame.grid(row=0, column=0)

    # add frames to notebook

    AMPMnotebook.add(AMFrame, text='AM Times')
    AMPMnotebook.add(PMFrame, text='PM Times')

    Label(AMFrame, text="Frequency (seconds)").grid(row=0, column=1)
    Label(AMFrame, text="Duration (seconds)").grid(row=0, column=2)
    Label(PMFrame, text="Frequency (seconds)").grid(row=0, column=1)
    Label(PMFrame, text="Duration (seconds)").grid(row=0, column=2)

    saveButtonSemiAutoAM = Button(AMFrame, text="Save", command=saveDataSemiAuto)
    cancelButtoSemiAutoAM = Button(AMFrame, text="Cancel", command=fenetreConfigSemiAuto.destroy)
    saveButtonSemiAutoPM = Button(PMFrame, text="Save", command=saveDataSemiAuto)
    cancelButtoSemiAutoPM = Button(PMFrame, text="Cancel", command=fenetreConfigSemiAuto.destroy)

    saveButtonSemiAutoAM.grid(row=14, column=1, pady=10)
    cancelButtoSemiAutoAM.grid(row=14, column=2, pady=10)
    saveButtonSemiAutoPM.grid(row=14, column=1, pady=10)
    cancelButtoSemiAutoPM.grid(row=14, column=2, pady=10)


    labelSemiAutoFrequency0_1 = Label(AMFrame, text="Beetween 00h and 01h")
    entrySemiAutoFrequency0_1_text = StringVar()
    entrySemiAutoFrequency0_1_text.set("")
    entrySemiAutoFrequency0_1 = Entry(AMFrame, textvariable=entrySemiAutoFrequency0_1_text, width=15)
    entrySemiAutoFrequency0_1.insert(END,configurationSemiAuto["semiAutoFrequency0_1"])

    entrySemiAutoDuration0_1_text = StringVar()
    entrySemiAutoDuration0_1_text.set("")
    entrySemiAutoDuration0_1 = Entry(AMFrame, textvariable=entrySemiAutoDuration0_1_text, width=15)
    entrySemiAutoDuration0_1.insert(END,configurationSemiAuto["semiAutoDuration0_1"])

    labelSemiAutoFrequency0_1.grid(row=1, column=0)
    entrySemiAutoFrequency0_1.grid(row=1, column=1)
    entrySemiAutoDuration0_1.grid(row=1, column=2)

    ########################################################################################

    labelSemiAutoFrequency1_2 = Label(AMFrame, text="Beetween 01h and 02h")
    entrySemiAutoFrequency1_2_text = StringVar()
    entrySemiAutoFrequency1_2_text.set("")
    entrySemiAutoFrequency1_2 = Entry(AMFrame, textvariable=entrySemiAutoFrequency1_2_text, width=15)
    entrySemiAutoFrequency1_2.insert(END,configurationSemiAuto["semiAutoFrequency1_2"])

    entrySemiAutoDuration1_2_text = StringVar()
    entrySemiAutoDuration1_2_text.set("")
    entrySemiAutoDuration1_2 = Entry(AMFrame, textvariable=entrySemiAutoDuration1_2_text, width=15)
    entrySemiAutoDuration1_2.insert(END,configurationSemiAuto["semiAutoDuration1_2"])

    labelSemiAutoFrequency1_2.grid(row=2, column=0)
    entrySemiAutoFrequency1_2.grid(row=2, column=1)
    entrySemiAutoDuration1_2.grid(row=2, column=2)

    ########################################################################################

    labelSemiAutoFrequency2_3 = Label(AMFrame, text="Beetween 02h and 03h")
    entrySemiAutoFrequency2_3_text = StringVar()
    entrySemiAutoFrequency2_3_text.set("")
    entrySemiAutoFrequency2_3 = Entry(AMFrame, textvariable=entrySemiAutoFrequency2_3_text, width=15)
    entrySemiAutoFrequency2_3.insert(END,configurationSemiAuto["semiAutoFrequency2_3"])

    entrySemiAutoDuration2_3_text = StringVar()
    entrySemiAutoDuration2_3_text.set("")
    entrySemiAutoDuration2_3 = Entry(AMFrame, textvariable=entrySemiAutoDuration2_3_text, width=15)
    entrySemiAutoDuration2_3.insert(END,configurationSemiAuto["semiAutoDuration2_3"])

    labelSemiAutoFrequency2_3.grid(row=3, column=0)
    entrySemiAutoFrequency2_3.grid(row=3, column=1)
    entrySemiAutoDuration2_3.grid(row=3, column=2)

    ########################################################################################

    labelSemiAutoFrequency3_4 = Label(AMFrame, text="Beetween 03h and 04h")
    entrySemiAutoFrequency3_4_text = StringVar()
    entrySemiAutoFrequency3_4_text.set("")
    entrySemiAutoFrequency3_4 = Entry(AMFrame, textvariable=entrySemiAutoFrequency3_4_text, width=15)
    entrySemiAutoFrequency3_4.insert(END,configurationSemiAuto["semiAutoFrequency3_4"])

    entrySemiAutoDuration3_4_text = StringVar()
    entrySemiAutoDuration3_4_text.set("")
    entrySemiAutoDuration3_4 = Entry(AMFrame, textvariable=entrySemiAutoDuration3_4_text, width=15)
    entrySemiAutoDuration3_4.insert(END,configurationSemiAuto["semiAutoDuration3_4"])

    labelSemiAutoFrequency3_4.grid(row=4, column=0)
    entrySemiAutoFrequency3_4.grid(row=4, column=1)
    entrySemiAutoDuration3_4.grid(row=4, column=2)

    ########################################################################################

    labelSemiAutoFrequency4_5 = Label(AMFrame, text="Beetween 04h and 05h")
    entrySemiAutoFrequency4_5_text = StringVar()
    entrySemiAutoFrequency4_5_text.set("")
    entrySemiAutoFrequency4_5 = Entry(AMFrame, textvariable=entrySemiAutoFrequency4_5_text, width=15)
    entrySemiAutoFrequency4_5.insert(END,configurationSemiAuto["semiAutoFrequency4_5"])

    entrySemiAutoDuration4_5_text = StringVar()
    entrySemiAutoDuration4_5_text.set("")
    entrySemiAutoDuration4_5 = Entry(AMFrame, textvariable=entrySemiAutoDuration4_5_text, width=15)
    entrySemiAutoDuration4_5.insert(END,configurationSemiAuto["semiAutoDuration4_5"])

    labelSemiAutoFrequency4_5.grid(row=5, column=0)
    entrySemiAutoFrequency4_5.grid(row=5, column=1)
    entrySemiAutoDuration4_5.grid(row=5, column=2)

    ########################################################################################

    labelSemiAutoFrequency5_6 = Label(AMFrame, text="Beetween 05h and 06h")
    entrySemiAutoFrequency5_6_text = StringVar()
    entrySemiAutoFrequency5_6_text.set("")
    entrySemiAutoFrequency5_6 = Entry(AMFrame, textvariable=entrySemiAutoFrequency5_6_text, width=15)
    entrySemiAutoFrequency5_6.insert(END,configurationSemiAuto["semiAutoFrequency5_6"])

    entrySemiAutoDuration5_6_text = StringVar()
    entrySemiAutoDuration5_6_text.set("")
    entrySemiAutoDuration5_6 = Entry(AMFrame, textvariable=entrySemiAutoDuration5_6_text, width=15)
    entrySemiAutoDuration5_6.insert(END,configurationSemiAuto["semiAutoDuration5_6"])

    labelSemiAutoFrequency5_6.grid(row=6, column=0)
    entrySemiAutoFrequency5_6.grid(row=6, column=1)
    entrySemiAutoDuration5_6.grid(row=6, column=2)

    ########################################################################################

    labelSemiAutoFrequency6_7 = Label(AMFrame, text="Beetween 06h and 07h")
    entrySemiAutoFrequency6_7_text = StringVar()
    entrySemiAutoFrequency6_7_text.set("")
    entrySemiAutoFrequency6_7 = Entry(AMFrame, textvariable=entrySemiAutoFrequency6_7_text, width=15)
    entrySemiAutoFrequency6_7.insert(END,configurationSemiAuto["semiAutoFrequency6_7"])

    entrySemiAutoDuration6_7_text = StringVar()
    entrySemiAutoDuration6_7_text.set("")
    entrySemiAutoDuration6_7 = Entry(AMFrame, textvariable=entrySemiAutoDuration6_7_text, width=15)
    entrySemiAutoDuration6_7.insert(END,configurationSemiAuto["semiAutoDuration6_7"])

    labelSemiAutoFrequency6_7.grid(row=7, column=0)
    entrySemiAutoFrequency6_7.grid(row=7, column=1)
    entrySemiAutoDuration6_7.grid(row=7, column=2)

    ########################################################################################

    labelSemiAutoFrequency7_8 = Label(AMFrame, text="Beetween 7h and 8h")
    entrySemiAutoFrequency7_8_text = StringVar()
    entrySemiAutoFrequency7_8_text.set("")
    entrySemiAutoFrequency7_8 = Entry(AMFrame, textvariable=entrySemiAutoFrequency7_8_text, width=15)
    entrySemiAutoFrequency7_8.insert(END,configurationSemiAuto["semiAutoFrequency7_8"])

    entrySemiAutoDuration7_8_text = StringVar()
    entrySemiAutoDuration7_8_text.set("")
    entrySemiAutoDuration7_8 = Entry(AMFrame, textvariable=entrySemiAutoDuration7_8_text, width=15)
    entrySemiAutoDuration7_8.insert(END,configurationSemiAuto["semiAutoDuration7_8"])

    labelSemiAutoFrequency7_8.grid(row=8, column=0)
    entrySemiAutoFrequency7_8.grid(row=8, column=1)
    entrySemiAutoDuration7_8.grid(row=8, column=2)

    ########################################################################################

    labelSemiAutoFrequency8_9 = Label(AMFrame, text="Beetween 08h and 09h")
    entrySemiAutoFrequency8_9_text = StringVar()
    entrySemiAutoFrequency8_9_text.set("")
    entrySemiAutoFrequency8_9 = Entry(AMFrame, textvariable=entrySemiAutoFrequency8_9_text, width=15)
    entrySemiAutoFrequency8_9.insert(END,configurationSemiAuto["semiAutoFrequency8_9"])

    entrySemiAutoDuration8_9_text = StringVar()
    entrySemiAutoDuration8_9_text.set("")
    entrySemiAutoDuration8_9 = Entry(AMFrame, textvariable=entrySemiAutoDuration8_9_text, width=15)
    entrySemiAutoDuration8_9.insert(END,configurationSemiAuto["semiAutoDuration8_9"])

    labelSemiAutoFrequency8_9.grid(row=9, column=0)
    entrySemiAutoFrequency8_9.grid(row=9, column=1)
    entrySemiAutoDuration8_9.grid(row=9, column=2)

    ########################################################################################

    labelSemiAutoFrequency9_10 = Label(AMFrame, text="Beetween 09h and 10h")
    entrySemiAutoFrequency9_10_text = StringVar()
    entrySemiAutoFrequency9_10_text.set("")
    entrySemiAutoFrequency9_10 = Entry(AMFrame, textvariable=entrySemiAutoFrequency9_10_text, width=15)
    entrySemiAutoFrequency9_10.insert(END,configurationSemiAuto["semiAutoFrequency9_10"])

    entrySemiAutoDuration9_10_text = StringVar()
    entrySemiAutoDuration9_10_text.set("")
    entrySemiAutoDuration9_10 = Entry(AMFrame, textvariable=entrySemiAutoDuration9_10_text, width=15)
    entrySemiAutoDuration9_10.insert(END,configurationSemiAuto["semiAutoDuration9_10"])

    labelSemiAutoFrequency9_10.grid(row=10, column=0)
    entrySemiAutoFrequency9_10.grid(row=10, column=1)
    entrySemiAutoDuration9_10.grid(row=10, column=2)

    ########################################################################################

    labelSemiAutoFrequency10_11 = Label(AMFrame, text="Beetween 10h and 11h")
    entrySemiAutoFrequency10_11_text = StringVar()
    entrySemiAutoFrequency10_11_text.set("")
    entrySemiAutoFrequency10_11 = Entry(AMFrame, textvariable=entrySemiAutoFrequency10_11_text, width=15)
    entrySemiAutoFrequency10_11.insert(END,configurationSemiAuto["semiAutoFrequency10_11"])

    entrySemiAutoDuration10_11_text = StringVar()
    entrySemiAutoDuration10_11_text.set("")
    entrySemiAutoDuration10_11 = Entry(AMFrame, textvariable=entrySemiAutoDuration10_11_text, width=15)
    entrySemiAutoDuration10_11.insert(END,configurationSemiAuto["semiAutoDuration10_11"])

    labelSemiAutoFrequency10_11.grid(row=11, column=0)
    entrySemiAutoFrequency10_11.grid(row=11, column=1)
    entrySemiAutoDuration10_11.grid(row=11, column=2)

    ########################################################################################

    labelSemiAutoFrequency11_12 = Label(AMFrame, text="Beetween 11h and 12h")
    entrySemiAutoFrequency11_12_text = StringVar()
    entrySemiAutoFrequency11_12_text.set("")
    entrySemiAutoFrequency11_12 = Entry(AMFrame, textvariable=entrySemiAutoFrequency11_12_text, width=15)
    entrySemiAutoFrequency11_12.insert(END,configurationSemiAuto["semiAutoFrequency11_12"])

    entrySemiAutoDuration11_12_text = StringVar()
    entrySemiAutoDuration11_12_text.set("")
    entrySemiAutoDuration11_12 = Entry(AMFrame, textvariable=entrySemiAutoDuration11_12_text, width=15)
    entrySemiAutoDuration11_12.insert(END,configurationSemiAuto["semiAutoDuration11_12"])

    labelSemiAutoFrequency11_12.grid(row=12, column=0)
    entrySemiAutoFrequency11_12.grid(row=12, column=1)
    entrySemiAutoDuration11_12.grid(row=12, column=2)

    ########################################################################################

    labelSemiAutoFrequency12_13 = Label(PMFrame, text="Beetween 12h and 13h")
    entrySemiAutoFrequency12_13_text = StringVar()
    entrySemiAutoFrequency12_13_text.set("")
    entrySemiAutoFrequency12_13 = Entry(PMFrame, textvariable=entrySemiAutoFrequency12_13_text, width=15)
    entrySemiAutoFrequency12_13.insert(END,configurationSemiAuto["semiAutoFrequency12_13"])

    entrySemiAutoDuration12_13_text = StringVar()
    entrySemiAutoDuration12_13_text.set("")
    entrySemiAutoDuration12_13 = Entry(PMFrame, textvariable=entrySemiAutoDuration12_13_text, width=15)
    entrySemiAutoDuration12_13.insert(END,configurationSemiAuto["semiAutoDuration12_13"])

    labelSemiAutoFrequency12_13.grid(row=1, column=0)
    entrySemiAutoFrequency12_13.grid(row=1, column=1)
    entrySemiAutoDuration12_13.grid(row=1, column=2)

    ########################################################################################

    labelSemiAutoFrequency13_14 = Label(PMFrame, text="Beetween 13h and 14h")
    entrySemiAutoFrequency13_14_text = StringVar()
    entrySemiAutoFrequency13_14_text.set("")
    entrySemiAutoFrequency13_14 = Entry(PMFrame, textvariable=entrySemiAutoFrequency13_14_text, width=15)
    entrySemiAutoFrequency13_14.insert(END,configurationSemiAuto["semiAutoFrequency13_14"])

    entrySemiAutoDuration13_14_text = StringVar()
    entrySemiAutoDuration13_14_text.set("")
    entrySemiAutoDuration13_14 = Entry(PMFrame, textvariable=entrySemiAutoDuration13_14_text, width=15)
    entrySemiAutoDuration13_14.insert(END,configurationSemiAuto["semiAutoDuration13_14"])

    labelSemiAutoFrequency13_14.grid(row=2, column=0)
    entrySemiAutoFrequency13_14.grid(row=2, column=1)
    entrySemiAutoDuration13_14.grid(row=2, column=2)

    ########################################################################################

    labelSemiAutoFrequency14_15 = Label(PMFrame, text="Beetween 14h and 15h")
    entrySemiAutoFrequency14_15_text = StringVar()
    entrySemiAutoFrequency14_15_text.set("")
    entrySemiAutoFrequency14_15 = Entry(PMFrame, textvariable=entrySemiAutoFrequency14_15_text, width=15)
    entrySemiAutoFrequency14_15.insert(END,configurationSemiAuto["semiAutoFrequency14_15"])

    entrySemiAutoDuration14_15_text = StringVar()
    entrySemiAutoDuration14_15_text.set("")
    entrySemiAutoDuration14_15 = Entry(PMFrame, textvariable=entrySemiAutoDuration14_15_text, width=15)
    entrySemiAutoDuration14_15.insert(END,configurationSemiAuto["semiAutoDuration14_15"])

    labelSemiAutoFrequency14_15.grid(row=3, column=0)
    entrySemiAutoFrequency14_15.grid(row=3, column=1)
    entrySemiAutoDuration14_15.grid(row=3, column=2)

    ########################################################################################

    labelSemiAutoFrequency15_16 = Label(PMFrame, text="Beetween 15h and 16h")
    entrySemiAutoFrequency15_16_text = StringVar()
    entrySemiAutoFrequency15_16_text.set("")
    entrySemiAutoFrequency15_16 = Entry(PMFrame, textvariable=entrySemiAutoFrequency15_16_text, width=15)
    entrySemiAutoFrequency15_16.insert(END,configurationSemiAuto["semiAutoFrequency15_16"])

    entrySemiAutoDuration15_16_text = StringVar()
    entrySemiAutoDuration15_16_text.set("")
    entrySemiAutoDuration15_16 = Entry(PMFrame, textvariable=entrySemiAutoDuration15_16_text, width=15)
    entrySemiAutoDuration15_16.insert(END,configurationSemiAuto["semiAutoDuration15_16"])

    labelSemiAutoFrequency15_16.grid(row=4, column=0)
    entrySemiAutoFrequency15_16.grid(row=4, column=1)
    entrySemiAutoDuration15_16.grid(row=4, column=2)

    ########################################################################################

    labelSemiAutoFrequency16_17 = Label(PMFrame, text="Beetween 16h and 17h")
    entrySemiAutoFrequency16_17_text = StringVar()
    entrySemiAutoFrequency16_17_text.set("")
    entrySemiAutoFrequency16_17 = Entry(PMFrame, textvariable=entrySemiAutoFrequency16_17_text, width=15)
    entrySemiAutoFrequency16_17.insert(END,configurationSemiAuto["semiAutoFrequency16_17"])

    entrySemiAutoDuration16_17_text = StringVar()
    entrySemiAutoDuration16_17_text.set("")
    entrySemiAutoDuration16_17 = Entry(PMFrame, textvariable=entrySemiAutoDuration16_17_text, width=15)
    entrySemiAutoDuration16_17.insert(END,configurationSemiAuto["semiAutoDuration16_17"])

    labelSemiAutoFrequency16_17.grid(row=6, column=0)
    entrySemiAutoFrequency16_17.grid(row=6, column=1)
    entrySemiAutoDuration16_17.grid(row=6, column=2)

    ########################################################################################

    labelSemiAutoFrequency17_18 = Label(PMFrame, text="Beetween 17h and 18h")
    entrySemiAutoFrequency17_18_text = StringVar()
    entrySemiAutoFrequency17_18_text.set("")
    entrySemiAutoFrequency17_18 = Entry(PMFrame, textvariable=entrySemiAutoFrequency17_18_text, width=15)
    entrySemiAutoFrequency17_18.insert(END,configurationSemiAuto["semiAutoFrequency17_18"])

    entrySemiAutoDuration17_18_text = StringVar()
    entrySemiAutoDuration17_18_text.set("")
    entrySemiAutoDuration17_18 = Entry(PMFrame, textvariable=entrySemiAutoDuration17_18_text, width=15)
    entrySemiAutoDuration17_18.insert(END,configurationSemiAuto["semiAutoDuration17_18"])

    labelSemiAutoFrequency17_18.grid(row=7, column=0)
    entrySemiAutoFrequency17_18.grid(row=7, column=1)
    entrySemiAutoDuration17_18.grid(row=7, column=2)

    ########################################################################################

    labelSemiAutoFrequency18_19 = Label(PMFrame, text="Beetween 18h and 19h")
    entrySemiAutoFrequency18_19_text = StringVar()
    entrySemiAutoFrequency18_19_text.set("")
    entrySemiAutoFrequency18_19 = Entry(PMFrame, textvariable=entrySemiAutoFrequency18_19_text, width=15)
    entrySemiAutoFrequency18_19.insert(END,configurationSemiAuto["semiAutoFrequency18_19"])

    entrySemiAutoDuration18_19_text = StringVar()
    entrySemiAutoDuration18_19_text.set("")
    entrySemiAutoDuration18_19 = Entry(PMFrame, textvariable=entrySemiAutoDuration18_19_text, width=15)
    entrySemiAutoDuration18_19.insert(END,configurationSemiAuto["semiAutoDuration18_19"])

    labelSemiAutoFrequency18_19.grid(row=8, column=0)
    entrySemiAutoFrequency18_19.grid(row=8, column=1)
    entrySemiAutoDuration18_19.grid(row=8, column=2)

    ########################################################################################

    labelSemiAutoFrequency19_20 = Label(PMFrame, text="Beetween 19h and 20h")
    entrySemiAutoFrequency19_20_text = StringVar()
    entrySemiAutoFrequency19_20_text.set("")
    entrySemiAutoFrequency19_20 = Entry(PMFrame, textvariable=entrySemiAutoFrequency19_20_text, width=15)
    entrySemiAutoFrequency19_20.insert(END,configurationSemiAuto["semiAutoFrequency19_20"])

    entrySemiAutoDuration19_20_text = StringVar()
    entrySemiAutoDuration19_20_text.set("")
    entrySemiAutoDuration19_20 = Entry(PMFrame, textvariable=entrySemiAutoDuration19_20_text, width=15)
    entrySemiAutoDuration19_20.insert(END,configurationSemiAuto["semiAutoDuration19_20"])

    labelSemiAutoFrequency19_20.grid(row=9, column=0)
    entrySemiAutoFrequency19_20.grid(row=9, column=1)
    entrySemiAutoDuration19_20.grid(row=9, column=2)

    ########################################################################################

    labelSemiAutoFrequency20_21 = Label(PMFrame, text="Beetween 20h and 21h")
    entrySemiAutoFrequency20_21_text = StringVar()
    entrySemiAutoFrequency20_21_text.set("")
    entrySemiAutoFrequency20_21 = Entry(PMFrame, textvariable=entrySemiAutoFrequency20_21_text, width=15)
    entrySemiAutoFrequency20_21.insert(END,configurationSemiAuto["semiAutoFrequency20_21"])

    entrySemiAutoDuration20_21_text = StringVar()
    entrySemiAutoDuration20_21_text.set("")
    entrySemiAutoDuration20_21 = Entry(PMFrame, textvariable=entrySemiAutoDuration20_21_text, width=15)
    entrySemiAutoDuration20_21.insert(END,configurationSemiAuto["semiAutoDuration20_21"])

    labelSemiAutoFrequency20_21.grid(row=10, column=0)
    entrySemiAutoFrequency20_21.grid(row=10, column=1)
    entrySemiAutoDuration20_21.grid(row=10, column=2)

    ########################################################################################

    labelSemiAutoFrequency21_22 = Label(PMFrame, text="Beetween 21h and 22h")
    entrySemiAutoFrequency21_22_text = StringVar()
    entrySemiAutoFrequency21_22_text.set("")
    entrySemiAutoFrequency21_22 = Entry(PMFrame, textvariable=entrySemiAutoFrequency21_22_text, width=15)
    entrySemiAutoFrequency21_22.insert(END,configurationSemiAuto["semiAutoFrequency21_22"])

    entrySemiAutoDuration21_22_text = StringVar()
    entrySemiAutoDuration21_22_text.set("")
    entrySemiAutoDuration21_22 = Entry(PMFrame, textvariable=entrySemiAutoDuration21_22_text, width=15)
    entrySemiAutoDuration21_22.insert(END,configurationSemiAuto["semiAutoDuration21_22"])

    labelSemiAutoFrequency21_22.grid(row=11, column=0)
    entrySemiAutoFrequency21_22.grid(row=11, column=1)
    entrySemiAutoDuration21_22.grid(row=11, column=2)

    ########################################################################################

    labelSemiAutoFrequency22_23 = Label(PMFrame, text="Beetween 22h and 23h")
    entrySemiAutoFrequency22_23_text = StringVar()
    entrySemiAutoFrequency22_23_text.set("")
    entrySemiAutoFrequency22_23 = Entry(PMFrame, textvariable=entrySemiAutoFrequency22_23_text, width=15)
    entrySemiAutoFrequency22_23.insert(END,configurationSemiAuto["semiAutoFrequency22_23"])

    entrySemiAutoDuration22_23_text = StringVar()
    entrySemiAutoDuration22_23_text.set("")
    entrySemiAutoDuration22_23 = Entry(PMFrame, textvariable=entrySemiAutoDuration22_23_text, width=15)
    entrySemiAutoDuration22_23.insert(END,configurationSemiAuto["semiAutoDuration22_23"])

    labelSemiAutoFrequency22_23.grid(row=12, column=0)
    entrySemiAutoFrequency22_23.grid(row=12, column=1)
    entrySemiAutoDuration22_23.grid(row=12, column=2)

    ########################################################################################

    labelSemiAutoFrequency23_24 = Label(PMFrame, text="Beetween 23h and 24h")
    entrySemiAutoFrequency23_24_text = StringVar()
    entrySemiAutoFrequency23_24_text.set("")
    entrySemiAutoFrequency23_24 = Entry(PMFrame, textvariable=entrySemiAutoFrequency23_24_text, width=15)
    entrySemiAutoFrequency23_24.insert(END,configurationSemiAuto["semiAutoFrequency23_24"])

    entrySemiAutoDuration23_24_text = StringVar()
    entrySemiAutoDuration23_24_text.set("")
    entrySemiAutoDuration23_24 = Entry(PMFrame, textvariable=entrySemiAutoDuration23_24_text, width=15)
    entrySemiAutoDuration23_24.insert(END,configurationSemiAuto["semiAutoDuration23_24"])

    labelSemiAutoFrequency23_24.grid(row=13, column=0)
    entrySemiAutoFrequency23_24.grid(row=13, column=1)
    entrySemiAutoDuration23_24.grid(row=13, column=2)

    ########################################################################################

    fenetreConfigSemiAuto.mainloop()