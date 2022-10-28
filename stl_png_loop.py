import vtkplotlib as vpl
from stl.mesh import Mesh
import os
import math
from tqdm import tqdm

def rotation(filename,deg):

    # filename = 'airplane.stl'
    rotation_folderName = 'rotation'
    # deg = 45

    # Remove all files in dir
    dir = rotation_folderName
    for f in os.listdir(dir):
        os.remove(os.path.join(dir,f))


    mesh = Mesh.from_file(filename)
    mesh.rotate([-0.1, 0.0, 0.1], math.radians(0))

    print('[INFO]:: Generating 2D Images from 3D Model')
    for i in tqdm(range(0,360,deg)):
        
        vpl.mesh_plot(mesh)
        vpl.view(camera_direction = [1, 0, -1])
        
        # vpl.save_fig(rotation_folderName+'/'+filename[:-4]+'_degree_'+str(i)+".png", pixels=(608, 608), off_screen=True)
        vpl.save_fig(rotation_folderName+'/'+filename[:-4]+'_degree_'+str(i)+".png", pixels=(300, 300), off_screen=True)
        # print(i)
        
        vpl.reset_camera()
        vpl.close()

        mesh.rotate([-0.1, 0.0, 0.1], math.radians(deg))

# rotation()