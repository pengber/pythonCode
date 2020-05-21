import numpy as np
import cv2

filter_du = np.array([
        [1.0, 2.0, 1.0],
        [0.0, 0.0, 0.0],
        [-1.0, -2.0, -1.0],
    ])
    # 这会将它从2D滤波转换为3D滤波器
    # 为每个通道：R，G，B复制相同的滤波器
filter_yuan = [filter_du]*3
filter_du = np.stack([filter_du] * 3, axis=0)
print(filter_du)
print(filter_du[:,:,0])