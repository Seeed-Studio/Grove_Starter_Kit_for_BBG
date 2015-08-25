# ADXL345 Python example 
# This is an example to show you how to the Grove +-16g Accelerometer

import time
from adxl345 import ADXL345

if __name__ == "__main__":

    adxl345 = ADXL345()

    while True:
        axes = adxl345.getAxes(True)
        print "ADXL345 on address 0x%x:" % (adxl345.address)
        print "   x = %.3fG" % ( axes['x'] )
        print "   y = %.3fG" % ( axes['y'] )
        print "   z = %.3fG" % ( axes['z'] )
        time.sleep(1)