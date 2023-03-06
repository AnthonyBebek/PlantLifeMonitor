# PlantLifeMonitor
-- Made to be ran on a raspbery pi --
-- Uses communication via an Arduino UNO to control sensors --

Dependentcies:
-- MYSQL or MARIADB
-- Flask
-- NGINX or APACHE 

Python imports:
-- Pyserial
-- chartjs
-- croniter

Flask needs to be installed into this directory for the program to run correctly.

-- Rundown of the files -- 
DB.py - file talks to the SQL DB
Coms.py - file talks to the arduino
Application.py - file serves the HTML files found in the templates folder
Calcs.py - calls for the Coms.py file and the DB.py file to determin if the plant needs watering or not
Predictions.py - predicts if the plant needs watering or not
Update.sh - Runs the Application.py file in a python virtual enviroment
