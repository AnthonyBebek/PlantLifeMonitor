import mariadb
import sys

def getlastMAir():
    conn = mariadb.connect(
        user="Growth",
        password="Growth",
        host="127.0.0.1",
        port=3306,
        database="Growth")
    dt = []
    temp = []
    temperature = []
    Times = []
    cur = conn.cursor(buffered=True)
    cur.execute("SELECT M_AirTemp, DATE_FORMAT(MeasurementTime, \"%d\" \" \" \"%b\" \" \" \"%Y\" \" - \" \"%H\" \":\" \"%i\") From CropSensors WHERE MeasurementTime >= (DATE(NOW())-1/24) LIMIT 48;")
    for water in cur:
        temp.append(water)
    for index in range(len(temp)):
        s = temp[index]
        s = list(s)
        temperature.append(s[0])
        dt.append(s[1])
    for index in range(len(dt)):
        t = dt[index]
        t = str(t)
        t = t.replace("datetime.datetime", "")
        Times.append(t)
    conn.close()
    return temperature, Times

def getlastMSoil():
    conn = mariadb.connect(
        user="Growth",
        password="Growth",
        host="127.0.0.1",
        port=3306,
        database="Growth")
    dt = []
    temp = []
    temperature = []
    Times = []
    cur = conn.cursor(buffered=True)
    cur.execute("SELECT M_SoilTemp, MeasurementTime From CropSensors WHERE MeasurementTime >= (DATE(NOW())-1/24) LIMIT 48;")
    for water in cur:
        temp.append(water)
    for index in range(len(temp)):
        s = temp[index]
        s = list(s)
        temperature.append(s[0])
        dt.append(s[1])
    for index in range(len(dt)):
        t = dt[index]
        t = str(t)
        t = t.replace("datetime.datetime", "")
        Times.append(t)
    conn.close()
    return temperature, Times

def getlastMHumid():
    conn = mariadb.connect(
        user="Growth",
        password="Growth",
        host="127.0.0.1",
        port=3306,
        database="Growth")
    dt = []
    temp = []
    temperature = []
    Times = []
    cur = conn.cursor(buffered=True)
    cur.execute("SELECT M_Humidity, MeasurementTime From CropSensors WHERE MeasurementTime >= (DATE(NOW())-1/24) LIMIT 48;")
    for water in cur:
        temp.append(water)
    for index in range(len(temp)):
        s = temp[index]
        s = list(s)
        temperature.append(s[0])
        dt.append(s[1])
    for index in range(len(dt)):
        t = dt[index]
        t = str(t)
        t = t.replace("datetime.datetime", "")
        Times.append(t)
    conn.close()
    return temperature, Times


def getlastMSoilMoist():
    conn = mariadb.connect(
        user="Growth",
        password="Growth",
        host="127.0.0.1",
        port=3306,
        database="Growth")
    dt = []
    temp = []
    temperature = []
    Times = []
    cur = conn.cursor(buffered=True)
    cur.execute("SELECT M_SoilMoisture, DATE_FORMAT(MeasurementTime, \"%d\" \" \" \"%b\" \" \"  \"%H\" \":\" \"%i\" ) From CropSensors WHERE MeasurementTime >= (DATE(NOW())-1/24) LIMIT 48;;") 
    for water in cur:
        temp.append(water)
    for index in range(len(temp)):
        s = temp[index]
        s = list(s)
        temperature.append(s[0])
        dt.append(s[1])
    for index in range(len(dt)):
        t = dt[index]
        t = str(t)
        t = t.replace("datetime.datetime", "")
        Times.append(t)
    conn.close()
    return temperature, Times

def updatesensors(AT, AM, ST, SM, LUX, WL):
        conn = mariadb.connect(
        user="Growth",
        password="Growth",
        host="127.0.0.1",
        port=3306,
        database="Growth")
        cur = conn.cursor()
        cur.execute("INSERT INTO CropSensors (`PlantName`, `MeasurementTime`, `M_AirTemp`, `M_Humidity`, `M_SoilTemp`, `M_SoilMoisture`, `M_LuxLevel`, `WaterLevel`) VALUES ( \"" + str("Cress") + "\", CURTIME(), " + str(AT) + ", " + str(AM) + ", " + str(ST) + ", " + str(SM) + ", " + str(LUX) + "," + str(WL) + ");")
        conn.commit()
        conn.close()

