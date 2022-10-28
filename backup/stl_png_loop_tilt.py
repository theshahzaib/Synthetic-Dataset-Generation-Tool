import vtkplotlib as vpl
from stl.mesh import Mesh
import glob
import os
import math

filename = 'airplane.stl'
rotation_folderName = 'rotation'

# Read the STL using numpy-stl
mesh = Mesh.from_file(filename)

deg = 90
mesh.rotate([-0.1, 0.0, 0.1], math.radians(0))

for tilt in range(-20,21,20):
    
    tilt_value = 0
    if (tilt > 0):
        tilt_value = 360 - tilt
    else:
        tilt_value = tilt

    for i in range(0,361,deg):

        
        vpl.mesh_plot(mesh)
        vpl.view(camera_direction = [1, tilt, -1])

        
        vpl.save_fig(rotation_folderName+'/'+filename[:-4]+'_tilt_'+str(tilt_value)+'_degree_'+str(i)+".png", pixels=(608, 608), off_screen=True)
        print(i)
        
        vpl.reset_camera()
        vpl.close()

        mesh.rotate([-0.1, 0.0, 0.1], math.radians(deg))

    


    # Show the figure
    # vpl.show()
    # vpl.close()
