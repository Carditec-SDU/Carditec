import cv2

import numpy as np
address = "D:\\BaiduNetdiskDownload\\BITVehicle_Dataset (2)\\BITVehicle_Dataset\\"
saveaddress = "D:\\BaiduNetdiskDownload\\BITVehicle_Dataset (2)\\NewNewBITVehicle_Dataset\\"

times = 30
def hisEqulColor(img):
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
    channels = cv2.split(ycrcb)
    #print(len(channels))
    channels[0] = cv2.bilateralFilter(channels[0],3,5,10)
    cv2.equalizeHist(channels[0], channels[0])

    cv2.merge(channels, ycrcb)
    cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2BGR, img)

    return img

for i in range(1,times+1):
    img = cv2.imread(address+str(i)+".jpg")
    resizeimg = cv2.resize(img, dsize=(416, 416))
    equimg = hisEqulColor(resizeimg)
    cv2.imwrite(saveaddress + str(i) + ".jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 50])
