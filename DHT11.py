#!/usr/bin/python
import sys
import Adafruit_DHT
while True:
  import humidity, temperature = Adafruit_DHT.read_retry(11, 4)
  F = ((temperature * 1.8) + 32)
  print ('Temp: {0:0.1f} C Humidity: {1:0.1f} %'.format(F, humidity)
  print ("Temperature in C: " ,temperature)
