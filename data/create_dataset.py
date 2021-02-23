import pandas as pd
import numpy as np
import cv2
import os

def create_dataset(img_folder,dpi):
    Dataset_energy=pd.read_table('Indices_MolPlan.dat',sep=' ',header=None,names=['mol_index','energy'])
    img_data_array=[]
    energy=[]
    t0=time.time()
    i=0
    for file in os.listdir(img_folder):

        image_path= os.path.join(img_folder,  file)
        image= cv2.imread(image_path)
        image=cv2.resize(image, (dpi,dpi),interpolation = cv2.INTER_AREA)
        image=np.array(image)
        image = image.astype('float32')/255
        img_data_array.append(image)
        index=int(re.split('[_,.]',file)[1])
        E=Dataset_energy[Dataset_energy['mol_index']==index].iloc[0,1]
        energy.append(E)
        i+=1
    energy=np.array(energy).reshape((4237,1))
    img_data=np.array(img_data_array)
    return img_data,energy
