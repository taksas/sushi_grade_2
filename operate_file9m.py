from multiprocessing.spawn import import_main_path
import shutil
import random
import glob
import os

import numpy as np

import cv2
from scipy import ndimage

# いろいろ(main)

def erb(neta, nedan):
  os.makedirs('./attach/sushi_threshold_m/' + neta + '/' + nedan, exist_ok=True)
  os.makedirs('./attach/sushi_gaussian_m/' + neta + '/' + nedan, exist_ok=True)
  os.makedirs('./attach/sushi_mosaic_m/' + neta + '/' + nedan, exist_ok=True)
  image_list = glob.glob('./attach/sushi_resize_m/' + neta + '/' + nedan + '/*')
  print(image_list)
  for path in image_list:
      threshold_image(path)
      gaussian_image(path)
      mosaic_image(path)


# 閾値
def threshold_image(pic):
    output = pic.replace('sushi_resize_m', 'sushi_threshold_m')

    image = cv2.imread(pic)
    # 閾値100を超えたがぞを255にする
    image_thr =  cv2.threshold(image, 100, 255, cv2.THRESH_TOZERO)[1]

    cv2.imwrite(output, image_thr)

# ぼかし
def gaussian_image(pic):
    output = pic.replace('sushi_resize_m', 'sushi_gaussian_m')

    image = cv2.imread(pic)
    # 奇数じゃないといけない
    image_gau =  cv2.GaussianBlur(image, (15, 15), 0)

    cv2.imwrite(output, image_gau)

# モザイク
def mosaic_image(pic):
    output = pic.replace('sushi_resize_m', 'sushi_mosaic_m')

    image = cv2.imread(pic)
    image_small = cv2.resize(image, None, fx=0.1, fy=0.1, interpolation=cv2.INTER_NEAREST)
    image_masaic = cv2.resize(image_small, image.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

    cv2.imwrite(output, image_masaic)




if __name__ == '__main__':

    erb("6", "0")
    erb("17", "0")

    erb("18", "0")
    erb("19", "0")
    erb("27", "0")

    erb("41", "0")

    erb("81", "0")



    erb("6", "1")
    erb("17", "1")

    erb("18", "1")
    erb("19", "1")
    erb("27", "1")

    erb("41", "1")

    erb("81", "1")
