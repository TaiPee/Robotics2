import math

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