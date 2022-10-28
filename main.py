# Master Script for the project
# from stl_png_loop import rotation
from stl_png_loop_tilt import rotation_tilt
from tran_png import transparent_overlayimg
from overlay_img import overlayimg_make
import time

st = time.time()
# Running Loop Script
filename = 'airplane.stl'
deg = 90
# rotation(filename,deg)
rotation_tilt(filename,deg)

# Genreating Transperent Overlay Images
object_dim = [40,40]
transparent_overlayimg(object_dim)

# Paste Transperent Overlay on Satilite Imagery
offset = 5
flag_rect = True
overlayimg_make(offset,flag_rect)



# get the end time
et = time.time()
# get the execution time
elapsed_time = et - st
print('\nExecution time:', round(elapsed_time,2), 'seconds')







