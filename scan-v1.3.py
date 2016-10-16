# -*- coding: utf-8 -*-
import csv
import numpy as np

f=[file("./output0999.txt",'a'),file("./output1999.txt",'a'),file("./output2999.txt",'a'),file("./output3999.txt",'a')]
#准备分开存到四个文件里，每个放1000张图的处理结果
csvfile = file("./train.csv")

lines = csv.reader(csvfile)

currentPicId=0; #当前正在处理的照片id

b=np.zeros((720,640),dtype=np.int) #无法 np.zeros((4000,720,640))，内存不够

for line in lines:
    pId=int(line[0])
    x1=int(line[1])/2
    y1=int(line[2])
    x2=int(line[3])/2
    y2=int(line[4])
    if(pId!=currentPicId): #说明跳到了“下一张”图（如果pId有变化，则currentId就相对来说是”上一张“图的id
        f_idx=currentPicId/1000 #用”上一张“图的id/1000得到的数字来决定它应该写在哪个output.txt里
        print "writing"+str(f_idx) #显示当前正在往哪里写数据
        csv_writer=csv.writer(f[f_idx])
        for j in range(0,720):
            csv_writer.writerow(b[j]) #执行写入
        
        b=np.zeros((720,640),dtype=np.int) #处理完一张图之后重新初始化b
        currentPicId=pId
       
    b[y1:y2,x1:x2]=1

#补上最后一张图（因为pId发生变化才会触发”写入“，最后一张图的处理结果的写入需要自己手动触发）--------
f_idx=pId/1000
print "writing"+str(f_idx)
csv_writer=csv.writer(f[f_idx])
for j in range(0,720):
    csv_writer.writerow(b[j])
#---------------------------------------------------------

f[0].close()
f[1].close()
f[2].close()
f[3].close()
csvfile.close()