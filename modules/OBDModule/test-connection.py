
import obdreader
import time


while True:
    msg = obdreader.getVehicleTelemtries("test-connection")
    if(msg is not None):
        print(msg)
    else:
        print("cannot get obd data")
    time.sleep(1)