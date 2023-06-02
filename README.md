# PlantLifeMonitor
- Made to be ran on a raspbery pi 
- Uses communication via an Arduino UNO to control sensors 

## Dependentcies:
- MYSQL or MARIADB
- Flask
- NGINX or APACHE 

## Python imports:
- Pyserial
- chartjs
- croniter

Flask needs to be installed into this directory for the program to run correctly.

## Rundown of the files
- DB.py file talks to the SQL DB
- Coms.py - file talks to the arduino
- Application.py - file serves the HTML files found in the templates folder
- Calcs.py - calls for the Coms.py file and the DB.py file to determin if the plant needs watering or not
- Predictions.py - predicts if the plant needs watering or not
- Update.sh - Runs the Application.py file in a python virtual enviroment

## How they interconnect

![image8](https://github.com/Fox2low/PlantLifeMonitor/assets/77130209/5fc0fdcc-7005-468a-aab4-4dfee0b14302)

## Get the ISO file for the full prebuilt OS here:
 https://drive.google.com/file/d/1BN1muYDiF5sIKCxGLZ_ClekoyyZy8rxy/view?usp=share_link

## Wiring Diagrams
<img width="809" alt="image1" src="https://github.com/Fox2low/PlantLifeMonitor/assets/77130209/9c5bb04a-b585-4f4a-8d82-b04b01bec030">
<img width="494" alt="image3" src="https://github.com/Fox2low/PlantLifeMonitor/assets/77130209/1ca25420-bffc-4a28-b238-585e3d5be27e">

## Webpage
![image5](https://github.com/Fox2low/PlantLifeMonitor/assets/77130209/23b9f0d5-69e7-4895-983a-e45ec207327c)

## Flow Chart
<img width="404" alt="image6" src="https://github.com/Fox2low/PlantLifeMonitor/assets/77130209/1c65709a-15fb-41a2-89e8-b01a4319efaa">

## Roadmap
![image4](https://github.com/Fox2low/PlantLifeMonitor/assets/77130209/67a1b72d-6b3f-479f-b270-be127c6eb903)





