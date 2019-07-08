# coding:utf-8
import os
import glob
from shutil import copyfile

source_path = "/home/yingbing/data/campusimg/333/"
target_path = "/home/yingbing/data/sdata/"

target_file_list = open(source_path + "/index", "r")
targets = target_file_list.read()
targets = targets.split('\n')
# print(targets)

i = 700

for target in targets:
    try:
        copyfile(source_path+str(target)
             , target_path+str(i)+".jpg")

        i = i + 1
        
    except:
        continue