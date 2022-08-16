from distutils import extension
from operator import imod


import os
import shutil 

from_dir = "C:/Users/user/Downloads"
to_dir = "C:/Users/user/whitehat"

  if extension == '':
    continue
  if extension in ['.txt', '.doc','.docx','.pdf']:

    path1 = from_dir + '/' + file_name                      
    path2 = to_dir + '/' + "Image_Files"                      
    path3 = to_dir + '/' + "Image_Files" + '/' + file_name


if os.path.exists(path2):
    print("Moving " + file_name + ".....")

    # Move from path1 ---> path3
    shutil.move(path1, path3)

else:
    os.makedirs(path2)
    print("Moving " + file_name + ".....")
    shutil.move(path1, path3)