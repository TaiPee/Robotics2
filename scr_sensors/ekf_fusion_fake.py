import json
import numpy as np
from ekf import extended_kf
from helperMethods import helperMethods
import matplotlib.pyplot as plt

# setting some constants
ACTUAL_GRAVITY = 9.80665

file_name = 'fake_data.json'

with open(file_name) as data_file:
    data = json.load(data_file)

    # read initial data
    initial_data = data[0]

    # create object of helper class
    helperObj = helperMethods()

    # set standard deviations
    latLonStdDev = 2.0
    altStdDev = 3.518522417151836
    accEastStdDev = ACTUAL_GRAVITY * 0.033436506994600976
    accNorthStdDev = ACTUAL_GRAVITY * 0.05355371135598354
    accUpStdDev = ACTUAL_GRAVITY * 0.2088683796078286

    # kf_north = extended_kf(helperObj.lonToMtrs(initial_data["gps_lon"]), \
    #                   initial_data["vel_east"], latLonStdDev, \
    #                   accEastStdDev, initial_data["timestamp"])
    # kf_east = extended_kf(helperObj.latToMtrs(initial_data["gps_lat"]), \
    #                   initial_data["vel_north"], latLonStdDev, \
    #                   accNorthStdDev, initial_data["timestamp"])
    # kf_down = extended_kf(initial_data["gps_alt"], \
    #                   initial_data["vel_down"] * -1.0, latLonStdDev, \
    #                   accUpStdDev, initial_data["timestamp"])


    kf_north = extended_kf(helperObj.lonToMtrs(initial_data["gps_lon"]), \
                      0, latLonStdDev, \
                      accEastStdDev, initial_data["timestamp"])
    kf_east = extended_kf(helperObj.latToMtrs(initial_data["gps_lat"]), \
                      0, latLonStdDev, \
                      accNorthStdDev, initial_data["timestamp"])
    kf_down = extended_kf(initial_data["gps_alt"], \
                      0 * -1.0, latLonStdDev, \
                      accUpStdDev, initial_data["timestamp"])
    
    # save previous
    prevTime = initial_data["timestamp"]
    prevEast = helperObj.latToMtrs(initial_data["gps_lat"])
    prevNorth = helperObj.lonToMtrs(initial_data["gps_lon"])
    
    # lists for collecting final points to plot
    pointsToPlotLat = []
    pointsToPlotLon = []

    # lists for plotting original data points
    orgLat = []
    orgLon = []

    # run loop over new readings
    for i in range(1,len(data)): #len(data)
        prevData = data[i-1]
        currData = data[i]

        # call the predict function for all objects 
        # (since we already have the first reading, we call call predict)
        kf_east.predict(currData["abs_east_acc"] * ACTUAL_GRAVITY, 
                        currData["timestamp"])
        kf_north.predict(currData["abs_north_acc"] * ACTUAL_GRAVITY,
                        currData["timestamp"])
        kf_down.predict(currData["abs_up_acc"] * ACTUAL_GRAVITY,
                        currData["timestamp"])

        # if GPS data is not zero, proceed
        if(currData["gps_lat"] != 0.0):

            delta_time = prevTime

            defPosErr = 0.0
            # call the update function for all objects
            vEast = currData["vel_east"]
            longitude = kf_east.lonToMtrs(currData["gps_lon"])
            kf_east.update(longitude, vEast, defPosErr, currData["vel_error"])

            vNorth = currData["vel_north"]
            latitude = kf_north.latToMtrs(currData["gps_lat"])
            kf_north.update(latitude, vNorth, defPosErr, currData["vel_error"])

            vUp = currData["vel_down"] * -1.0
            kf_down.update(currData["gps_alt"], vUp, currData["altitude_error"], 
                        currData["vel_error"])
            # append original points to plot
            orgLat.append(currData["gps_lat"])
            orgLon.append(currData["gps_lon"])


            # save previous
            prevTime = currData["timestamp"]
            prevEast = longitude
            prevNorth = latitude
            

        # get predicted values
        predictedLonMtrs = kf_east.get_position()
        predictedLatMtrs = kf_north.get_position()
        predictedAlt = kf_down.get_position()

        predictedLat, predictedLon = helperObj.mtrsToGeopoint(predictedLatMtrs,
                                                                predictedLonMtrs)

        predictedVE = kf_east.get_velocity()
        predictedVN = kf_north.get_velocity()

        resultantV = np.sqrt(np.power(predictedVE, 2) + np.power(predictedVN, 2))
        deltaT = currData["timestamp"] - initial_data["timestamp"]

        # print("{} seconds in, Lat: {}, Lon: {}, Alt: {}, Vel(mph): {}".format(
        #         deltaT, predictedLat, predictedLon, predictedAlt, resultantV))

        # append predicted points to list
        pointsToPlotLat.append(predictedLat)
        pointsToPlotLon.append(predictedLon)
        
        
            # plt.scatter(predictedLat, predictedLon)
        # plt.scatter(currData["gps_lat"], currData["gps_lon"])
        # plt.pause(0.0001)
        # # plt.xlim([37, 41])
        # # plt.ylim([-125, -122])

        # plt.xlim([0.0077+37.94, 0.0092+37.94])
        # plt.ylim([-0.0076-1.2204e2, -0.0095-1.2204e2])

print(len(orgLat))
pLa = orgLat[::10]
pLo = orgLon[::10]
for j in range(len(pLa)):
    plt.scatter(pLa[j],pLo[j])
    plt.pause(0.001)
    plt.xlim([0.0077+37.94, 0.0092+37.94])
    plt.ylim([-0.0076-1.2204e2, -0.0095-1.2204e2])
plt.show()

# print(len(orgLat))
pLa = pointsToPlotLat[::10]
pLo = pointsToPlotLon[::10]
for j in range(len(pLa)):
    plt.scatter(pLa[j],pLo[j])
    plt.pause(0.001)
    plt.xlim([0.0077+37.94, 0.0092+37.94])
    plt.ylim([-0.0076-1.2204e2, -0.0095-1.2204e2])
plt.show()

plt.show()
plt.subplot(2,1,1)
plt.title('Original')
plt.plot(orgLat, orgLon)



plt.subplot(2,1,2)
plt.title('Fused')
plt.plot(pointsToPlotLat, pointsToPlotLon)

plt.show()