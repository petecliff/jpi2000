#!/usr/bin/env python

import bme680
import json
import datetime
import requests
import os

sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)

sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)
sensor.set_gas_status(bme680.DISABLE_GAS_MEAS)

sensor.set_gas_heater_temperature(320)
sensor.set_gas_heater_duration(150)
sensor.select_gas_heater_profile(0)

ingestUrl = os.getenv('INGEST_URL')

reading = {}
reading['dev_eui'] = 'demo_device_1'
reading['type'] = 'jp2001'
reading['timestamp'] = datetime.datetime.utcnow().replace(microsecond=0).isoformat()

notRead = True

while notRead:
    if sensor.get_sensor_data():
        reading['temperature'] = '{0:.2f}'.format(sensor.data.temperature)
        reading['humidity'] = '{0:.2f}'.format(sensor.data.humidity)
        reading['pressure'] = '{0:.2f}'.format(sensor.data.pressure)
        notRead = False

result = requests.post(ingestUrl, data=json.dumps(reading))
print(json.dumps(reading))
print(result)

