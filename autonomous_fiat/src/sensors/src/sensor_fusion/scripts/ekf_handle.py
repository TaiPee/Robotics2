import math
import numpy as np

def euler_to_quaternion(yaw, pitch, roll):
    cy = math.cos(yaw * 0.5)
    sy = math.sin(yaw * 0.5)
    cp = math.cos(pitch * 0.5)
    sp = math.sin(pitch * 0.5)
    cr = math.cos(roll * 0.5)
    sr = math.sin(roll * 0.5)

    w = cr * cp * cy + sr * sp * sy; # w
    x = cr * cp * sy - sr * sp * cy; # x
    y = cr * sp * cy + sr * cp * sy; # y
    z = sr * cp * cy - cr * sp * sy; # z

    return w, x, y, z

def quaternion_to_euler(qw, qx, qy, qz):
    pitch = math.asin(2 * (qw * qy - qx * qz))
    yaw = math.atan2(2 * (qw * qz + qx * qy), qw * qw - qx * qx - qy * qy + qz * qz)
    roll = math.atan2(2 * (qw * qx + qy * qz), qw * qw + qx * qx - qy * qy - qz * qz)
    return yaw, pitch, roll

def get_accelaration(ax, ay, az, yaw, pitch, roll):
    # Calculate acceleration north, east, and down
    an = ax * math.cos(pitch) + az * math.sin(pitch)
    ae = ay * math.cos(roll) + ax * math.sin(roll) * math.sin(pitch) + az * math.sin(roll) * math.cos(pitch)
    ad = ay * math.sin(roll) + ax * math.cos(roll) * math.sin(pitch) + az * math.cos(roll) * math.cos(pitch)
    return an, ae, ad





EARTH_RADIUS = 6371 * 1000.0 # meters


def latToMtrs(latitude):
    '''
    Converts Latitude to Meters
    '''
    distance = getDistMtrs(latitude, 0.0, 0.0, 0.0)
    if(distance < 0):
        distance *= -1

    return distance

def lonToMtrs(longitude):
    '''
    Converts Longitiude to Meters
    '''
    distance = getDistMtrs(0.0, longitude, 0.0, 0.0)
    if(longitude < 0):
        distance *= -1

    return distance

def degToRad(latOrLon):
    '''
    Converts Degrees to Radians
    '''

    return (latOrLon * np.pi) / 180.0

def radToDeg(latOrLon):
    '''
    Converts radians to degrees
    '''
    
    return (latOrLon * 180.0) / np.pi

def getDistMtrs(lat_from, lon_from, lat_to, lon_to):
    '''
    Get distance between two GPS points
    '''
    deltaLon = degToRad(lon_to - lon_from)
    deltaLat = degToRad(lat_to - lat_from)

    a = np.power(np.sin(deltaLat/2.0), 2) + \
          np.cos(degToRad(lat_from)) * np.cos(degToRad(lat_to)) * \
              np.power(np.sin(deltaLon/2.0), 2)
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1.0 - a))

    return EARTH_RADIUS * c

def getPointAhead(lat_from, lon_from, distMtrs, azimuth):
    '''
    Helper function for mtrsToGeopoint
    '''
    radiusFraction = distMtrs / EARTH_RADIUS
    bearing = degToRad(azimuth)
    lat1 = degToRad(lat_from)
    lon1 = degToRad(lon_from)

    lat2_part1 = np.sin(lat1) * np.cos(radiusFraction)
    lat2_part2 = np.cos(lat1) * np.sin(radiusFraction) * np.cos(bearing)

    lat2 = np.arcsin(lat2_part1 + lat2_part2)

    lon2_part1 = np.sin(bearing) * np.sin(radiusFraction) * np.cos(lat1)
    lon2_part2 = np.cos(radiusFraction) - (np.sin(lat1) * np.sin(lat2))

    lon2 = lon1 + np.arctan2(lon2_part1, lon2_part2)
    lon2 = np.mod((lon2 + 3 * np.pi), (2 * np.pi)) - np.pi

    return radToDeg(lat2), radToDeg(lon2)


def mtrsToGeopoint(latAsMtrs, lonAsMtrs):
    '''
    Conversion between GPS points to meters
    '''
    lat_tmp, lon_tmp = getPointAhead(0.0, 0.0, lonAsMtrs, 90.0)
    lat_ret, lon_ret = getPointAhead(lat_tmp, lon_tmp, latAsMtrs, 0.0)

    return lat_ret, lon_ret