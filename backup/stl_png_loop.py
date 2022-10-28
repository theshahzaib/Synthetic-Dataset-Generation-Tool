import vtkplotlib as vpl
from stl.mesh import Mesh
import os
import math

def rotation():

    filename = 'airplane.stl'
    rotation_folderName = 'rotation'
    deg = 45

    # Remove all files in dir
    dir = rotation_folderName
    for f in os.listdir(dir):
        os.remove(os.path.join(dir,f))


    mesh = Mesh.from_file(filename)
    mesh.rotate([-0.1, 0.0, 0.1], math.radians(0))


    for i in range(0,361,deg):
        
        vpl.mesh_plot(mesh)
        vpl.view(camera_direction = [1, 0, -1])
        
        # vpl.save_fig(rotation_folderName+'/'+filename[:-4]+'_degree_'+str(i)+".png", pixels=(608, 608), off_screen=True)
        vpl.save_fig(rotation_folderName+'/'+filename[:-4]+'_degree_'+str(i)+".png", pixels=(300, 300), off_screen=True)
        print(i)
        
        vpl.reset_camera()
        vpl.close()

        mesh.rotate([-0.1, 0.0, 0.1], math.radians(deg))

# rotation()