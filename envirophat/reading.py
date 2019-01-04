#!/usr/bin/env python

import os
import requests
import time
import datetime
import json

from envirophat import light, weather, motion, analog, leds

leds.on()

ingestUrl = os.getenv('INGEST_URL')
unit = 'hPa' # Pressure unit, can be either hPa (hectopascals) or Pa (pascals)

reading = {}
reading['dev_eui'] = 'demo_device_2'
reading['type'] = 'jp2002'
reading['timestamp'] = datetime.datetime.utcnow().replace(microsecond=0).isoformat()

r,g,b = light.rgb()

ax, ay, az = motion.accelerometer()

mx, my, mz = motion.magnetometer()

reading['light'] = light.light()
reading['rgb'] = '#{0:02x}{1:02x}{2:02x}'.format(r,g,b)
reading['magnetometer'] = str(mx) + 'mx ' + str(my) + 'my ' + str(mz) + 'mz' 
reading['accelerometer'] = str(ax) + 'ax ' + str(ay) + 'ay ' + str(az) + 'az'
reading['altitude'] = '{0:.2f}'.format(weather.altitude())
reading['temperature'] = '{0:.2f}'.format(weather.temperature())
reading['pressure'] = '{0:.2f}'.format(weather.pressure(unit=unit))

try: 
    leds.off()
    result = requests.post(ingestUrl, data=json.dumps(reading))
    leds.on()
    time.sleep(0.5)
    print(result)
    leds.off()
except:
    print 'Network error'

print (json.dumps(reading))

leds.off()

