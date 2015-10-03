# RaspbianGardenWaterControl
The smart garden irrigation water timer for the Raspberry Pi running Raspbian

This was tested on a RPi2 with the latest Raspbian Jessie 9/24/2015
Uses python3, RPi.GPIO, forecast.io (needs an API key and your latitude/longitude) - no message queue yet
This version is able to save the schedule dictionary to a file so it survives across reboots!
Also got rid of the dangerous ignore ssh cert context for getting the weather forecast. 
