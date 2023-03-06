import os

files = os.listdir("/home/pi/Documents/Programming/www/static/images")
length = len(files)
cmd = "sudo fswebcam image" + str(int(length) + 1) + ".jpg" 
os.system("ls")
os.chdir("/home/pi/Documents/Programming/www/static/images")
os.system(cmd)