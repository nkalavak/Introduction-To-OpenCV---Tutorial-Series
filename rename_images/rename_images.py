import os
import cv2
import glob
import numpy as np
path = r'/home/nivii/Desktop/UndergradResearch/Undergrad Research/Yinghao/Round3/Masks'# Name of the folder with the files
pattern = r'*.jpg' # File extension of interest
title_pattern = r'sy_' # Change to the pattern, to include title

#Renaming files without consecutive names
def rename(dir, pattern, titlePattern):
    for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        os.rename(pathAndFilename, 
                  os.path.join(dir, titlePattern + title + ext))

rename(path, pattern, title_pattern)


"""
#Rename directory of image files with consecutive numbers
#Importing - os to make array of files and rename, Image to check file type
import os
from PIL import Image

#Variables for script
images_dir = "C:\file\directory\pictures\\temp\\"
file_array = os.listdir(images_dir)
file_name = 1

#Loops through each file and renames it to either a png or gif file
for file in file_array:
    img = Image.open(images_dir + file)
    if img.format != "GIF":
        os.rename(images_dir + file, images_dir + str(file_name) + ".png")
    elif img.format == "GIF":
        os.rename(images_dir + file, images_dir + str(file_name) + ".gif")
    file_name = file_name + 1"""