import cv2
import numpy as np

def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()

n_images = 598 # number of image frames in each video file
threshold1 = 250
threshold2 = 370
finddata_path = '/path_to_file'
saveimag_path = '/path_to_save'

for img in range(n_images):
    # load the image, convert it to grayscale, and compute the
    # focus measure of the image using the Variance of Laplacian
    # method
    index = img%03
    image = cv2.imread(finddata_path+'/frame'+str(index)+'.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur_value = variance_of_laplacian(gray)

    #classify blur based on thresholds
    if blur_value < threshold1:
        text = "Very Clear"
        color = (0, 255, 0)
    elif blur_value < threshold2:
        text = "Not too Blurry"
        color = (0, 255, 255)
    else:
        text = "Blurry"
        color = (0, 0, 255)   

    # display the image
    image_info = "Image source: frame "+ str(index) +".jpg"  
    cv2.putText(image, "{}:  (bluriness={:.2f})".format(text, blur_value), (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 3)
    cv2.putText(image, image_info, (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (225,255,255), 3)
    cv2.imwrite(saveimag_path+'Image'+ str(index) +'.jpg', image)
    key = cv2.waitKey(0)