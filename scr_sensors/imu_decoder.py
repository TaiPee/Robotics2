import math

# Quaternion values from the IMU sensor
qw = 0.9848
qx = 0.1736
qy = 0.0044
qz = 0.0002

# Calculate pitch, yaw, and roll
pitch = math.asin(2 * (qw * qy - qx * qz))
yaw = math.atan2(2 * (qw * qz + qx * qy), qw * qw - qx * qx - qy * qy + qz * qz)
roll = math.atan2(2 * (qw * qx + qy * qz), qw * qw + qx * qx - qy * qy - qz * qz)

# Acceleration values from the IMU sensor
ax = 0.1
ay = 0.2
az = 0.3

# Calculate acceleration north, east, and down
an = ax * math.cos(pitch) + az * math.sin(pitch)
ae = ay * math.cos(roll) + ax * math.sin(roll) * math.sin(pitch) + az * math.sin(roll) * math.cos(pitch)
ad = ay * math.sin(roll) + ax * math.cos(roll) * math.sin(pitch) + az * math.cos(roll) * math.cos(pitch)

print("Pitch: ", pitch)
print("Yaw: ", yaw)
print("Roll: ", roll)
print("Acceleration North: ", an)
print("Acceleration East: ", ae)
print("Acceleration Down: ", ad)
