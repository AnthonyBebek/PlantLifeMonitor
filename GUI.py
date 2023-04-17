import PySimpleGUI as sg
import time
from gpiozero import CPUTemperature
import os
import socket

sg.theme('Material2')


def webserver():
    webstatus = os.system('systemctl is-active --quiet PMW.service')
    if webstatus == 0:
        webcolor = "Green"
        vis = False
        status = "Online"
    else:
        webcolor = "Red"
        vis = True
        status = "Offline"
    
    return status, webcolor, vis

def SQLServer():
    webstatus = os.system('systemctl is-active --quiet mysql.service')
    if webstatus == 0:
        webcolor = "Green"
        vis = False
        status = "Running"
    else:
        webcolor = "Red"
        vis = True
        status = "Stoppped"
    
    return status, webcolor, vis

def CPUTemp():
    the = CPUTemperature()
    cpu = int(the.temperature)
    if cpu > 0 or cpu == 0:
        if cpu < 40 or cpu == 40:
            cpucolor = "green"
        elif cpu > 40 and int(cpu) < 70:
            cpucolor = "orange"
        elif cpu > 70 or cpu == 70:
            cpucolor = "red"
    else:
        cpucolor = "grey"
    return str(cpu), cpucolor

def ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 1))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address



webstats = webserver()
cpuTemp = CPUTemp()
sqlstats = SQLServer()

layout = [  [sg.Text('Websever Status:'), sg.Text(webstats[0], text_color=webstats[1] , key="webstat"), sg.Button("Start Webserver", visible = webstats[2], key = "webvis")],
            [sg.Text('SQL Server Status:'), sg.Text(sqlstats[0], text_color=sqlstats[1] , key="sqlstat"), sg.Button("Start SQL", visible = sqlstats[2], key = "sqlvis")],
            [sg.Text('CPU Temp:'), sg.Text(cpuTemp[0], text_color=cpuTemp[1] , key="cpuTemp")],
            [sg.Text('IP address:'), sg.Text(ip(), text_color="grey", key="ip")],
            [sg.Button('Exit')] ]

window = sg.Window('Plant Life Monitor Console', layout)
i = 0
while True:
    event, values = window.read(timeout = 10)
    window.Refresh()
    
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "webvis":
        print("Starting Webserver")
        os.system("sudo systemctl start PMW.service")
    elif event == "sqlvis":
        print("Starting SQL")
        os.system("sudo systemctl start mysql.service")
    event, values = window.read(timeout = 10)
    if event == sg.TIMEOUT_KEY:
        time.sleep(0.05)
        window['webstat'].update(webserver()[0], text_color = webserver()[1])
        window['webvis'].update(visible = webserver()[2])
        window['sqlstat'].update(SQLServer()[0], text_color = SQLServer()[1])
        window['sqlvis'].update(visible = SQLServer()[2])
        window['cpuTemp'].update(CPUTemp()[0], text_color = CPUTemp()[1])
        window['ip'].update(ip())
        i+=1

window.close()
