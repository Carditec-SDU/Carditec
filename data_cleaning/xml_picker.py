import os
import glob
from shutil import copyfile

source_path = "/home/yingbing/data/7_1/Tricycle/"
target_path = "/home/yingbing/data/Ori/"

xml_file_list = open(source_path + "index", 'r')
xmls = xml_file_list.read().split('\n')

base = 20141
i = 1

for target in xmls:
    try:
        copyfile(source_path+str(target), 
            target_path+str(base+i)+'.JPEG')
    except:
        continue
    i = i+1


