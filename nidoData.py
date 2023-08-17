import requests
import json
import datetime
import pytz
from tzlocal import get_localzone
import dateutil.parser
import os 

def get_nth_key(dictionary, n=0):
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key

def readConfig():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + "/config/configNido.txt") as file:
        lines = [line.rstrip() for line in file]
    temp = {}
    for elem in lines:
        temp[elem.split("=")[0]] = elem.split("=")[1]
    return temp

def getLastNidoValue():
    configuration = readConfig()
    temp = []
    try:
        url = configuration["NidoUrl"] + "/rest/v1/devices/"+configuration["DeviceId"]+"/data?max-per-page=1"

        payload = {}
        headers = {
        'x-api-key': configuration["APIKey"]
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        my_var = json.loads(response.text)

        for i in range(len(my_var["data"][0])):
                
                if(get_nth_key(my_var["data"][0], i ).lower() == "datetime"):
                    my_var["data"][0][get_nth_key(my_var["data"][0], i )] = dateutil.parser.isoparse(my_var["data"][0][get_nth_key(my_var["data"][0], i )]).astimezone(get_localzone()).strftime('%d/%m/%Y\n  %H:%M:%S')
                    temp.append(["Last check", my_var["data"][0][get_nth_key(my_var["data"][0], i )]])
                else:
                    temp.append([get_nth_key(my_var["data"][0], i ), my_var["data"][0][get_nth_key(my_var["data"][0], i )]])
        print(temp)
    except Exception as e:
        print("Error while getting Nido Data")
        print(e)
        temp = ["Nido Data", "Error"]
    return temp

