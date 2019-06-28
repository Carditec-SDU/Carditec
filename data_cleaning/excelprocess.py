import pandas as pd

data_frame=pd.read_excel('C:\\Users\\shiraz\\Documents\\Tencent Files\\912751642\\FileRecv\\车辆标记信息.xlsx',skiprows=None)

col_name = data_frame.columns.tolist()
col_name.insert(7, "space")
col_name.insert(8,"location5")
col_name.insert(9,"location6")
col_name.insert(10,"location7")
col_name.insert(11,"location8")
col_name.insert(12,"location6")
col_name.insert(13,"category")
#pd.concat([df, pd.DataFrame(columns=list('DE'))])
#data_frame.reindex(columns = col_name,fill_value=None)
data_frame["space"] = None
data_frame["location5"] = None
data_frame["location6"] = None
data_frame["location7"] = None
data_frame["location8"] = None
data_frame["catagory"] = None

data_txt = open("data.txt","a+")
col_name = data_frame.columns.tolist()
print(col_name)
for i in range(9850):
    if(data_frame.loc[i+1]["imgnumber"] is None):
        line = "./data/" + data_frame.loc[i]["imgnumber"].astype("str") + ".jpg" + " " + data_frame.loc[i][
            "location1"].astype("str") + "," + data_frame.loc[i]["location2"].astype("str") + "," + data_frame.loc[i][
                   "location3"].astype("str") + "," + data_frame.loc[i]["location4"].astype("str") + "," + \
               data_frame.loc[i]["category"] + "\n"
        data_txt.writelines(line)
        continue
    if(data_frame.loc[i]["imgnumber"] == data_frame.loc[i+1]["imgnumber"]):
        if(data_frame.loc[i]["imgnumber"] == data_frame.loc[i+2]["imgnumber"]):
            line = line ="./data/"+data_frame.loc[i]["imgnumber"].astype("str")+".jpg"+" "+data_frame.loc[i]["location1"].astype("str")+","+data_frame.loc[i]["location2"].astype("str")+","+data_frame.loc[i]["location3"].astype("str")+","+data_frame.loc[i]["location4"].astype("str")+","+data_frame.loc[i]["category"]+" "+ data_frame.loc[i+1]["location1"].astype("str")+","+data_frame.loc[i+1]["location2"].astype("str")+","+data_frame.loc[i+1]["location3"].astype("str")+","+data_frame.loc[i+1]["location4"].astype("str")+","+data_frame.loc[i+1]["category"]+" "+data_frame.loc[i+2]["location1"].astype("str")+","+data_frame.loc[i+2]["location2"].astype("str")+","+data_frame.loc[i+2]["location3"].astype("str")+","+data_frame.loc[i+2]["location4"].astype("str")+","+data_frame.loc[i+2]["category"]+"\n"
            data_frame = data_frame.drop(index=i + 1)
            data_frame = data_frame.drop(index=i + 2)
            data_frame.index = range(len(data_frame))
            print(len(data_frame))
            data_txt.writelines(line)
        else:
            line ="./data/"+data_frame.loc[i]["imgnumber"].astype("str")+".jpg"+" "+data_frame.loc[i]["location1"].astype("str")+","+data_frame.loc[i]["location2"].astype("str")+","+data_frame.loc[i]["location3"].astype("str")+","+data_frame.loc[i]["location4"].astype("str")+","+data_frame.loc[i]["category"]+" "+ data_frame.loc[i+1]["location1"].astype("str")+","+data_frame.loc[i+1]["location2"].astype("str")+","+data_frame.loc[i+1]["location3"].astype("str")+","+data_frame.loc[i+1]["location4"].astype("str")+","+data_frame.loc[i+1]["category"]+"\n"
            data_frame = data_frame.drop(index=i+1)
            data_frame.index = range(len(data_frame))
            print(len(data_frame))
            data_txt.writelines(line)
    else:

        line = "./data/"+data_frame.loc[i]["imgnumber"].astype("str")+".jpg"+" "+data_frame.loc[i]["location1"].astype("str")+","+data_frame.loc[i]["location2"].astype("str")+","+data_frame.loc[i]["location3"].astype("str")+","+data_frame.loc[i]["location4"].astype("str")+","+data_frame.loc[i]["category"]+"\n"
        print(len(data_frame))
        data_txt.writelines(line)