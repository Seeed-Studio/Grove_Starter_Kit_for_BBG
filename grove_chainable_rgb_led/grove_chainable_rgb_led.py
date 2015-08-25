 # grove_chainable_rgb_led.py
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
from logo import print_seeedstudio
import Adafruit_BBIO.GPIO as GPIO

CLK_PIN = "P9_22"
DATA_PIN = "P9_21"
NUMBER_OF_LEDS = 1

class ChainableLED():
    def __init__(self, clk_pin, data_pin, number_of_leds):
        self.__clk_pin = clk_pin
        self.__data_pin = data_pin
        self.__number_of_leds = number_of_leds
        
        GPIO.setup(self.__clk_pin, GPIO.OUT)
        GPIO.setup(self.__data_pin, GPIO.OUT)
        
        for i in range(self.__number_of_leds):
            self.setColorRGB(i, 0, 0, 0)
            
    def clk(self):
        GPIO.output(self.__clk_pin, GPIO.LOW)
        time.sleep(0.00002)
        GPIO.output(self.__clk_pin, GPIO.HIGH)
        time.sleep(0.00002)

    def sendByte(self, b):
        "Send one bit at a time, starting with the MSB"
        for i in range(8):
            # If MSB is 1, write one and clock it, else write 0 and clock
            if (b & 0x80) != 0:
                GPIO.output(self.__data_pin, GPIO.HIGH)
            else:
                GPIO.output(self.__data_pin, GPIO.LOW)
            self.clk()

            # Advance to the next bit to send
            b = b << 1
            
    def sendColor(self, red, green, blue):
        "Start by sending a byte with the format '1 1 /B7 /B6 /G7 /G6 /R7 /R6' "
        #prefix = B11000000
        prefix = 0xC0
        if (blue & 0x80) == 0:     
            #prefix |= B00100000
            prefix |= 0x20
        if (blue & 0x40) == 0:     
            #prefix |= B00010000
            prefix |= 0x10
        if (green & 0x80) == 0:    
            #prefix |= B00001000
            prefix |= 0x08
        if (green & 0x40) == 0:    
            #prefix |= B00000100
            prefix |= 0x04
        if (red & 0x80) == 0:      
            #prefix |= B00000010
            prefix |= 0x02
        if (red & 0x40) == 0:      
            #prefix |= B00000001
            prefix |= 0x01
        self.sendByte(prefix)
        
        # Now must send the 3 colors
        self.sendByte(blue)
        self.sendByte(green)
        self.sendByte(red)
        
    def setColorRGB(self, led, red, green, blue):
        # Send data frame prefix (32x '0')
        self.sendByte(0x00)
        self.sendByte(0x00)
        self.sendByte(0x00)
        self.sendByte(0x00)
        
        # Send color data for each one of the leds
        for i in range(self.__number_of_leds):
            '''
            if i == led:
                _led_state[i*3 + _CL_RED] = red;
                _led_state[i*3 + _CL_GREEN] = green;
                _led_state[i*3 + _CL_BLUE] = blue;

            sendColor(_led_state[i*3 + _CL_RED], 
                      _led_state[i*3 + _CL_GREEN], 
                      _led_state[i*3 + _CL_BLUE]);
            '''
            self.sendColor(red, green, blue)

        # Terminate data frame (32x "0")
        self.sendByte(0x00)
        self.sendByte(0x00)
        self.sendByte(0x00)
        self.sendByte(0x00)


# Note: Use P9_22(UART2_RXD) and P9_21(UART2_TXD) as GPIO.
# Connect the Grove - Chainable RGB LED to UART Grove port of Beaglebone Green.
if __name__ == "__main__":
    print_seeedstudio()

    rgb_led = ChainableLED(CLK_PIN, DATA_PIN, NUMBER_OF_LEDS)
    
    while True:
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
        
        
                
                
                
                