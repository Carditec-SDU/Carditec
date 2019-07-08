import cv2

import numpy as np
#address = "D:\\BaiduNetdiskDownload\\BITVehicle_Dataset (2)\\BITVehicle_Dataset\\"
#saveaddress = "D:\\BaiduNetdiskDownload\\BITVehicle_Dataset (2)\\NewNewBITVehicle_Dataset\\"
testaddress = "C:\\Users\\shiraz\\Pictures\\testimg\\"
savetestaddress = "C:\\Users\\shiraz\\Pictures\\testimgdone\\"
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
    img = cv2.imread(testaddress+str(i)+".jpg")

    #cv2.imshow("img",img)
    #filterimg = cv2.bilateralFilter(img,5,7,15)
    #v2.imshow("filterimg",filterimg)
    equimg = hisEqulColor(img)

    cv2.imwrite(savetestaddress+str(i)+".jpg", equimg, [int(cv2.IMWRITE_JPEG_QUALITY), 50])
    if(i%100==0):
        print("第"+str(i)+"张图片处理")
    #cv2.imshow("equimg",equimg)


    #cv2.waitKey(0)



