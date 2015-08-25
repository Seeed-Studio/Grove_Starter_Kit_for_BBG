 # grove_button.py
 # Beaglebone Green Python library

 # Copyright (c) 2015 seeed technology inc.
 # Website    : www.seeed.cc
 # Author     : Wuruibin
 # Created Time: July 2015
 # Modified Time:
 
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
from logo import print_seeedstudio
import Adafruit_BBIO.GPIO as GPIO

# Note: Use P9_22(UART2_RXD) as GPIO.
# Connect the Grove Button to UART Grove port of Beaglebone Green.
Button = "P9_22"            # GPIO P9_22
GPIO.setup(Button, GPIO.IN)

if __name__== '__main__':
    print_seeedstudio()

    while True:
        if GPIO.input(Button):
            print "Button is pressed."
            time.sleep(1)
        else:
            print "Button is unstuck."
            time.sleep(1)