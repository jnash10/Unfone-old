import os
import datetime
from pytz import timezone

os.system("sudo airmon-ng start wlan1") #put dongle in monitor mode


timestamp = str(datetime.datetime.now(timezone('Asia/Kolkata')))   #configure date time attributes
newstamp = ""

for i in range(len(timestamp)):    #further date time configuration
        if timestamp[i] == "." or timestamp[i]== ":" or timestamp[i]== " ":
                newstamp = newstamp + "_"
        else:
                newstamp = newstamp + timestamp[i]


os.system("sudo python probemon.py -i wlan1mon -o logs/"+newstamp+" -f -r -s -l") #giive intructions to terminal/system 
#start Probemon.py with  instructions to show all possible data in wifi probe
