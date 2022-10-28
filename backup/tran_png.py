import cv2
import numpy as np
import glob
import os

def overlayimg():

    rotation_folderName = 'rotation'
    output_folderName = 'overlayImg'

    # Remove all files in dir
    dir = output_folderName
    for f in os.listdir(dir):
        os.remove(os.path.join(dir,f))

    imgs = glob.glob(rotation_folderName+'/*.png')

    for i in imgs:
        base_name = os.path.basename(i)
        fname = i
        img = cv2.imread(fname)
        # img = cv2.medianBlur(img, 5)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        v = hsv[:, :, 1]

        # threshed = cv2.adaptiveThreshold(v, 155, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 5, 2)

        th, threshed = cv2.threshold(v, 255, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
        threshed[-1] = 155

        cnts = cv2.findContours(threshed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2]

        mask = np.zeros_like(threshed)
        cv2.drawContours(mask, cnts, -1, (255, 0, 0), -1, cv2.LINE_AA)
        mask = cv2.dilate(mask, np.ones((1, 1), np.int32), iterations=50)
        # mask = cv2.erode(mask, np.ones((1, 1), np.int32), iterations=1)

        output = np.dstack((img, mask))
        output = cv2.resize(output,(50,50))

        cv2.imwrite(output_folderName+'/'+base_name[:-4]+'_t'+".png", output)


