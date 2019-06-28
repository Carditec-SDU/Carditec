# coding:utf-8
import os
import glob
from shutil import copyfile

source_path = "/mnt/e/数据集/车辆数据集/imagenet/Electromobile/"
target_path = "/mnt/e/target/Electromobile/"

target_file_list = open(source_path + "/target.index", "r")
targets = target_file_list.read()
targets = targets.split('\n')
print(targets)
for target in targets:
    # print(target)
    try:
         copyfile(source_path+"n03791053_"+str(target)+".JPEG"
             , target_path+str(target)+".JPEG")
    except:
        continue