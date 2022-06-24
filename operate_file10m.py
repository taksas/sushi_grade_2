from multiprocessing.spawn import import_main_path
import shutil
import random
import glob
import os

import numpy as np

import cv2
from scipy import ndimage

# 正方形にリサイズ？(main)

def erb(neta, nedan):
  os.makedirs('./attach/sushi_rotate1_m/' + neta + '/' + nedan, exist_ok=True)
  os.makedirs('./attach/sushi_rotate2_m/' + neta + '/' + nedan, exist_ok=True)

  image_list = glob.glob('./attach/sushi_resize_m/' + neta + '/' + nedan + '/*')
  print(image_list)
  for path in image_list:
      rotate_image1(path)
      rotate_image2(path)


# モザイク
def mosaic_image(pic):
    output = pic.replace('sushi_resize_m', 'sushi_mosaic_m')

    image = cv2.imread(pic)
    image_small = cv2.resize(image, None, fx=0.1, fy=0.1, interpolation=cv2.INTER_NEAREST)
    image_masaic = cv2.resize(image_small, image.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

    cv2.imwrite(output, image_masaic)

# 画像回転
def rotate_image1(pic):
    output = pic.replace('sushi_resize_m', 'sushi_rotate1_m')
    image = cv2.imread(pic)
    for ang in [-5, 0, 5]:
        image_rot = ndimage.rotate(image, ang)
        cv2.imwrite(output, image_rot)

# 画像回転
def rotate_image2(pic):
    output = pic.replace('sushi_resize_m', 'sushi_rotate2_m')
    image = cv2.imread(pic)
    for ang in [5, 0, -5]:
        image_rot = ndimage.rotate(image, ang)
        cv2.imwrite(output, image_rot)


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
