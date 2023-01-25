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


def to_yaw_pitch_roll():

    return

std::tuple<float,float,float> ekfNavINS::getPitchRollYaw(float ax, float ay, float az, float hx, float hy, float hz) {
  // initial attitude and heading
  theta = asinf(ax/G);
  phi = -asinf(ay/(G*cosf(theta)));
  // magnetic heading correction due to roll and pitch angle
  Bxc = hx*cosf(theta) + (hy*sinf(phi) + hz*cosf(phi))*sinf(theta);
  Byc = hy*cosf(phi) - hz*sinf(phi);
  // finding initial heading
  psi = -atan2f(Byc,Bxc);
  return (std::make_tuple(theta,phi,psi));
}