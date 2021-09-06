#!/usr/bin/env python3

from visual_kinematics.RobotSerial import *
import numpy as np
from math import pi
import os, sys

def forward_vk(robot, theta_degree):
    print("-------forward-------")
    print(f"[Input] theta_degree:{theta_degree}")
   
    f = robot.forward(np.radians(theta_degree))

    xyz1 = f.t_3_1
    [x1, y1, z1] = xyz1

    abc1 = f.euler_3
    abc_degree1 = np.degrees(abc1)

    print(f"[Output] xyz: {xyz1.reshape(1,-1)}, abc_degree: {abc_degree1}")
    return xyz1, abc_degree1

def inverse_vk(robot, xyz, abc_degree):    
    print("-------inverse-------")
    print(f"[Input] xyz: {xyz.reshape(1,-1)}, abc_degree: {abc_degree}")

    end = Frame.from_euler_3(np.radians(abc_degree), xyz)
    robot.inverse(end)
    theta_degree = np.degrees(robot.axis_values)

    print(f"inverse successful: {robot.is_reachable_inverse}")
    print(f"[Output] theta: {theta_degree}")    
    return theta_degree

def main():

    if (len(sys.argv) > 2):
        x = float(sys.argv[1])  # "../../data/all_ctru_data_info_filtered_by_qc.16.npy"
        y = float(sys.argv[2])
        z = float(sys.argv[3])
    else:
        print(f"Usage: {sys.argv[0]} x y z")
        print(f"Example: {sys.argv[0]} 0.3 0.2 0.4")
        exit()


    np.set_printoptions(precision=3, suppress=True)

    # scale arm length in a number between 0 and 1, because of the plot assuming that range
    a0 = 0.5
    a1 = 0.2
    a2 = 0.3
    a3 = 0.4
    
    dh_params = np.array([[a0, 0, 0, 0],
                          [0, 0, pi/2, 0],
                          [0, a1, 0, 0],
                          [0, a2, 0, -pi/2],
                          [a3, 0, -pi/2, 0]])


    print("====================== First inverse, then forward, press any key to continue  ======================")
    xyz = np.array([[x], [y], [z]])
    # abc_degree may need to be set by guess and forward() tries
    abc_degree = np.degrees([3.135, 0.151, 3.054])  # ??? refer euler angles at https://en.wikipedia.org/wiki/Euler_angles

    robot = RobotSerial(dh_params, dh_type="modified")
    theta_degree = inverse_vk(robot, xyz, abc_degree) 
    xyz1, abc_degree1 = forward_vk(robot, theta_degree)

    print("*" * 50)
    print(f"Comparison: {xyz.reshape(1,-1)} vs {xyz1.reshape(1,-1)}, {abc_degree} vs {abc_degree1}")
    print("=" * 50)

    robot.show()

    # input("====================== First forward, then inverse, press any key to continue ======================")
    # # theta_degree = [30, 120, -70, -130, 30]   
    # # theta_degree = [0, 60, -60, 90, 10]
    # theta_degree = [0, 0, 0, 0, 0]

    # robot = RobotSerial(dh_params, dh_type="modified")
    # xyz1, abc_degree1 = forward_vk(robot, theta_degree)
    # xyz = xyz1; abc_degree = abc_degree1
    # # theta_degree1 = inverse_vk(robot, xyz, abc_degree) 

    # # print("*" * 50)
    # # print(f"Comparison: {theta_degree} vs {theta_degree1}")
    # # print("=" * 50)

    # robot.show()

if __name__ == "__main__":
    main()
