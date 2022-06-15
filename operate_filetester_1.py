from multiprocessing.spawn import import_main_path
import shutil
import random
import glob
import os

def erb(neta):
  neta1 = neta
  try:
    num1 = len([name for name in os.listdir('./sushi/' + str(neta) + '/' + '1') if os.path.isfile(os.path.join('./sushi/' + str(neta) + '/' + '1', name))])

  except Exception:
      pass

  try:
    num0 = len([name for name in os.listdir('./sushi/' + str(neta) + '/' + '0') if os.path.isfile(os.path.join('./sushi/' + str(neta) + '/' + '0', name))])

  except Exception:
    pass

  try:
     if num1 >= 20 and num0 >= 20 :
      print(neta1)
  except Exception:
    pass


if __name__ == '__main__':
  for i in range(1, 88):
    erb(i)