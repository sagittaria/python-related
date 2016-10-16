def scan(scanSize,step,x1,y1,x2,y2,picWidth,picHeight):
    scanX1=0
    scanY1=0
    Has_Not_Reached_Right=True
    Has_Not_Reached_Bottom=True
    while(Has_Not_Reached_Bottom):
        while(Has_Not_Reached_Right):
            scanX2=scanX1+scanSize
            scanY2=scanY1+scanSize
            #do some judge here
            
            #case1:total cover or be-covered
            if((scanX1<=x1 and scanY1<=y1 and scanX2>=x2 and scanY2>=y2) or (scanX1>=x1 and scanY1>=y1 and scanX2<=x2 and scanY2<=y2)):
                #output 1
            
            #case2:Scaner's right-bottom-corner in (x1,y1)&(x2,y2)
            if(
            
            
            scanX1+=step
            #Has_Not_Reached_Right?
    
    scanY1+=step
    #Has_Not_Reached_Bottom?

##abort 10.15 10:34