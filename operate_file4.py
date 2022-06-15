from multiprocessing.spawn import import_main_path
import shutil
import random
import glob
import os

import numpy as np

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
def resize_image(pic):
    #調整後サイズを指定(横幅、縦高さ)
    size=(64,64)
    output = pic.replace('20_erb_sushi', 'esushi_resize')

    base_pic=np.zeros((size[1],size[0],3),np.uint8)
    pic1=cv2.imread(pic,cv2.IMREAD_COLOR)
    h,w=pic1.shape[:2]
    ash=size[1]/h
    asw=size[0]/w
    if asw<ash:
        sizeas=(int(w*asw),int(h*asw))
    else:
        sizeas=(int(w*ash),int(h*ash))
    pic1 = cv2.resize(pic1,dsize=sizeas)
    base_pic[int(size[1]/2-sizeas[1]/2):int(size[1]/2+sizeas[1]/2),
    int(size[0]/2-sizeas[0]/2):int(size[0]/2+sizeas[0]/2),:]=pic1
    cv2.imwrite(output, base_pic)


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
