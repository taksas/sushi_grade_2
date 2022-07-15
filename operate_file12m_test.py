from multiprocessing.spawn import import_main_path
import shutil
import random
import glob
import os

import numpy as np

import cv2
from scipy import ndimage

# 開店したやつを正方形にリサイズ(all)

def erb(neta, nedan):
  os.makedirs('./attach/sushi_rotate1_m_64/' + neta + '/' + nedan, exist_ok=True)
  os.makedirs('./attach/sushi_rotate1_s_64/' + neta + '/' + nedan, exist_ok=True)
  os.makedirs('./attach/sushi_rotate2_m_64/' + neta + '/' + nedan, exist_ok=True)
  os.makedirs('./attach/sushi_rotate2_s_64/' + neta + '/' + nedan, exist_ok=True)

  image_list1m = glob.glob('./attach/sushi_rotate1_m/' + neta + '/' + nedan + '/*')
  image_list1s = glob.glob('./attach/sushi_rotate1_s/' + neta + '/' + nedan + '/*')
  image_list2m = glob.glob('./attach/sushi_rotate2_m/' + neta + '/' + nedan + '/*')
  image_list2s = glob.glob('./attach/sushi_rotate2_s/' + neta + '/' + nedan + '/*')


  for path in image_list1m:
      resize_image(path)
  for path in image_list1s:
      resize_image(path)
  for path in image_list2m:
      resize_image(path)
  for path in image_list2s:
      resize_image(path)

# サイズ変更
def resize_image(pic):
    #調整後サイズを指定(横幅、縦高さ)
    size=(64,64)
    output = pic.replace('sushi_rotate1_m', 'sushi_rotate1_m_64').replace('sushi_rotate1_s', 'sushi_rotate1_s_64').replace('sushi_rotate2_m', 'sushi_rotate2_m_64').replace('sushi_rotate2_s', 'sushi_rotate2_s_64')

                
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
