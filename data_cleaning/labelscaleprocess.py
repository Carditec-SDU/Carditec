import pandas as pd
import cv2
times = 21880
ori_txt = open('/home/yingbing/dl/keras-yolo3/model_data/annot_new.txt'，'r')
data_txt = open("labelscaledata.txt","w")
address = "/home/yingbing/data/Ori"
x = 416
y = 416



#print(data_frame.loc[1]["imgnumber"].astype("str"))

for i in range(0,times):
    img = cv2.imread(address + str(i) + ".jpg")
    x_before = img.shape[1]
    y_before = img.shape[0]
    x_scale = x_before/x
    y_scale = y_before/y
    ori_line = ori_txt.readline()
    blank_line = ori_line.strip("\n")
    for k in blank_line:
        comma_line = blank_line[k+1].strip(",") 
        


    if(i == times):
        a = data_frame.loc[i-1]
        line = "./data/" + data_frame.loc[i-1]["imgnumber"].astype("str") + ".jpg" + " " + (
            str(int(data_frame.loc[i - 1][
                        "location1"] / x_scale))) + "," + (str(int(data_frame.loc[i-1][
                                                                       "location2"] / y_scale))) + "," + (
                   str(int(data_frame.loc[i - 1][
                               "location3"] / x_scale))) + "," + (str(int(data_frame.loc[i - 1][
                                                                              "location4"] / y_scale))) + "," + \
               data_frame.loc[i - 1]["category"] + "\n"
    if (data_frame.loc[i]["imgnumber"] is None):
        line = "./data/" + data_frame.loc[i-1]["imgnumber"].astype("str") + ".jpg" + " " + (str(int(data_frame.loc[i-1][
            "location1"]/x_scale)))+ "," + (str(int(data_frame.loc[i-1][
            "location2"]/y_scale)))+ "," + (str(int(data_frame.loc[i-1][
            "location3"]/x_scale)))+ "," + (str(int(data_frame.loc[i-1][
            "location4"]/y_scale)))+ "," + \
               data_frame.loc[i-1]["category"] + "\n"
        data_txt.writelines(line)
        continue
    if (data_frame.loc[i-1]["imgnumber"] == data_frame.loc[i]["imgnumber"]):
        if (data_frame.loc[i-1]["imgnumber"] == data_frame.loc[i+1]["imgnumber"]):
            line = line = "./data/" + data_frame.loc[i-1]["imgnumber"].astype("str") + ".jpg" + " " + (str(int(data_frame.loc[i-1][
            "location1"]/x_scale)))+ "," + (str(int(data_frame.loc[i-1][
            "location2"]/y_scale)))+ "," + (str(int(data_frame.loc[i-1][
            "location3"]/x_scale)))+ "," + (str(int(data_frame.loc[i-1][
            "location4"]/y_scale))) + "," + data_frame.loc[i-1]["category"] + " " + (str(int(data_frame.loc[i][
            "location1"]/x_scale)))+ "," + (str(int(data_frame.loc[i][
            "location2"]/y_scale)))+ "," + (str(int(data_frame.loc[i][
            "location3"]/x_scale)))+ "," + (str(int(data_frame.loc[i][
            "location4"]/y_scale)))+ "," + data_frame.loc[i ]["category"] + " " + (str(int(data_frame.loc[i+1][
            "location1"]/x_scale)))+ "," + (str(int(data_frame.loc[i+1][
            "location2"]/y_scale)))+ "," + (str(int(data_frame.loc[i+1][
            "location3"]/x_scale)))+ "," + (str(int(data_frame.loc[i+1][
            "location4"]/y_scale))) + "," + data_frame.loc[i + 1]["category"] + "\n"
            data_frame = data_frame.drop(index=i )
            data_frame = data_frame.drop(index=i + 1)
            data_frame.index = range(len(data_frame))
            print(len(data_frame))
            data_txt.writelines(line)
        else:
            line = "./data/" + data_frame.loc[i-1]["imgnumber"].astype("str") + ".jpg" + " " + (str(int(data_frame.loc[i-1][
            "location1"]/x_scale)))+ "," + (str(int(data_frame.loc[i-1][
            "location2"]/y_scale)))+ "," + (str(int(data_frame.loc[i-1][
            "location3"]/x_scale)))+ "," + (str(int(data_frame.loc[i-1][
            "location4"]/y_scale)))+ "," + data_frame.loc[i-1]["category"] + " " + (str(int(data_frame.loc[i][
            "location1"]/x_scale)))+ "," + (str(int(data_frame.loc[i][
            "location2"]/y_scale)))+ "," + (str(int(data_frame.loc[i][
            "location3"]/x_scale)))+ "," + (str(int(data_frame.loc[i][
            "location4"]/y_scale)))+ "," + \
                   data_frame.loc[i]["category"] + "\n"
            data_frame = data_frame.drop(index=i)
            data_frame.index = range(len(data_frame))
            print(len(data_frame))
            data_txt.writelines(line)
    else:

        line = "./data/" + data_frame.loc[i-1]["imgnumber"].astype("str") + ".jpg" + " " + (str(int(data_frame.loc[i-1][
            "location1"]/x_scale)))+ "," + (str(int(data_frame.loc[i-1][
            "location2"]/y_scale)))+ "," + (str(int(data_frame.loc[i-1][
            "location3"]/x_scale)))+ "," + (str(int(data_frame.loc[i-1][
            "location4"]/y_scale)))+ "," + \
               data_frame.loc[i-1]["category"] + "\n"
        print(len(data_frame))
        data_txt.writelines(line)











