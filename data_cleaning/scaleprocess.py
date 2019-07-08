import cv2

import numpy as np

# address = "D:\\BaiduNetdiskDownload\\BITVehicle_Dataset (2)\\NewNewBITVehicle_Dataset\\"
# saveaddress = "D:\\BaiduNetdiskDownload\\BITVehicle_Dataset (2)\\NewNewNewBITVehicle_Dataset\\"

address = "/home/yingbing/data/sdata/"
saveaddress = "/home/yingbing/data/sdata_416/"

times = 805


for i in range(1,times+1):
    img = cv2.imread(address+str(i)+".jpg")

    #cv2.imshow("img",img)
    #filterimg = cv2.bilateralFilter(img,5,7,15)
    #v2.imshow("filterimg",filterimg)

    img = cv2.resize(img,dsize=(416,416))
    cv2.imwrite(saveaddress+str(i)+".jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 50])
    if(i%100==0):
        print("第"+str(i)+"张图片处理")
    #cv2.imshow("equimg",equimg)


    #cv2.waitKey(0)
