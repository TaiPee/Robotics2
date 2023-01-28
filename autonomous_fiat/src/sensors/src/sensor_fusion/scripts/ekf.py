import numpy as np
import math

class extended_kf():
    """
    
    x: the state is a concatenation of position and velicity

    Covariance matrices
    Q: process variance (IMU-accelometer)
    R: measurement variance (GPS)

    """

    def __init__(self, initial_position, initial_velocity, position_std_dev ,acceleration_std_dev, time):

        self.x = np.array([[initial_position], [initial_velocity]]) # x denotes the state

        # initial covariance guess
        self.P = np.identity(2)

        # transformation matrix for input data
        self.H = np.identity(2)

        acceleration_var = acceleration_std_dev #* acceleration_std_dev
        self.Q = np.array([[acceleration_var, 0], [0, acceleration_var]])

        position_var = position_std_dev #* position_std_dev
        self.R = np.array([[position_var, 0], [0, position_var]])

        self.current_time = time

        pass
    
    def predict(self, acceleration, time):
        """
        A: describes the nominal state kinematics - static transition
        B: describes the nominal state kinematics - control matrix
        """
        delta_t = time - self.current_time

        # predicted state estimate
        self.A = np.array([[1.0, delta_t], [0.0, 1.0]]) 
        self.B = np.array([[0.5 * delta_t * delta_t], [delta_t]])
        self.u = np.array([[acceleration]])
        self.x = np.add(np.matmul(self.A, self.x), np.matmul(self.B, self.u))

        # predicted covariance estimate
        self.P = np.add(np.matmul(np.matmul(self.A, self.P), np.transpose(self.A)), self.Q)

        # 
        self.current_time = time

    def update(self, position, velocity, position_error, velocity_error):
        """
        z: denotes the measured state
        """

        self.z = np.array([[position], [velocity]])

        # measurement residual
        state_error = np.subtract(self.z, self.x)

        # residual covariance
        if(not position_error):
            self.R[0, 0] = position_error #* position_error
        else:
            self.R[1, 1] = velocity_error #* velocity_error

        # near-optimal Kalman Gain
        s = np.add(self.P, self.R)
        try:
            s_inverse = np.linalg.inv(s)
        except np.linalg.LinAlgError:
            pass
        else:
            # s_inverse = np.eye(2)
            K = np.matmul(self.P, s_inverse)

            # updated state estimate
            self.x = np.add(self.x, np.matmul(K, state_error))

            # update covariance estimate
            self.P = np.matmul(np.subtract(np.identity(2), K), self.P)

    def get_position(self):
        '''
        Returns predicted position in the current axis.
        '''
        return self.x[0, 0]

    def get_velocity(self):
        '''
        Returns predicted velocity in the current axis.
        '''
        return self.x[1, 0]