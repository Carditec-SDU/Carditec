import xml.etree.ElementTree as ET
from os import getcwd

work_dir = "/home/yingbing/data/7_1/Tricycle/"

def convert_annotation(name):
    in_file = open(work_dir+str(name))
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        obj.find('name').text = "Tricycle"
    
    tree.write(work_dir+str(name))
    in_file.close()

index_file = open(work_dir+"xml.index", "r")
names = index_file.read()
names = names.split('\n')
for name in names:
   # print(name)
    try:
        convert_annotation(name)
    except:
        continue