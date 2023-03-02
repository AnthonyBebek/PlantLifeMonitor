import random
import chartjs
import sys
import datetime
import DB
import croniter
import serial
from datetime import date, time, datetime, timedelta
import json
from flask import (
    Flask,
    render_template,
    Response, 
    request, 
    redirect, 
    url_for
)


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

air_tmp_data = []
air_water_data = []
soil_tmp_data = []
soil_water_data = []
#Update data using ajax automatically

#MAIN GRAPHS
def soil_temp():
    s = DB.getlastMSoil()
    t = str(s[0])
    t = t.replace("]", "")
    t = t.replace("[", "")
    t = t.replace("'", "", 128)
    t = t.split(",")
    return t

def air_temp():
    s = DB.getlastMAir()
    t = str(s[0])
    t = t.replace("]", "")
    t = t.replace("[", "")
    t = t.replace("'", "", 128)
    t = t.split(",")
    return t

def air_water():
    s = DB.getlastMHumid()
    t = str(s[0])
    t = t.replace("]", "")
    t = t.replace("[", "")
    t = t.replace("'", "", 128)
    t = t.split(",")
    return t

def soil_water():
    s = DB.getlastMSoilMoist()
    t = str(s[0])
    t = t.replace("]", "")
    t = t.replace("[", "")
    t = t.replace("'", "", 128)
    t = t.split(",")
    return t


def timelabels():
    s = DB.getlastMSoilMoist()
    times = str(s[1])
    times = times.replace("]", "")
    times = times.replace("[", "")
    times = times.replace("'", "", 128)
    return times

#Other card infomation

#Page 1
Estimated_next_water_time = "00:00 AM"
Last_water_time = "00:00 AM"
Current_Water_Level = "0L / 0L"
Estimated_next_water_refill = "00/00/0000 00:00 AM"
Water_useage_since_planting = "0L / 0L"
#Page 2
Current_light_level = "Low"
Days_since_planting = "0"
Estimated_days_till_harvest = "0"
Planting_Date = "00/00/0000 00:00 AM"
Estimated_harvest_Date = "00/00/0000 00:00 AM"

def Estimated_next_water_time():
    now = datetime.now()
    sched = '1 * * * * *'
    cron = croniter.croniter(sched, now)
    res = cron.get_next(datetime)
    res = res.strftime("%a %d %b - %H:%m")
    return res

def Last_water_time():
    return str(DB.getlastwater())

def Current_Water_Level():
    return str(DB.getwaterlevel())

def Estimated_next_water_refill():
    CurrentWaterLevel = str(DB.getwaterlevel())
    CurrentWaterLevel = CurrentWaterLevel.replace("%", "")
    CurrentWaterLevel = int(CurrentWaterLevel)
    WaterUsageSincePlanting = str(DB.getWaterUseage())
    WaterUsageSincePlanting = WaterUsageSincePlanting.replace(" mill", "")
    WaterUsageSincePlanting = int(WaterUsageSincePlanting)
    DaysSincePlanting = str(DB.getDayssinceplant())
    DaysSincePlanting = DaysSincePlanting.replace(" Days", "")
    DaysSincePlanting = int(DaysSincePlanting)

    s = WaterUsageSincePlanting / DaysSincePlanting
    if s == 0:
        return "Unknown"
    else:
        Nextrefill = CurrentWaterLevel / s
        Nextrefill = int(Nextrefill)
        if Nextrefill == 0:
            return "Today"
        else:
            if Nextrefill == 1:
                return str(Nextrefill) + " Day"
            else:
                return str(Nextrefill) + " Days"

def Water_useage_since_planting():
    return str(DB.getWaterUseage())

def Current_light_level():
    return str(DB.getlux())

def Days_since_planting():
    return str(DB.getDayssinceplant())

def Estimated_days_till_harvest():
    data = DB.getharvestdays()
    return data

def Planting_Date():
    data = DB.getcropplantdate()
    return data

def Estimated_harvest_Date():
    data = DB.getharvestdate()
    return data

#Update DB with new Plant data

def new_plant():
    print("Hello")
    return "True"

@app.route('/timelabels/') 
def api_get_timelabels(): 
    return timelabels()

@app.route('/Estimated_next_water_time/') 
def api_get_Estimated_next_water_time(): 
    return Estimated_next_water_time()

@app.route('/Last_water_time/') 
def api_get_Last_water_time(): 
    return Last_water_time()

@app.route('/Current_Water_Level/') 
def api_get_Current_Water_Level(): 
    return Current_Water_Level()

@app.route('/Estimated_next_water_refill/') 
def api_get_Estimated_next_water_refill(): 
    return Estimated_next_water_refill()

@app.route('/Water_useage_since_planting/') 
def api_get_Water_useage_since_planting(): 
    return Water_useage_since_planting()

@app.route('/Current_light_level/') 
def api_get_Current_light_level(): 
    return Current_light_level()

@app.route('/Days_since_planting/') 
def api_get_Days_since_planting(): 
    return Days_since_planting()

@app.route('/Estimated_days_till_harvest/') 
def api_get_Estimated_days_till_harvest(): 
    return Estimated_days_till_harvest()

@app.route('/Planting_Date/') 
def api_get_Planting_Date(): 
    return Planting_Date()

@app.route('/Estimated_harvest_Date/') 
def api_get_Estimated_harvest_Date(): 
    return Estimated_harvest_Date()

#Sending the page to flask


@app.route('/')
@app.route('/index')
def index():
    global air_tmp_data
    global air_water_data
    global soil_tmp_data
    global soil_water_data
    return render_template('index.html', air_tmp_data=air_tmp_data, soil_tmp_data=soil_tmp_data, air_water_data=air_water_data, soil_water_data=soil_water_data)

@app.route('/photos')
def photos():
    return render_template('photos.html')

@app.route('/photolist')
def photolist():
    return str(30)

@app.route('/setup')
def setup():
    return render_template('setup.html')

@app.route('/soil_temp/') 
def api_get_soil_temp(): 
    return soil_temp()

@app.route('/air_temp/') 
def api_get_air_temp(): 
    return air_temp()

@app.route('/air_water/') 
def api_get_air_water(): 
    return air_water()

@app.route('/soil_water/') 
def api_get_soil_water(): 
    return soil_water()

@app.route('/getcrops/') 
def api_get_crops(): 
    return str(DB.getcrop())

#Update DB with new plant data

@app.route('/newplant', methods=['POST'])
def newplant():
    name =  request.form['name']
    Plantdate = request.form['PlantingDate']
    Harvestdate = request.form['HarvestDate']
    RAirTemp = request.form['RAirTemp']
    RHumidity = request.form['RHumidity']
    RSoilTemp = request.form['RSoilTemp']
    RSoilMoist = request.form['RSoilMoist']
    RLux = request.form['RLux']
    RTimePerWater = request.form['RTimePerWater']
    RWaterPerInt = request.form['RWaterPerInt']
    DB.newplant(name, Plantdate, Harvestdate, RAirTemp, RHumidity, RSoilTemp, RSoilMoist, RLux, RTimePerWater, RWaterPerInt)
    return json.dumps({'status':'OK'})

@app.route('/noplant', methods = ['POST'])
def noplant():
    DB.noplant()
    return json.dumps({'status':'OK'})


@app.route("/new_plant", methods=['POST', 'GET'])
def conf_services():
    if request.method == "POST":
        app.logger.warning(request.values.get('new_freq'))
        new_plant()
    return "Ok"

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)