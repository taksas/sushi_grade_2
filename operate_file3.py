from multiprocessing.spawn import import_main_path
import shutil
import random
import glob
import os

import cv2
from scipy import ndimage

# 正方形にリサイズ？

def erb(neta, nedan):
  os.makedirs('./esushi_resize/' + neta + '/' + nedan, exist_ok=True)
  image_list = glob.glob('./20_erb_sushi/' + neta + '/' + nedan + '/*')
  print(image_list)
  for path in image_list:
      resize_image(path)

# サイズ変更
def resize_image(image_path):
    image = cv2.imread(image_path)
    # 64 * 64に変更
    image_resize = cv2.resize(image, (64,64))
    output = image_path.replace('20_erb_sushi', 'esushi_resize')
    file_name = output
    cv2.imwrite(file_name, image_resize)


if __name__ == '__main__':
    erb("5", "0")
    erb("6", "0")
    erb("17", "0")

    erb("18", "0")
    erb("19", "0")
    erb("27", "0")

    erb("41", "0")
    erb("44", "0")
    erb("81", "0")


    erb("5", "1")
    erb("6", "1")
    erb("17", "1")

    erb("18", "1")
    erb("19", "1")
    erb("27", "1")

    erb("41", "1")
    erb("44", "1")
    erb("81", "1")
