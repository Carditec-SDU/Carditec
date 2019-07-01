import cv2

import numpy as np
address = "/home/yingbing/data/7_1/Truck/"
saveaddress = "/home/yingbing/data/Adj/"

times = 1298
base = 20583

def hisEqulColor(img):
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
    channels = cv2.split(ycrcb)
    #print(len(channels))
    channels[0] = cv2.bilateralFilter(channels[0],3,5,10)
    cv2.equalizeHist(channels[0], channels[0])

    cv2.merge(channels, ycrcb)
    cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2BGR, img)

    return img

f = open(address+"index", "r")
imgs = f.read()
imgs = imgs.split('\n')

for i in range(0,times):
    img = cv2.imread( address + imgs[i])
    resizeimg = cv2.resize(img, dsize=(416, 416))
    equimg = hisEqulColor(resizeimg)
    cv2.imwrite(saveaddress + str(base+i) + ".jpg", equimg, [int(cv2.IMWRITE_JPEG_QUALITY), 50])

