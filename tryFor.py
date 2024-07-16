import os
import shutil

path = "C:/python projects/"
newPath =  "C:/python projects"+'/'+"Image_files"
list_of_files = os.listdir(path)
print(list_of_files)

for file_name in list_of_files :
   root, ext=os.path.splitext(file_name)

    