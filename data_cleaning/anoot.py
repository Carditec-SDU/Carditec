# coding: utf-8
# 找出未被标记的图片

jpeg_names = []
xml_names = []

jpeg_file = open("index", 'r')
lines = jpeg_file.read()
lines = lines.split('\n')
for line in lines:
    try:
        # print(line)
        line = line.split('_')[1]
        line = line.split('.')[0]
        jpeg_names.append(line)
    except:
        continue

xml_file = open("xml.index", 'r')
xml_lines = xml_file.read()
xml_lines = xml_lines.split('\n')
for xml_line in xml_lines:
    try:
        xml_line = str(xml_line).split('_')[1]
        xml_line = xml_line.split('.')[0]
        xml_names.append(xml_line)
        # xml_line = xml_file.readline
    except:
        continue

target_names = []
for name in jpeg_names:
    # jpeg_names.remove(name)
    if name not in xml_names:
        name_switch = name + '\n'
        target_names.append(name_switch)

# print(target_names)
unanoo_file = open("target.index", "w")
unanoo_file.writelines(target_names)


