#!/usr/bin/python

import json
import os
import sys
import re

# Variables
install_location = '/home/pi/.homeassistant'

def import_entity():
    global entities
    try:
        os.popen('cp core.entity_registry core.entity_registry.bak')
    except:
        sys.exit('ERROR - Could not create backup of core.entity_registry')

    with open('core.entity_registry') as json_file:
        entities = json.load(json_file)

def import_devices():
    global devices
    try:
        os.popen('cp core.device_registry core.device_registry.bak')
    except:
        sys.exit('ERROR - Could not create backup of core.device_registry')

    with open('core.device_registry') as json_file:
        devices = json.load(json_file)

def write_devices():
    global devices

    print('Writing the device registry')
    try:
        with open('core.device_registry', 'w') as outfile:
            json.dump(devices, outfile, indent=2)
    except:
        sys.exit('ERROR - Could not write device registry')

def main():
    os.chdir(install_location + '/.storage')

    import_entity()
    import_devices()

    # Identify devices with more than one entity
    device_to_update = []

    for entity in entities['data']['entities']:
        if re.search("^switch.*", entity['entity_id']) or re.search("^light.*", entity['entity_id']) or re.search("^binary_sensor.*", entity['entity_id']):
            device_to_update.append(entity)
            print(entity)

    for device in devices['data']['devices']:
        for d in device_to_update:
            if d['device_id'] == device['id']:
                print('Device: ' + device['id'])
                if device['name_by_user']:
                    print('Old name: ' + device['name_by_user'])
                try:
                    device['name_by_user'] = d['name']
                    print('New name: ' + device['name_by_user'])
                except:
                    break

    write_devices()

    print('Success')

if __name__ == '__main__':
    try:
        main()
    except:
        print('Fatal error in main loop')
