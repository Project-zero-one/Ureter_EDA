#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import glob
from matplotlib import pyplot as plt
import numpy as np
import csv
import os


def plot_rgbhist(csv_dice_file, save_path):

    with open(csv_dice_file, 'r') as csv_file:
        for row in csv.reader(csv_file):
            img = cv2.imread(row[1])
            new_file_name = os.path.basename(row[1])

            fig = plt.figure()
            print(new_file_name)

            b, g, r = img[:, :, 0], img[:, :, 1], img[:, :, 2]

            blue = np.array(b, dtype=np.float32)
            green = np.array(g, dtype=np.float32)
            red = np.array(r, dtype=np.float32)

            hist_b = cv2.calcHist([blue], [0], None, [256], [1, 256])
            hist_g = cv2.calcHist([green], [0], None, [256], [1, 256])
            hist_r = cv2.calcHist([red], [0], None, [256], [1, 256])

            plt.plot(hist_r, color='r', label="r")
            plt.plot(hist_g, color='g', label="g")
            plt.plot(hist_b, color='b', label="b")
            plt.title("rgb_hist_for_d0")
            plt.legend()
            # plt.show()

            fig.savefig(f"{save_path}{new_file_name}")


if __name__ == '__main__':
    plot_rgbhist(
        "/mnt/cloudy_z/src/yhamajima/Ureter_EDA/preprocess/dice_0_test.csv",
        "/mnt/cloudy_z/src/yhamajima/Ureter_segmentation/experiment/rgb/"
    )
