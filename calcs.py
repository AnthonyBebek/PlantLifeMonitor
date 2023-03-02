import Coms
import DB
import serial
from datetime import date, time, datetime, timedelta

requirements = str(DB.getcroprequirements())
requirements = requirements.split(',')
for i in range(len(requirements)):
    requirements[i] = requirements[i].replace("(","")
    requirements[i] = requirements[i].replace("[","")
    requirements[i] = requirements[i].replace("'","")
    requirements[i] = requirements[i].replace("]","")
    requirements[i] = requirements[i].replace(")","")
    requirements[i] = int(requirements[i])

#SET THESE VALUES TO YOUR PLANTS NEEDS
minAmoisture = requirements[1]
minSmoisture = requirements[3]
maxATemp = requirements[0]
maxStemp = requirements[2]
maxLight = requirements[4]
minWLevel = 10
#pumpseed is in Ml/s
Pumplps = 27
delay = 0

'''
WATERING CONDITIONS

-- IF ANY CONDITION IS MET THE PLANT WILL BE WATERED AND THE REASON WILL BE LOGGED --

- SOIL MOISTURE IS UNDER 50%
- AIR HUMIDITY IS UNDER 30%
- AIR TEMP IS OVER 21°C
- SOIL TEMP IS OVER 19°C
- LIGHT
- HASEN'T BEEN WATERED IN THE LAST 3 HOURS
- LUX LEVEL IS OVER 700
'''

Data = DB.getcurrnet()


AirTemp = Data[0]
Humidity = Data[1]
SoilTemp = Data[2]
SoilMoisture = Data[3]
Lux = Data[4]

AirTemp = ','.join(map(str, AirTemp))
Humidity = '.'.join(map(str, Humidity))
SoilTemp = '.'.join(map(str, SoilTemp))
SoilMoisture = '.'.join(map(str,SoilMoisture))
Lux = '.'.join(map(str,Lux))
AirTemp = int(AirTemp)
Humidity = int(Humidity)
SoilMoisture = int(SoilMoisture)
SoilTemp = int(SoilTemp)
Lux = int(Lux)

reason = ""

def water(delay):
    start = datetime.now()
    Coms.pump(delay)
    end = datetime.now()
    amount = datetime.now()
    diff = (end - start).total_seconds()
    amount = diff * Pumplps
    DB.updatewater(str(start)[:-7], str(end)[:-7], int(amount))


if AirTemp > maxATemp:
    reason = reason + "1"
    delay = delay + 0.5

if Humidity > minAmoisture:
    reson = reason + "2"
    delay = delay + 0.5

if SoilTemp > maxStemp:
    reason = reason + "3"
    delay = delay + 0.5

if SoilMoisture < minSmoisture:
    reason = reason + "4"
    delay = delay + 1.5

if Lux > maxLight:
    reason = reason + "5"
    delay = delay + 0.25

if AirTemp > maxATemp or Humidity > minAmoisture or SoilTemp > maxStemp or SoilMoisture < minSmoisture or Lux > maxLight:
    print("Plant needs water!")
    print("Reason: ", reason)
    water(delay)
else:
    print("Plant is currently fine")
    times = DB.getwatertimes()
    t1 = times[0]
    t1 = t1.replace("((", "")
    t1 = t1.replace("),)", "")
    t1 = t1.split(",")
    t2 = times[1]
    t2 = t2.replace("((", "")
    t2 = t2.replace("),)", "")
    t2 = t2.split(",")
    t3 = times[2]
    t3 = t3.replace("((", "")
    t3 = t3.replace("),)", "")
    t3 = t3.split(",")
    now = datetime.now()
    if now.hour -1 == t1[3] or now.hour - 1 == t2[3] or now.hour -1 == t3[3]:
        water(1)
        print("Plant watered because it might get hot soon")