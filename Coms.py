import serial
import DB
#import calcs
import time
import os

def getWL():
	WL = ""
	ser = serial.Serial('/dev/ttyACM0',9600, timeout=1)
	ser.reset_input_buffer()
	while WL == "":
		ser.write(b"7\n")
		WL = ser.readline().decode('utf-8').rstrip()
	ser.close()
	WL = str(WL)
	WL = WL.replace("b'", "")
	WL = WL.replace("\\r\\n\'", "")
	print("WaterLevel: ", WL)
	return str(WL)

def getvalues():
	lux = ""
	airT = ""
	airM = ""
	ST = ""
	SM = ""
	WL = ""
	ser = serial.Serial('/dev/ttyACM0',9600, timeout=1)
	ser.reset_input_buffer()
	while lux == "":
		ser.write(b"4\n")
		lux = ser.readline().decode('utf-8').rstrip()
	print("Light Level: ",lux)
	lux = str(lux)
	while airT == "":
		ser.write(b"2\n")
		airT = ser.readline().decode('utf-8').rstrip()
	print("Air Temp: ", airT)
	airT = str(airT)
	while airM == "":
		ser.write(b"3\n")
		airM = ser.readline().decode('utf-8').rstrip()
	print("Air Moisture: ", airM)
	airM = str(airM)
	while ST == "":
		ser.write(b"5\n")
		ST = ser.readline().decode('utf-8').rstrip()
	print("Soil Temp: ", ST)
	ST = str(ST)
	while SM == "":
		ser.write(b"6\n")
		SM = ser.readline().decode('utf-8').rstrip()
	print("Soil Moisture: ", SM)
	SM = str(SM)
	while WL == "":
		ser.write(b"7\n")
		WL = ser.readline().decode('utf-8').rstrip()
	print("Water Level: ", WL)
	WL = str(WL)
	ser.close()
	lux = float(lux)
	airT = float(airT)
	airM = float(airM)
	ST = float(ST)
	SM = float(SM)
	WL = float(WL)
	return lux, airT, airM, ST, SM, WL


def updatedb():
	list1 = list(getvalues())
	l1 = list1[0]
	aT1 = list1[1]
	aM1 = list1[2]
	ST1 = list1[3]
	SM1 = list1[4]
	WL1 = list1[5]
	list2 = list(getvalues())
	l2 = list2[0]
	aT2 = list2[1]
	aM2 = list2[2]
	ST2 = list2[3]
	SM2 = list2[4]
	WL2 = list2[5]
	list3 = list(getvalues())
	l3 = list3[0]
	aT3 = list3[1]
	aM3 = list3[2]
	ST3 = list3[3]
	SM3 = list3[4]
	WL3 = list3[5]
	airT = (aT1 + aT2 + aT3)/3
	airM = (aM1 + aM2 + aM3)/3
	ST = (ST1 + ST2 + ST3)/3
	SM = (SM1 + SM2 + SM3)/3
	lux = (l1 + l2 + l3)/3 
	WL = (WL1 + WL2 + WL3)/3
	DB.updatesensors(int(float(airT)), int(float(airM)), int(float(ST)),int(float(SM)), int(float(lux)), int(float(WL)))
	return

def pump(delay):
	print("Pumping")
	ser = serial.Serial('/dev/ttyACM0',9600, timeout=1)
	ser.reset_input_buffer()
	WL = ""
	while WL == "":
		ser.write(b"9\n")
		WL = ser.readline().decode('utf-8').rstrip()
	time.sleep(delay)
	WL = ""
	while WL == "":
		ser.write(b"8\n")
		WL = ser.readline().decode('utf-8').rstrip()
	ser.close()

updatedb()
