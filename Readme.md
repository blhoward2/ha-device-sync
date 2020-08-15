In Home Assistant, it is much easier to rename entities during zwave pairing than devices, which requires many more steps. This script copies over all custom entity names for switches, lights, and binary_sensors to the corresponding device.

No warranties, though it does make a backup of both core files on each run.

Define the installation location at the top in install_location. This should point to the hidden folder for HA. No idea if this works on Hass as I’m using Raspbian.

Usage:

1. Download the device_sync.py file and place it anywhere on the system
2. Run python3 device_sync.py as a user with write access to HA
3. Restart the HA server 
