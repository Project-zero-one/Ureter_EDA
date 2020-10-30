import os
import cv2
from glob import glob


def hw_split(mask_dir, split_height, split_width):
    mask_files = glob(mask_dir)
    print(mask_files)

    for mask_file in mask_files:
        print(mask_file)
        img = cv2.imread(mask_file)
        mask = os.path.splitext(os.path.basename(mask_file))[0]
        height, width, channels = img.shape

        new_img_height = int(height / split_height)
        new_img_width = int(width / split_width)

        # print(height)  # 720
        # print(width)  # 1280
        # print(channels)  # 3
        # print(split_width)  # 3
        # print(split_height)  # 2

        for h in range(split_height):
            height_start = h * new_img_height
            height_end = height_start + new_img_height

            for w in range(split_width):
                width_start = w * new_img_width
                width_end = width_start + new_img_width

                file_name = mask + str(h) + "_" + str(w) + ".png"
                clp = img[height_start:height_end, width_start:width_end]
                cv2.imwrite(
                    f'/mnt/cloudy_z/src/yhamajima/Ureter_segmentation/experiment/{file_name}', clp)


if __name__ == '__main__':
    hw_split(
        '/mnt/cloudy_z/src/yhamajima/Ureter_segmentation/test/*/label/frame_042494.png', 2, 3)
