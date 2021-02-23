import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import gc
structure=pd.read_csv('structure.csv',sep=',')
data=structure.iloc[:,1:]
data.molecule_name=data.molecule_name.apply(lambda x: x.strip("''"))
names=data['molecule_name'].unique()
names=list(names)
dict={'C':6,'N':7,'H':1,'O':8,'F':9}
data_an=data
data_an['atom'].replace(dict,inplace=True)
del structure,data
gc.collect()

#funciton for creating the images
def gaussian(molecule_name,sigma,levels,a):
    coor=data_an[data_an['molecule_name']==molecule_name]
    length=len(coor)
    e=np.e
    f=0
    fig,ax=plt.subplots(figsize=(3,3))
    x_mean=coor.iloc[:,3].mean()
    y_mean=coor.iloc[:,4].mean()
    x=np.linspace(-a,a,100)
    y=np.linspace(-a,a,100)
    X, Y = np.meshgrid(x, y)
    for i in range(0,length):
        xi=coor.iloc[i,3]-x_mean
        yi=coor.iloc[i,4]-y_mean
        zi=coor.iloc[i,2]
        f=f+zi*e**(-((X-xi)**2+(Y-yi)**2)/(2*sigma**2))
    c=ax.contourf(X,Y,f,levels,cmap='binary_r')
    plt.axis('off')
    plt.savefig('/Images_reor/{}.png'.format(molecule_name),bbox_inches = 'tight',pad_inches = 0)
    plt.close(fig)
    gc.collect()

i=0
t_0=time.time()
for name in names:
    gaussian(name,0.2,11,5)
    i+=1
    if i%100==0:
        print(i)
        print(time.time()-t_0)
