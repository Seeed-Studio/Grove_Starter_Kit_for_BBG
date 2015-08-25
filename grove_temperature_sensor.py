 # grove_temperature_sensor.py
 # Beaglebone Green Python library

 # Copyright (c) 2015 seeed technology inc.
 # Website    : www.seeed.cc
 # Author     : Wuruibin
 # Created Time: July 2015
 # Modified Time: August 2015
 
 # The MIT License (MIT)

 # Permission is hereby granted, free of charge, to any person obtaining a copy
 # of this software and associated documentation files (the "Software"), to deal
 # in the Software without restriction, including without limitation the rights
 # to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 # copies of the Software, and to permit persons to whom the Software is
 # furnished to do so, subject to the following conditions:

 # The above copyright notice and this permission notice shall be included in
 # all copies or substantial portions of the Software.

 # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 # THE SOFTWARE.


#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import math
from logo import print_seeedstudio
import grove_i2c_adc
import Adafruit_BBIO.GPIO as GPIO

BUZZER = "P9_22"            # GPIO P9_22
GPIO.setup(BUZZER, GPIO.OUT)

# The threshold to turn the buzzer on 28 Celsius
THRESHOLD_TEMPERATURE = 28

adc = grove_i2c_adc.I2cAdc()

#   The argument in the read_temperature() method defines which Grove board(Grove Temperature Sensor) version you have connected.
#   Defaults to 'v1.2'. eg.
#       temp = read_temperature('v1.0')          # B value = 3975
#       temp = read_temperature('v1.1')          # B value = 4250
#       temp = read_temperature('v1.2')          # B value = 4250
def read_temperature(model = 'v1.2'):
    "Read temperature values in Celsius from Grove Temperature Sensor"
    # each of the sensor revisions use different thermistors, each with their own B value constant
    if model == 'v1.2':
        bValue = 4250  # sensor v1.2 uses thermistor ??? (assuming NCP18WF104F03RC until SeeedStudio clarifies)
    elif model == 'v1.1':
        bValue = 4250  # sensor v1.1 uses thermistor NCP18WF104F03RC
    else:
        bValue = 3975  # sensor v1.0 uses thermistor TTC3A103*39H

    total_value = 0
    for index in range(20):
        sensor_value = adc.read_adc()
        total_value += sensor_value
        time.sleep(0.05)
    average_value = float(total_value / 20)

    # Transform the ADC data into the data of Arduino platform.
    sensor_value_tmp = (float)(average_value / 4095 * 2.95 * 2 / 3.3 * 1023)
    resistance = (float)(1023 - sensor_value_tmp) * 10000 / sensor_value_tmp
    temperature = round((float)(1 / (math.log(resistance / 10000) / bValue + 1 / 298.15) - 273.15), 2)
    return temperature

# Function: If the temperature sensor senses the temperature that is up to the threshold you set in the code, the buzzer is ringing for 1s.
# Hardware: Grove - I2C ADC, Grove - Temperature Sensor, Grove - Buzzer
# Note: Use P9_22(UART2_RXD) as GPIO.
# Connect the Grove Buzzer to UART Grove port of Beaglebone Green.
# Connect the Grove - I2C ADC to I2C Grove port of Beaglebone Green, and then connect the Grove - Temperature Sensor to Grove - I2C ADC.
if __name__ == '__main__':
    print_seeedstudio()

    while True:
        try:
            # Read temperature values in Celsius from Grove Temperature Sensor
            temperature = read_temperature('v1.2')
            
            # When the temperature reached predetermined value, buzzer is ringing.
            if temperature > THRESHOLD_TEMPERATURE:
                # Send HIGH to switch on BUZZER
                GPIO.output(BUZZER, GPIO.HIGH)
            else:
                # Send LOW to switch off BUZZER
                GPIO.output(BUZZER, GPIO.LOW)
            
            print "temperature = ", temperature
            
        except KeyboardInterrupt:
            GPIO.output(BUZZER, GPIO.LOW)
            break

        except IOError:
            print "Error"

