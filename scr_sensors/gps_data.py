import time
from pyicloud import PyiCloudService
from geonav_conversions import *
import matplotlib.pyplot as plt

try:
    api = PyiCloudService('blourenco217@gmail.com', 'applexecDIP853')
except KeyboardInterrupt:
    exit()

time.sleep(5)

org_north = []
org_east = []
org_error = []

current_ts = 0
device = api.devices[1]

i = 0
while i<10:
    location = device.location()
    if location['positionType'] == 'GPS' and location['timeStamp'] != current_ts:
        print(location['latitude'], location['longitude'])
        print(location['horizontalAccuracy'])
        current_ts = location['timeStamp']
        lat = location['latitude']
        lon = location['longitude']
        north, east, _ = LLtoUTM(lat, lon)
        org_north.append(north)
        org_east.append(east)
        org_error.append(location['horizontalAccuracy'])
    
        i = i + 1
        plt.scatter(north, east)

        # define a suitable window
        # plt.xlim([0.0077+37.94, 0.0092+37.94])
        # plt.ylim([-0.0076-1.2204e2, -0.0095-1.2204e2])


plt.show()

for i in range(len(org_north)):
    plt.scatter(org_north[i],org_east[i])
    plt.pause(0.001)
plt.show()
