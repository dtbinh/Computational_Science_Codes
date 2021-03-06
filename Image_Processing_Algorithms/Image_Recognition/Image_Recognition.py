import numpy as np
import scipy.misc as smisc
import scipy.ndimage as nd
import Image
import imageproc
import os

def ShiftCenterFrame(f):
    cofm = nd.center_of_mass( f )
    V,H = f.shape
    dv = V/2 - cofm[0]
    dh = H/2 - cofm[1]
    dv = int(dv); dh =int(dh)
    fshift = nd.shift( f, (dv,dh) )
    return fshift, (dv,dh)

def AngleOfRotation( data ):
    x,y = data.nonzero()
    m = np.array( (x,y) )
    cv = np.cov( m )
    evals, evecs = np.linalg.eig( cv )
    ang = np.arctan2( evecs[0,1], evecs[0,0] )
    return ang


estonia = smisc.imread('EstoniaBeach.jpg',flatten=1);
estonia = estonia/4;

img =  Image.open('EstoniaBeach.jpg').convert('YCbCr')

mg = np.array(img)

mg_ch = (mg[:,:,1]>130)+(mg[:,:,2]>138)
mg_ch = mg_ch>0;
mg_ch = nd.binary_fill_holes(mg_ch);


work_mg = nd.binary_erosion(mg_ch,iterations=2)
work_mg = nd.binary_dilation(work_mg,iterations=2)


lbls,nls = nd.label(work_mg)

#Forming an array of points large enough to be of interest

arr = []
for i in range(nls):
    z = (lbls==i).sum()
    if z > 450:
#        print i,z
        arr.append([i,z])
arr = np.array(arr)
arr = arr[np.lexsort((arr[:,0],arr[:,1]))]
arr = arr[0:-1]


V,H = work_mg.shape
cy = int(V/2)
cx = int(H/2)

for i in range(len(arr)):
    ref_mg = (lbls==arr[i][0])+0
    shiftd,(dv,dh) = ShiftCenterFrame(ref_mg)
    ang = AngleOfRotation(shiftd)
    ang = np.degrees(ang)
    rotd = nd.rotate(shiftd,ang)

    mv = cy-dv
    mh = cx-dh
    y,x = rotd.shape
    midy = int(y/2)
    midx = int(x/2)
    estonia[mv,mh-4:mh+4] = 255
    estonia[mv-4:mv+4,mh] = 255  
    
#    #Method 1 : Accuracy = 50%!!
    num = int(rotd[midy,:].sum()/20)

    j = 20
    k = 1
    for i in range(int(num)):
        mv1 = int(cy-dv)
        mh1 = int(cx-j-dh)
        if (mv1 <V and mh1<H):
            estonia[mv1,mh1-4:mh1+4] = 255
            estonia[mv1-4:mv1+4,mh1] = 255
        elif(mv1>=V and mh1 < H):
            estonia[V-4:V,mh1-4:mh1+4] = 255
        elif(mv1<V and mh1>=H):
            estonia[mv1-4:mv1+4,H-4:H-1] = 255
        else:
            continue
        j = j-15
smisc.imshow(estonia)
smisc.imsave('Final.jpg',estonia)