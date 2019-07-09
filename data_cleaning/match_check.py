dir = "/home/yingbing/data/sdata_416/"

index_file = open(dir+"index", "r")
lines = index_file.read().split('\n')

for line in lines:
    num = line.split('.')[0]
    try:
        open(dir+str(num)+".jpg", "r")
        print("checked: "+str(num))
        checked += 1
    except:
        print(num)

print(checked)
