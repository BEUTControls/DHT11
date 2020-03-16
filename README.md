# DHT11
Found this to be a good site - 
https://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/

git clone https://github.com/adafruit/Adafruit_Python_DHT.git

cd Adafruit_Python_DHT

sudo apt-get install build-essential python-dev

sudo python setup.py install
to use python3
sudo pip3 install Adafruit_DHT

cd to your favorite directory
cd /home/pi/BEUT
sudo nano DHT11.py

#!/usr/bin/python
import sys
import Adafruit_DHT
while True:
  import humidity, temperature = Adafruit_DHT.read_retry(11, 4)
  F = ((temperature * 1.8) + 32)
  print ('Temp: {0:0.1f} C Humidity: {1:0.1f} %'.format(F, humidity))
  print ("Temperature in C: " ,temperature)
