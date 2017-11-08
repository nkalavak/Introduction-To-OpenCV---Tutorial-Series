import cv2
import numpy as np
import os

#Initialize file locations
filepath = '/path_to_file'
savepath = '/path_to_save'

# Playing video from file:
cap = cv2.VideoCapture(findpath)

try:
    if not os.path.exists(savepath):
        os.makedirs(savepath)
except OSError:
    print ('Error: Creating directory to store images!')

currentFrame = 0
ret = True
while(ret == True):
    # Capture frame-by-frame
    if currentFrame > 0:
        cap.set(cv2.CAP_PROP_POS_FRAMES,currentFrame) 
    ret, frame = cap.read()

    # Saves image of the current frame in jpg file
    ind = int(currentFrame/500)
    name = 'D:/01 Projects/AMAZON CATALYST PROJECT/data_surg1_test/frame' + str(ind) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images -- saves one in 500 frames
    currentFrame += 500

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()