def getcurrnet():
    conn = mariadb.connect(
        user="Growth",
        password="Growth",
        host="127.0.0.1",
        port=3306,
        database="Growth")
    temp = []
    temp2 = []
    temp3 = []
    temp4 = []
    temp5 = []
    Air_Temperature = []
    Air_Water = []
    Soil_Temperature = []
    Soil_Water = []
    Lux = []
    cur = conn.cursor(buffered=True)
    cur.execute("SELECT M_AirTemp, M_Humidity, M_SoilTemp, M_SoilMoisture, M_LuxLevel From CropSensors ORDER BY MeasurementTime DESC LIMIT 1;") 
    for water in cur:
        temp.append(water)
    for index in range(len(temp)):
        s = temp[index]
        s = list(s)
        Air_Temperature.append(s[0])
        temp2.append(s[1])
        temp3.append(s[2])
        temp4.append(s[3])
        temp5.append(s[4])
    for index in range(len(temp2)):
        t = temp2[index]
        t = str(t)
        Air_Water.append(t)
    for index in range(len(temp3)):
        x = temp3[index]
        x = str(x)
        Soil_Temperature.append(x)
    for index in range(len(temp4)):
        p = temp4[index]
        p = str(p)
        Soil_Water.append(p)  
    for index in range(len(temp5)):
        m = temp5[index]
        m = str(m)
        Lux.append(m) 
    conn.close()
    return Air_Temperature, Air_Water, Soil_Temperature, Soil_Water, Lux


def updatewater(start, end, amount):
        conn = mariadb.connect(
        user="Growth",
        password="Growth",
        host="127.0.0.1",
        port=3306,
        database="Growth")
        cur = conn.cursor()
        #print("INSERT INTO CropSustenance (`Timestamp`, `PlantName`, `FeedStartTime`, `FeedStopTime`, `FeedVolume`) VALUES (CURTIME(), \"" + str("Cress") + "\", " + str(start) + ", " + str(end) + ", " + str(amount) + ");")
        cur.execute("INSERT INTO CropSustenance (`Timestamp`, `PlantName`, `FeedStartTime`, `FeedStopTime`, `FeedVolume`) VALUES (CURTIME(), \"" + str("Cress") + "\", \"" + str(start) + "\", \"" + str(end) + "\", " + str(amount) + ");")
        conn.commit()
        conn.close()

def getlastwater():
        res = []
        conn = mariadb.connect(
        user="Growth",
        password="Growth",
        host="127.0.0.1",
        port=3306,
        database="Growth")
        cur = conn.cursor()
    
        cur.execute("SELECT DATE_FORMAT(FeedStartTime, \"%a \" \"%d\" \" \" \"%b\" \"  - \" \"%H\" \":\" \"%i\" ) FROM CropSustenance ORDER BY ID DESC LIMIT 1;")
        for i in cur:
            res.append(i)
        res = str(res).replace("[('", "")
        res = res.replace("',)]", "")
        conn.close()
        return res

def getcropplantdate():
        res = []
        conn = mariadb.connect(
        user="Growth",
        password="Growth",
        host="127.0.0.1",
        port=3306,
        database="Growth")
        cur = conn.cursor()
        cur.execute("SELECT DATE_FORMAT(PlantingDate, \"%a \" \"%d\" \" \" \"%b\" ) FROM Crop LIMIT 1;")
        for i in cur:
            res.append(i)
        res = str(res)
        res = res.replace("[('", "")
        res = res.replace("',)]", "")
        res = res.replace("[(datetime.date(", "")
        conn.close()
        return res

def getharvestdate():
        res = []
        conn = mariadb.connect(
        user="Growth",
        password="Growth",
        host="127.0.0.1",
        port=3306,
        database="Growth")
        cur = conn.cursor()
        cur.execute("SELECT DATE_FORMAT(HarvestDate, \"%a \" \"%d\" \" \" \"%b\" ) FROM Crop LIMIT 1;")
        for i in cur:
            res.append(i)
        res = str(res)
        res = res.replace("[('", "")
        res = res.replace("',)]", "")
        res = res.replace("[(datetime.date(", "")
        conn.close()
        return res

def getharvestdays():
        res = []
        conn = mariadb.connect(
        user="Growth",
        password="Growth",
        host="127.0.0.1",
        port=3306,
        database="Growth")
        cur = conn.cursor()
        cur.execute("SELECT DATEDIFF(`HarvestDate`, CURTIME()) AS Days FROM Crop LIMIT 1;")
        for i in cur:
            res.append(i)
        res = str(res)
        res = res.replace("[(", "")
        res = res.replace(",)]", "")
        res = res + " Days"
        conn.close()
        return res

def updatedays():
        res = []
        conn = mariadb.connect(
        user="Growth",
        password="Growth",
        host="127.0.0.1",
        port=3306,
        database="Growth")
        cur = conn.cursor()
        cur.execute("SELECT `DaysToHarvest` FROM Crop ORDER BY ID DESC LIMIT 1;")
        for i in cur:
            res.append(i)
        res = str(res)
        res = res.replace("[(", "")
        res = res.replace(",)]", "")
        res = res + " Days"
        conn.close()
        return res
    
