# -*- coding: utf-8 -*-
import math
import numpy as np

def scan(scanSize,step,x1,y1,x2,y2):
    #左上角网格的“坐标”
    left_up_x=math.ceil((x1-scanSize+step)/scanSize)
    left_up_y=math.ceil((y1-scanSize+step)/scanSize)
    #右下角网格的“坐标”
    right_bottom_x=math.ceil((x2-scanSize+step)/scanSize)
    right_bottom_y=math.ceil((y2-scanSize+step)/scanSize)
    
    #“左上坐标”~“右下坐标”全标为1    
    while(left_up_y<=right_bottom_y):
        
        while(left_up_x<=right_bottom_x):
            # 执行“标记为1”动作
            
            left_up_x+=1
        left_up_y+=1

##abort 10.15 11:24