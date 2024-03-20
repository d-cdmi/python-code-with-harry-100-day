marks = [15,48,63,41,25,1,85,64,20,1]
index = 0
for mark in marks:
    print(mark)
    if index==3:
        print('good')
    index +=1



for mark,index in enumerate(marks,start=1):  # start number index start
    print(mark)
    if index==3:
        print('good')
    index +=1