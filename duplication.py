from multiprocessing.spawn import import_main_path
import shutil
import random
import glob
import os

import imgsim
import shutil
import cv2



# 各要素20枚以上ある寿司ネタに対して、重複無しにする

def erb(neta, nedan):
  os.makedirs('./repeat_erb_sushi/' + neta + '/' + nedan, exist_ok=True)
  image_list = glob.glob('./erb_sushi/' + neta + '/' + nedan + '/*')
  for t in image_list:
    chk = checker(t, neta, nedan)
    if chk:
      shutil.copy(str(t), './repeat_erb_sushi/' + neta + '/' + nedan + '/')
    print(chk)



def checker(path, neta, nedan):
 img0 = cv2.imread(path)

 for file in glob.glob('./repeat_erb_sushi/' + neta + '/' + nedan + '/' + '*.jpg'):
  
    img1 = cv2.imread(file)
    vtr = imgsim.Vectorizer()
    vec0 = vtr.vectorize(img0)
    vec1 = vtr.vectorize(img1)
    dist = imgsim.distance(vec0, vec1)
    if dist == 0.0:
      return 0
  
 return 1
  




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
