# -*- coding: utf-8 -*-
import numpy as np

def gen(arr,x1,y,x2,y2):
    arr[x1:x2,y1:y2]=1

#生成0矩阵
arr=np.zeros((5,10))
x1=0
y1=0
x2=2
y2=2

print arr
gen(arr,x1,y1,x2,y2)
print arr