import cv2
import glob 

import os
import cv2
import glob
import numpy as np
finddata_path = r'/home/nivii/Desktop/MICCAI2019_Dataset/Test/surgery4' #/ground_truth'# Name of the folder with the files
savedata_path = r'/home/nivii/Desktop/MICCAI2019_Dataset/Test/surgery4' #/ground_truth'
pattern = r'*.jpg' # File extension of interest
   
def image_crop(dir, new_dir, extension):
    
    for pathAndFilename in glob.iglob(os.path.join(dir, extension)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        uncrop_image = cv2.imread(os.path.join(dir, pathAndFilename))
        image = uncrop_image[0:475,95:615]
        cv2.imwrite(os.path.join(pathAndFilename), image)
        
        
# Image crop for sequential images
# n_images = 100
# for img in range(n_images):
#     index = '%03d' % img + 200
#     uncrop_image = cv2.imread(finddata_path + '/frame' + str(img) + '.jpg')
#     image = uncrop_image[0:475,95:615]
#     cv2.imwrite(savedata_path + '/frame' + str(index) + '.jpg', image)

image_crop(finddata_path, savedata_path, pattern)