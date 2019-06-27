import h5py as h5
import cv2

f = h5.File('Apr_26.h5', 'w')

for i in range(1, 9851):
    image = cv2.imread(str(i) + '.jpg')
    dset = f.create_dataset(str(i), (416,416,3), dtype='f')
    dest[:,:,:] = image

f.close()