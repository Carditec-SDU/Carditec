from shutil import copyfile

f = open('/home/yingbing/dl/keras-yolo3/labels/train_label_1.txt', 'r')
lines = f.read().split('\n')

f_out = open('/home/yingbing/data/test/annot.txt', 'w')

count_Bus = 80
count_Sedan = 100
count_SUV = 100
count_Truck = 100
count_Bicycle = 100
count_Electromobile = 80

for line in lines:

    contents = line.split(' ')

    name_string = contents[0].split('/')
    name = name_string[-1].split('.')
    name = name[0]

    if int(name) <= 810:
        continue

    box_string = contents[1].split(',')

    try:
        cls = int(box_string[-1])
    except:
        print(name)
        continue

    execute = False

    if cls == 0:
        count_Bus -= 1
        execute = True
        if count_Bus < 0:
            continue
    elif cls == 3:
        count_Sedan -= 1
        execute = True
        if count_Sedan < 0:
            continue
    elif cls == 4:
        count_SUV -= 1
        execute = True
        if count_SUV < 0:
            continue
    elif cls == 5:
        count_Truck -= 1
        execute = True
        if count_Truck < 0:
            continue
    elif cls == 6:
        count_Bicycle -= 1
        execute = True
        if count_Bicycle < 0:
            continue
    elif cls == 8:
        count_Electromobile -= 1
        execute = True
        if count_Electromobile < 0:
            continue
    
    if execute:
        source_file = "/home/yingbing/data/Adjresize/" + str(name) + ".jpg"
        target_file = "/home/yingbing/data/test/" + str(name) + ".jpg"

        # copyfile(source_file, target_file)

        boxes = contents[1:]
        print(boxes)

        new_line = contents[0]

        for box in boxes:
            box_attrs = box.split(',')
            try:
                cls = int(box_attrs[-1])
                print(cls)
            except:
                continue

            if cls==0:
                new_line += " "+box_attrs[0]+","+box_attrs[1]+","+box_attrs[2]+","+box_attrs[3]+","+"0"
            elif cls==3:
                # box_attrs[4] == '1'
                new_line += " "+box_attrs[0]+","+box_attrs[1]+","+box_attrs[2]+","+box_attrs[3]+","+"1"
            elif cls==4:
                # box_attrs[4] == '2'
                new_line += " "+box_attrs[0]+","+box_attrs[1]+","+box_attrs[2]+","+box_attrs[3]+","+"2"
            elif cls==5:
                # box_attrs[4] == '3'
                new_line += " "+box_attrs[0]+","+box_attrs[1]+","+box_attrs[2]+","+box_attrs[3]+","+"3"
            elif cls==6:
                # box_attrs[4] == '4'
                # print(box)
                new_line += " "+box_attrs[0]+","+box_attrs[1]+","+box_attrs[2]+","+box_attrs[3]+","+"4"
            elif cls==8:
                # box_attrs[4] == '5'
                new_line += " "+box_attrs[0]+","+box_attrs[1]+","+box_attrs[2]+","+box_attrs[3]+","+"5"

            # new_line += " "+box_attrs[0]+","+box_attrs[1]+","+box_attrs[2]+","+box_attrs[3]+","+box_attrs[4]
            print(new_line)

        f_out.write(new_line)
        f_out.write('\n')

