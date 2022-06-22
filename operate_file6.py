from multiprocessing.spawn import import_main_path
import shutil
import random
import glob
import os

# 各要素20枚ある寿司ネタに対して、ランダムに5枚を選んで移動

def erb(neta, nedan):
  os.makedirs('./esushi_sub/' + neta + '/' + nedan, exist_ok=True)
  image_list = glob.glob('./esushi_main/' + neta + '/' + nedan + '/*')
  print(image_list)
  random.shuffle(image_list)
  print(image_list)
  for t in range(5):
      shutil.move(str(image_list[t]), './esushi_sub/' + neta + '/' + nedan + '/')



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
