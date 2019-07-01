import xml.etree.ElementTree as ET
from os import getcwd

sets=[('2007', 'train'), ('2007', 'val'), ('2007', 'test')]

classes = ["Bus", "Microbus", "MiniVan", "Sedan", "SUV", "Truck", "Bicycle", "DoubleDeck", "Electromobile", "FireTruck", "Motorcycle", "Motorhome", "PoliceCar", "RacingCar", "SchoolBus", "Tricycle"]

def convert_annotation(image_id, list_file):

    try:
        in_file = open('/home/yingbing/data/xmls/%s'%(image_id))
        tree=ET.parse(in_file)
        root = tree.getroot()

        for obj in root.iter('object'):
            difficult = obj.find('difficult').text
            cls = obj.find('name').text
            if cls not in classes :
                print(image_id)
                continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
            list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))
    except:
        return

wd = getcwd()

for year, image_set in sets:

    image_ids = open('/home/yingbing/data/xmls/index.txt','r').read().split('\n')
    
    list_file = open('/home/yingbing/dl/keras-yolo3/model_data/annot_new.txt', 'w')
    
    print(image_ids)

    for image_id in image_ids:
        iamge_id_n = image_id.split('.')[0]
        list_file.write('./data/%s.jpg'%iamge_id_n)
        convert_annotation(image_id, list_file)
        list_file.write('\n')
    list_file.close()