def getwaterlevel():
        res = []
        conn = mariadb.connect(
        user="Growth",
        password="Growth",
        host="127.0.0.1",
        port=3306,
        database="Growth")
        cur = conn.cursor()
        cur.execute("SELECT `WaterLevel` FROM CropSensors ORDER BY ID DESC LIMIT 1;")
        for i in cur:
            res.append(i)
        res = str(res)
        res = res.replace("[(", "")
        res = res.replace(",)]", "")
        res = res + "%"
        conn.close()
        return res

def getlux():
        res = []
        conn = mariadb.connect(
        user="Growth",
        password="Growth",
        host="127.0.0.1",
        port=3306,
        database="Growth")
        cur = conn.cursor()
        cur.execute("SELECT `M_LuxLevel` FROM CropSensors ORDER BY ID DESC LIMIT 1;")
        for i in cur:
            res.append(i)
        res = str(res)
        res = res.replace("[(", "")
        res = res.replace(",)]", "")
        res = res + " Lux"
        conn.close()
        return res

def getWaterUseage():
        res = []
        conn = mariadb.connect(
        user="Growth",
        password="Growth",
        host="127.0.0.1",
        port=3306,
        database="Growth")
        cur = conn.cursor()
        cur.execute("SELECT SUM(`FeedVolume`) FROM CropSustenance;")
        for i in cur:
            res.append(i)
        res = str(res)
        res = res.replace("[(Decimal('", "")
        res = res.replace("'),)]", "")
        res = res + " mill"
        conn.close()
        return res

def getDayssinceplant():
        res = []
        conn = mariadb.connect(
        user="Growth",
        password="Growth",
        host="127.0.0.1",
        port=3306,
        database="Growth")
        cur = conn.cursor()
        cur.execute("SELECT DATEDIFF(CURTIME(), `PlantingDate`) AS Days FROM Crop LIMIT 1;")
        for i in cur:
            res.append(i)
        res = str(res)
        res = res.replace("[(", "")
        res = res.replace(",)]", "")
        res = res + " Days"
        conn.close()
        return res
    
def newplant(name, PlantingDate, HarvestDate, RAirTemp, RHumidity, RSoilTemp, RSoilMoist, RLux, RTimePerWater, RWaterPerInt):
        res = []
        conn = mariadb.connect(
        user="Growth",
        password="Growth",
        host="127.0.0.1",
        port=3306,
        database="Growth")
        cur = conn.cursor()
        #print("INSERT INTO Crop (`PlantName`, `PlantingDate`, `HarvestDate`, `AirTemp`, `Humidity`, `SoilTemp`, `SoilMoisture`, `LuxLevel`, `WaterInterval`, `WaterVolume`) VALUES (\"" + str(name) + "\", \"" + str(PlantingDate) + "\", \"" + str(HarvestDate) + "\", \"" + str(RAirTemp) + "\", \"" + str(RHumidity) + "\", \"" + str(RSoilTemp) + "\", \"" + str(RSoilMoist) + "\", \"" + str(RLux) + "\", \"" + str(RTimePerWater)+ "\", \"" + str(RWaterPerInt) + "\");")
        cur.execute("INSERT INTO Crop (`PlantName`, `PlantingDate`, `HarvestDate`, `AirTemp`, `Humidity`, `SoilTemp`, `SoilMoisture`, `LuxLevel`, `WaterInterval`, `WaterVolume`) VALUES (\"" + str(name) + "\", \"" + str(PlantingDate) + "\", \"" + str(HarvestDate) + "\", \"" + str(RAirTemp) + "\", \"" + str(RHumidity) + "\", \"" + str(RSoilTemp) + "\", \"" + str(RSoilMoist) + "\", \"" + str(RLux) + "\", \"" + str(RTimePerWater)+ "\", \"" + str(RWaterPerInt) + "\");")
        conn.commit()
        cur.execute("UPDATE Crop set `DaysToHarvest` = DATEDIFF(`HarvestDate`, `PlantingDate`) WHERE `DaysToHarvest`IS NULL;")
        conn.commit()
        conn.close()

def noplant():
    conn = mariadb.connect(
        user="Growth",
        password="Growth",
        host="127.0.0.1",
        port=3306,
        database="Growth")
    cur = conn.cursor()
    cur.execute("TRUNCATE TABLE Crop;")
    conn.commit()
    conn.close()

