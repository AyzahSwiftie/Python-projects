# A python script to move image files from one folder to another folder.

import os
import shutil

from_folder = "C:/Users/rabiy/Downloads"
to_folder =  "C:/Users/rabiy/Downloads/DownloadedImages"
list_of_files = os.listdir(from_folder)
image_extensions = ['.gif', '.png', '.jpg', '.jpeg','.jfif' ]

# Move All Image files From Folder to TO Folder
for file_name in list_of_files :
    root, ext=os.path.splitext(file_name)       # root, ext=os.path.splitext(“path of a folder/file")
    if ext =='' :
        continue
    if ext in  image_extensions:             # check if the type of file in in this list ['.gif', '.png', '.jpg', '.jpeg','.jfif' ]

        source_dir = from_folder+'/'+file_name
        if os.path.exists(to_folder) :                            #checking if the folder exists
           destination_dir=to_folder+'/'+file_name                             #"C:/python projects/Image_files"+'/'+file_name
           print("Moving ...."+ file_name + "file to Images folder............") 
           shutil.move(source_dir, destination_dir)
        else:                                                       #if the folder doesn't exist then we create it
            new_folder = from_folder+'/'+"DownloadedImages"      #new_folder = C:/Users/rabiy/Downloads/DownloadedImages
            os.makedirs(new_folder)
            print("Moving ...."+ file_name + "file to Images folder............")
            shutil.move(source_dir,new_folder+'/'+file_name)         # move it to new path -DownloadedImages   


    
    