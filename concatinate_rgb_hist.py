#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
from glob import glob
from matplotlib import pyplot as plt
import numpy as np


def plot_rgbhist(file_path, save_path):
    image_files = glob(file_path)
    print(image_files)
    fig = plt.figure()
    red, blue, green = [], [], []

    for image_file in image_files:
        img = cv2.imread(image_file)
        print(img.shape)
        b, g, r = img[:, :, 0], img[:, :, 1], img[:, :, 2]
        blue.extend(b)
        green.extend(g)
        red.extend(r)

    blue = np.array(blue, dtype=np.float32)
    green = np.array(green, dtype=np.float32)
    red = np.array(red, dtype=np.float32)

    hist_b = cv2.calcHist([blue], [0], None, [256], [1, 256])
    hist_g = cv2.calcHist([green], [0], None, [256], [1, 256])
    hist_r = cv2.calcHist([red], [0], None, [256], [1, 256])

    plt.plot(hist_r, color='r', label="r")
    plt.plot(hist_g, color='g', label="g")
    plt.plot(hist_b, color='b', label="b")
    plt.legend()
    plt.show()

    # fig.savefig(save_path)


if __name__ == '__main__':
    plot_rgbhist(
        '/mnt/cloudy_z/src/yhamajima/Ureter_segmentation/test/*/movieframe/frame_146010.png',
        "/mnt/cloudy_z/src/yhamajima/Ureter_segmentation/experiment/test_rgb_0_2.png"
    )