def getcrop():
    conn = mariadb.connect(
        user="Growth",
        password="Growth",
        host="127.0.0.1",
        port=3306,
        database="Growth")
    temp = []
    temp2 = []
    temp3 = []
    temp4 = []
    temp5 = []
    temp6 = []
    temp7 = []
    temp8 = []
    temp9 = []
    temp10 = []
    temp11 = []
    temp12 = []
    PlantName = []
    PlantingDate = []
    DaysToHarvest = []
    HarvestDate = []
    AirTemp = []
    AirHumidity = []
    SoilTemp = []
    SoilMositure = []
    Lux = []
    WaterInterval = []
    WaterVolume = []
    cur = conn.cursor(buffered=True)
    cur.execute("SELECT ID, PlantName, PlantingDate, DaysToHarvest, HarvestDate, AirTemp, Humidity, SoilTemp, SoilMoisture, LuxLevel, WaterInterval, WaterVolume From Crop ORDER BY ID DESC;") 
    for water in cur:
        temp.append(water)
    for index in range(len(temp)):
        s = temp[index]
        s = list(s)
        PlantName.append(s[0])
        temp2.append(s[1])
        temp3.append(s[2])
        temp4.append(s[3])
        temp5.append(s[4])
        temp6.append(s[5])
        temp7.append(s[6])
        temp8.append(s[7])
        temp9.append(s[8])
        temp10.append(s[9])
        temp11.append(s[10])
        temp12.append(s[11])
    for index in range(len(temp2)):
        t = temp2[index]
        t = str(t)
        PlantingDate.append(t)
    for index in range(len(temp3)):
        x = temp3[index]
        x = str(x)
        DaysToHarvest.append(x)
    for index in range(len(temp4)):
        x = temp4[index]
        x = str(x)
        HarvestDate.append(x)
    for index in range(len(temp5)):
        p = temp5[index]
        p = str(p)
        AirTemp.append(p)  
    for index in range(len(temp6)):
        m = temp6[index]
        m = str(m)
        AirHumidity.append(m) 
    for index in range(len(temp7)):
        t = temp6[index]
        t = str(t)
        SoilTemp.append(t)
    for index in range(len(temp8)):
        x = temp8[index]
        x = str(x)
        SoilMositure.append(x)
    for index in range(len(temp9)):
        p = temp9[index]
        p = str(p)
        Lux.append(p)  
    for index in range(len(temp10)):
        m = temp10[index]
        m = str(m)
        WaterInterval.append(m) 
    for index in range(len(temp11)):
        m = temp11[index]
        m = str(m)
        WaterVolume.append(m) 
    conn.close()
    return PlantName, PlantingDate, DaysToHarvest, HarvestDate, AirTemp, AirHumidity, SoilTemp, SoilMositure, Lux, WaterInterval, WaterVolume

def getcroprequirements():
    conn = mariadb.connect(
        user="Growth",
        password="Growth",
        host="127.0.0.1",
        port=3306,
        database="Growth")
    temp = []
    temp2 = []
    temp3 = []
    temp4 = []
    temp5 = []
    Air_Temperature = []
    Air_Water = []
    Soil_Temperature = []
    Soil_Water = []
    Lux = []
    cur = conn.cursor(buffered=True)
    cur.execute("SELECT AirTemp, Humidity, SoilTemp, SoilMoisture, LuxLevel From Crop ORDER BY ID DESC LIMIT 1;") 
    for water in cur:
        temp.append(water)
    for index in range(len(temp)):
        s = temp[index]
        s = list(s)
        Air_Temperature.append(s[0])
        temp2.append(s[1])
        temp3.append(s[2])
        temp4.append(s[3])
        temp5.append(s[4])
    for index in range(len(temp2)):
        t = temp2[index]
        t = str(t)
        Air_Water.append(t)
    for index in range(len(temp3)):
        x = temp3[index]
        x = str(x)
        Soil_Temperature.append(x)
    for index in range(len(temp4)):
        p = temp4[index]
        p = str(p)
        Soil_Water.append(p)  
    for index in range(len(temp5)):
        m = temp5[index]
        m = str(m)
        Lux.append(m) 
    conn.close()
    return Air_Temperature, Air_Water, Soil_Temperature, Soil_Water, Lux


def getwatertimes():
    dt = []
    Times = []
    conn = mariadb.connect(
        user="Growth",
        password="Growth",
        host="127.0.0.1",
        port=3306,
        database="Growth")
    cur = conn.cursor()
    cur.execute("SELECT MeasurementTime FROM CropSensors WHERE M_AirTemp > (SELECT avg(M_AirTemp) FROM CropSensors)  AND M_SoilMoisture < (SELECT avg(M_SoilMoisture) FROM CropSensors) AND M_LuxLevel < (SELECT avg(M_LuxLevel) FROM CropSensors) AND M_Humidity < (SELECT avg(M_Humidity) FROM CropSensors) ORDER BY MeasurementTime DESC LIMIT 3;")
    for i in cur:
        dt.append(i)
    for index in range(len(dt)):
        t = dt[index]
        t = str(t)
        t = t.replace("datetime.datetime", "")
        Times.append(t)
    conn.close()
    return Times
