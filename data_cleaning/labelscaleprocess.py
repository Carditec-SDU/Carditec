
import cv2
times = 21880
ori_txt = open('/home/yingbing/dl/keras-yolo3/model_data/annot_new.txt','r')
data_txt = open("labelscaledata.txt","w")
address = "/home/yingbing/data/Ori/"
x = 416
y = 416

#print(data_frame.loc[1]["imgnumber"].astype("str"))

for i in range(1,times+1):
    
    ori_line = ori_txt.readline()
    blank_line = ori_line.split()
    merge_line = blank_line[0]+" "

    file_name = blank_line[0].split('/')[-1]
    file_name = file_name.split('.')[0]

    try:
        img = cv2.imread(address + file_name + ".JPEG")
        x_before = img.shape[1]
        y_before = img.shape[0]
        x_scale = x_before/x
        y_scale = y_before/y
    except:
        img = cv2.imread(address + file_name + ".jpg")
        x_before = img.shape[1]
        y_before = img.shape[0]
        x_scale = x_before/x
        y_scale = y_before/y

    for k in range(1,len(blank_line)):
        forcomma_line = blank_line[k]
        comma_line = forcomma_line.split(",")
        flag = 1
        for xynumber in comma_line:
            if(flag == 1 or flag ==3):
                xynumber = str(int(int(xynumber)/x_scale))
                merge_line = merge_line+xynumber+","
                flag=flag+1
                continue
            if(flag == 2 or flag == 4):
                xynumber = str(int(int(xynumber)/y_scale))
                merge_line = merge_line+xynumber+","
                flag=flag+1
                continue
            if(flag == 5):
                merge_line = merge_line+xynumber+" "
    data_txt.writelines(merge_line+"\n")












