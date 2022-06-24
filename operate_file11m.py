from multiprocessing.spawn import import_main_path
import shutil
import random
import glob
import os

import numpy as np

import cv2
from scipy import ndimage

import re

# お名前を0~にする(main_attach)



list = [[0] * 82 for i in range(2)]

def erb(neta, nedan):
  os.makedirs('./attach/sushi_m_r/' + neta + '/' + nedan, exist_ok=True)
  image_list = glob.glob('./attach/sushi_m/' + neta + '/' + nedan + '/*')
  print(image_list)
  num = 0
  for path in image_list:
      rename_image(path,neta,nedan,num)
      num += 1

# サイズ変更
def rename_image(pic,neta,nedan,num):
    # ファイル名の変更 
    os.rename(pic, './attach/sushi_m_r/' + neta + '/' + nedan + '/' + str(num) + '.jpg') 


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
