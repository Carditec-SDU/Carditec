import os
import glob
from shutil import copyfile
address = "C:\\Users\\shiraz\\Pictures\\n02834778\\"
address1 = "C:\\Users\\shiraz\\Pictures\\n02834778\\Annotation\\n02834778\\"
imageList1 = glob.glob(address+"tricycle\\*")
annotation = glob.glob(address1+"*")
annotationList = []
annotationnameList = []
image1 = []
imgname1 = []
image2 = []

for item in imageList1:
    image1.append(os.path.basename(item))

for item in image1:
    (temp1, temp2) = os.path.splitext(item)
    imgname1.append(temp1)
for item in annotation:
    annotationList.append(os.path.basename(item))
for item in annotationList:
    (temp1, temp2) = os.path.splitext(item)
    annotationnameList.append(temp1)

    for item1 in imgname1:
        if(temp1 == item1):
            copyfile(address1+temp1+".xml", address+"tricycle\\"+temp1+".xml")
            break
