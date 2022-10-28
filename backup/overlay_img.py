from PIL import Image
import os
import cv2
import numpy as np
import glob

# Useful Constants and Variables
bacground_img = "base_imgs/satellite_img1.jpg"
overlayimg_folderName = 'overlayImg'
output_folderName = 'satelliteImg_dataset'


cropping_list = []
DATASET_DIR = './'
IMG_EXTENSION = '.jpg'

infile = os.path.join(DATASET_DIR, bacground_img)

def overlay_image_alpha(img, img_overlay, x, y, alpha_mask=None):

    if y < 0 or y + img_overlay.width > img.width or x < 0 or x + img_overlay.height > img.shape[1]:
        y_origin = 0 if y > 0 else -y
        y_end = img_overlay.shape[0] if y < 0 else min(
            img.shape[0] - y, img_overlay.shape[0])

        x_origin = 0 if x > 0 else -x
        x_end = img_overlay.shape[1] if x < 0 else min(
            img.shape[1] - x, img_overlay.shape[1])

        img_overlay_crop = img_overlay[y_origin:y_end, x_origin:x_end]
        alpha = alpha_mask[y_origin:y_end,
                           x_origin:x_end] if alpha_mask is not None else None
    else:
        img_overlay_crop = img_overlay
        alpha = alpha_mask

    y1 = max(y, 0)
    y2 = min(img.shape[0], y1 + img_overlay_crop.shape[0])

    x1 = max(x, 0)
    x2 = min(img.shape[1], x1 + img_overlay_crop.shape[1])

    img_crop = img[y1:y2, x1:x2]
    img_crop[:] = alpha * img_overlay_crop + \
        (1.0 - alpha) * img_crop if alpha is not None else img_overlay_crop

    return img_crop[:]


def without_click(param,overlayimg_list):

    global cropping_list
    # if event == cv2.EVENT_LBUTTONDOWN:
    for k in overlayimg_list:

        base_name = os.path.basename(k)
        filename = overlayimg_folderName+'/'+base_name
        fornt_img = Image.open(filename, 'r')
        # img = cv2.imread('My project_1.png',
        #                  cv2.IMREAD_UNCHANGED)
        bg = Image.open(param, 'r')
        air_plane_pints = 0
        for i in range(1, 5):
            obj_img = Image.new('RGBA', (416, 416), (0, 0, 0, 0))
            back = obj_img.paste(bg, (0, 0))
            front = obj_img.paste(fornt_img, (air_plane_pints, air_plane_pints), mask=fornt_img)
            
            obj_img.save(output_folderName+"/syn_"+base_name, format="png")
            air_plane_pints += 80
            # output = overlay_image_alpha(back, front, x, y)

def show_loading():

    img_progress = np.ones(shape=(64, 64, 1))
    cv2.putText(img_progress, 'WORKING ON IMAGE, PLEASE WEIGHT',
                (0, 32),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (255, 255, 255,), 1, cv2.LINE_AA, False)
    # cv2.imshow('Loading', img_progress)

def overlayimg_make():

    # img = cv2.imread(infile)
    # height, width, _ = img.shape
    # cv2.namedWindow('window', cv2.WINDOW_FREERATIO)
    
    # Remove all files in dir
    dir = output_folderName
    for f in os.listdir(dir):
        os.remove(os.path.join(dir,f))

    overlay_imgs = glob.glob(overlayimg_folderName+'/*.png')
    # print(overlay_imgs)

    without_click(infile,overlay_imgs)
    
    
# if __name__ == '__main__':
#     main()
