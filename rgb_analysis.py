#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import glob
from matplotlib import pyplot as plt
import numpy as np
from scipy import stats
import csv
import os
import seaborn as sns

# plot only the rgb histogram


def plot_rgbhist(csv_dice_file, save_path):

    with open(csv_dice_file, 'r') as csv_file:
        for row in csv.reader(csv_file):
            img = cv2.imread(row[1])
            new_file_name = os.path.basename(row[1])

            fig = plt.figure()

            b, g, r = img[:, :, 0], img[:, :, 1], img[:, :, 2]

            blue = np.array(b, dtype=np.float32)
            green = np.array(g, dtype=np.float32)
            red = np.array(r, dtype=np.float32)

            hist_b = cv2.calcHist([blue], [0], None, [256], [1, 256])
            hist_g = cv2.calcHist([green], [0], None, [256], [1, 256])
            hist_r = cv2.calcHist([red], [0], None, [256], [1, 256])
            # mean_b = np.mean(blue).item()
            # mean_g = np.mean(green).item()
            # mean_r = np.mean(red).item()
            std_b = np.std(blue).item()
            std_g = np.std(green).item()
            std_r = np.std(red).item()
            print(std_b)
            med_b = np.median(blue).item()
            print(med_b)
            mode, count = stats.mode(blue, axis=None)
            print(mode)
            print(count)
            # plt.plot(hist_r, color='r', label="r")
            # plt.plot(hist_g, color='g', label="g")
            # plt.plot(hist_b, color='b', label="b")

            # plt.axvline(mean_b, color='c',
            #             linestyle='dashed', linewidth=1)
            # plt.axvline(mean_g, color='m',
            #             linestyle='dashed', linewidth=1)
            # plt.axvline(mean_r, color='k',
            #             linestyle='dashed', linewidth=1)
            # plt.title("rgb_hist_for_range08_and_up")
            # plt.legend()

            # fig.savefig(f"{save_path}{new_file_name}")

# plot only the hsv histogram


def plot_hsvhist(csv_dice_file, save_path):

    with open(csv_dice_file, 'r') as csv_file:
        for row in csv.reader(csv_file):
            img = cv2.imread(row[1], cv2.COLOR_BGR2HSV)
            new_file_name = os.path.basename(row[1])

            fig = plt.figure()

            h, s, v = img[:, :, 0], img[:, :, 1], img[:, :, 2]

            hist_h = cv2.calcHist([h], [0], None, [256], [1, 256])
            hist_s = cv2.calcHist([s], [0], None, [256], [1, 256])
            hist_v = cv2.calcHist([v], [0], None, [256], [1, 256])
            # mean = np.mean(hist_b).item()

            plt.plot(hist_h, color='r', label="h")
            plt.plot(hist_s, color='g', label="s")
            plt.plot(hist_v, color='b', label="v")

            # plt.axhline(mean, color='k',
            #             linestyle='dashed', linewidth=1)
            plt.title("rgb_hist_for_range08_and_up")
            plt.legend()

            fig.savefig(f"{save_path}hsv{new_file_name}")


# plot rgb and hsv histogram with mask
def plot_maskhist_rgb_hsv(csv_dice_file, mask_path, save_path):

    with open(csv_dice_file, 'r') as csv_file:

        for row in csv.reader(csv_file):
            img_rgb = cv2.imread(row[1])
            img_hsv = cv2.imread(row[1], cv2.COLOR_BGR2HSV)
            new_file_name = os.path.basename(row[1])

            fig = plt.figure()
            b, g, r = img_rgb[:, :, 0], img_rgb[:, :, 1], img_rgb[:, :, 2]
            blue = np.array(b, dtype=np.float32)
            print(np.mean(blue))
            # print(np.max(blue))
            # green = np.array(g, dtype=np.float32)
            # red = np.array(r, dtype=np.float32)

            hist_b = cv2.calcHist([blue], [0], None, [256], [1, 256])
            # print(np.max(hist_b))
            # hist_g = cv2.calcHist([green], [0], None, [256], [1, 256])
            # hist_r = cv2.calcHist([red], [0], None, [256], [1, 256])
            mean = np.mean(hist_b)
            # print(np.std(hist_b))
            # print(mean)

            # plt.plot(hist_r, color='r', label="r")
            # plt.plot(hist_g, color='g', label="g")
            # plt.plot(hist_b, color='b', label="b")
            # plt.title("rgb_hist_for_range08_and_up")
            # plt.legend()
            # fig.savefig(f"{save_path}rgb_mask_{new_file_name}")

            # fig = plt.figure()
            # h, s, v = img_hsv[:, :, 0], img_hsv[:, :, 1], img_hsv[:, :, 2]

            # hist_h = cv2.calcHist([h], [0], mask, [256], [1, 256])
            # hist_s = cv2.calcHist([s], [0], mask, [256], [1, 256])
            # hist_v = cv2.calcHist([v], [0], mask, [256], [1, 256])

            # plt.plot(hist_h, color='r', label="h")
            # plt.plot(hist_s, color='g', label="s")
            # plt.plot(hist_v, color='b', label="v")
            # plt.title("rgb_hist_for_range08_and_up")
            # plt.legend()
            # fig.savefig(f"{save_path}hsv_mask_{new_file_name}")


if __name__ == '__main__':
    plot_rgbhist(
        "/mnt/cloudy_z/src/yhamajima/Ureter_EDA/processed_data/test_imput.csv",
        "/mnt/cloudy_z/src/yhamajima/Ureter_EDA/processed_data/csv_output_test/"
    )
    # plot_hsvhist(
    #     "/mnt/cloudy_z/src/yhamajima/Ureter_EDA/processed_data/test_imput.csv",
    #     "/mnt/cloudy_z/src/yhamajima/Ureter_EDA/processed_data/csv_output_test/"
    # )
    # plot_maskhist_rgb_hsv(
    #     "/mnt/cloudy_z/src/yhamajima/Ureter_EDA/processed_data/test_imput.csv",
    #     "/mnt/cloudy_z/src/yhamajima/Ureter_EDA/processed_data/",
    #     "/mnt/cloudy_z/src/yhamajima/Ureter_EDA/processed_data/csv_output_test/"
    # )
