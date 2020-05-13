# -*- coding: utf-8 -*-
# @Time    : 2020/5/13 9:25
# @Author  : W07

import os
import cv2
import numpy as np

if __name__ == '__main__':
    img_path = r'‪F:\ocr\mtwi\T1._WBXtXdXXXXXXXX_!!0-item_pic.jpg.jpg'
    image = cv2.imread(img_path,cv2.CV_LOAD_IMAGE_GRAYSCALE)
    h,w= image.shape[:]
    # 仿射变换矩阵，缩小2倍
    A1 = np.array([[0.5,0,0],[0,0.5,0]],np.float32)