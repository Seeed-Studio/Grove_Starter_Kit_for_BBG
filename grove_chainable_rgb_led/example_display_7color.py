 # example_display_7color.py
 # Beaglebone Green Python library

 # Copyright (c) 2015 seeed technology inc.
 # Website    : www.seeed.cc
 # Author     : Wuruibin
 # Created Time: August 2015
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
#from logo import print_seeedstudio
import grove_chainable_rgb_led

CLK_PIN = "P9_22"
DATA_PIN = "P9_21"
NUMBER_OF_LEDS = 1


# Note: Use P9_22(UART2_RXD) and P9_21(UART2_TXD) as GPIO.
# Connect the Grove - Chainable RGB LED to UART Grove port of Beaglebone Green.
if __name__ == "__main__":
    #print_seeedstudio()

    rgb_led = grove_chainable_rgb_led.ChainableLED(CLK_PIN, DATA_PIN, NUMBER_OF_LEDS)
    
    while True:
        try:
            # The first parameter: NUMBER_OF_LEDS - 1; Other parameters: the RGB values.
            rgb_led.setColorRGB(0, 255, 0, 0)
            time.sleep(2)
            rgb_led.setColorRGB(0, 0, 255, 0)
            time.sleep(2)
            rgb_led.setColorRGB(0, 0, 0, 255)
            time.sleep(2)
            rgb_led.setColorRGB(0, 0, 255, 255)
            time.sleep(2)
            rgb_led.setColorRGB(0, 255, 0, 255)
            time.sleep(2)
            rgb_led.setColorRGB(0, 255, 255, 0)
            time.sleep(2)
            rgb_led.setColorRGB(0, 255, 255, 255)
            time.sleep(2)
        
        except KeyboardInterrupt:
            rgb_led.setColorRGB(0, 0, 0, 0)
            break

        except IOError:
            print "Error"
        
                
                
                
                