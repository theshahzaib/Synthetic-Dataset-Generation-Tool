from PIL import Image
import os
import cv2
# from matplotlib.pyplot import flag
import numpy as np
import glob
from tqdm import tqdm

# Global variables
coordinates_list = []
# background_img = ''

# Useful Constants and Variables
background_img = 'base_imgs/satellite_img1.jpg'
overlayimg_folderName = 'overlayImg'
output_folderName = 'satelliteImg_dataset'
base_img = cv2.imread(background_img, 1)

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
 
def pascal_voc_to_yolo(x1, y1, x2, y2, image_w, image_h):
    return [((x2 + x1)/(2*image_w)), ((y2 + y1)/(2*image_h)), (x2 - x1)/image_w, (y2 - y1)/image_h]

def coordinates_on_click(event, x, y, flags, params, offset=5, object_dim=[40,40]):
    global coordinates_list
    if event == cv2.EVENT_LBUTTONDOWN:
        # print(x, ' ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(base_img, str('.'), (x,y), font, 1, (0, 255, 0), 8)
        # cv2.rectangle(base_img, (x+offset, y+offset), 
        #                     (x+object_dim[0]-offset, y+object_dim[1]-offset), 
        #                     (0, 255, 0), -1)
        cv2.imshow('image', base_img)
        coordinates_list.append([x,y]) 

def auto_labels_generation(coordinates_list,offset,bg_img_h,bg_img_w,f_img_h,f_img_w,base_name):

    # Creating bounding box as txt file
    for obj_pt in coordinates_list:
        bb = pascal_voc_to_yolo(obj_pt[0]+offset, obj_pt[1]+offset,
                                obj_pt[0]+f_img_h-offset, obj_pt[1]+f_img_w-offset,
                                bg_img_h, bg_img_w)

        txt_file = open(output_folderName+'/syn_'+base_name[:-4]+'.txt', 'a')
        txt_file.write('0 '+str(bb[0])+' '+str(bb[1])+' '+str(bb[2])+' '+str(bb[3])+'\n')
        txt_file.close()

    txt_file_classes = open(output_folderName+'/classes.txt', 'w')
    txt_file_classes.write('airplane')
    txt_file_classes.close()

def dataset_labels_gen(param,overlayimg_list,coordinates_list,offset,flag_rect):

    print('[INFO]:: Generating Synthetic Satellite Imagery Dataset')
    for k in tqdm(overlayimg_list):

        base_name = os.path.basename(k)
        fornt_img = Image.open(overlayimg_folderName+'/'+base_name, 'r')

        bg = Image.open(param, 'r')
        
        # Make the image, starting with all transparent (alpha=0)
        obj_img = Image.new('RGBA', (416, 416), (0, 0, 0, 0))
        back = obj_img.paste(bg, (0, 0))
        
        for obj_pt in coordinates_list:
            front = obj_img.paste(fornt_img, (obj_pt[0], obj_pt[1]), mask=fornt_img)
        
        obj_img_cv = np.array(obj_img)

        # offset = 5

        # Getting size of the image
        bg_img_h, bg_img_w, _ = obj_img_cv.shape
        f_img_h, f_img_w = fornt_img.size

        if (flag_rect == True):
            for obj_pt in coordinates_list:
                cv2.rectangle(obj_img_cv, (obj_pt[0]+offset, obj_pt[1]+offset), 
                            (obj_pt[0]+f_img_h-offset, obj_pt[1]+f_img_w-offset), 
                            (0, 255, 0), 2)
        
        obj_img_cv_bgr = cv2.cvtColor(obj_img_cv, cv2.COLOR_RGB2BGR)

        cv2.imwrite(output_folderName+'/syn_'+base_name, obj_img_cv_bgr)

        # auto_labels_generation(coordinates_list,offset,bg_img_h,bg_img_w,f_img_h,f_img_w,base_name)

        ### Creating bounding box as txt files ###
        for obj_pt in coordinates_list:
            bb = pascal_voc_to_yolo(obj_pt[0]+offset, obj_pt[1]+offset,
                                    obj_pt[0]+f_img_h-offset, obj_pt[1]+f_img_w-offset,
                                    bg_img_h, bg_img_w)

            txt_file = open(output_folderName+'/syn_'+base_name[:-4]+'.txt', 'a')
            txt_file.write('0 '+str(bb[0])+' '+str(bb[1])+' '+str(bb[2])+' '+str(bb[3])+'\n')
            txt_file.close()

        txt_file_classes = open(output_folderName+'/classes.txt', 'w')
        txt_file_classes.write('airplane')
        txt_file_classes.close()

def overlayimg_make(offset=5,flag_rect=True):

    # Remove all files in dir
    dir = output_folderName
    for f in os.listdir(dir):
        os.remove(os.path.join(dir,f))

    overlay_imgs_list = glob.glob(overlayimg_folderName+'/*.png')
    cv2.imshow('image', base_img)
    cv2.setMouseCallback('image', coordinates_on_click)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(coordinates_list)

    dataset_labels_gen(background_img,overlay_imgs_list,coordinates_list,offset,flag_rect)

    print('[INFO]:: Synthetic Satellite Imagery Dataset Generated')
        
if __name__ == '__main__':
    overlayimg_make()








# def show_loading():

#     img_progress = np.ones(shape=(64, 64, 1))
#     cv2.putText(img_progress, 'WORKING ON IMAGE, PLEASE WEIGHT',
#                 (0, 32),
#                 cv2.FONT_HERSHEY_SIMPLEX, 1,
#                 (255, 255, 255,), 1, cv2.LINE_AA, False)
#     # cv2.imshow('Loading', img_progress)