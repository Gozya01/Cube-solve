import cv2
import numpy as np
import math 
import random
cube_str=[]
ans=[]
for num in range(1,7):
    imgobj = cv2.imread('D:\cube\Cube-solve\\test_photo\\'+str(num)+'.jpg')
    gray = cv2.cvtColor(imgobj, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    canny = cv2.Canny(blurred,30,30)
    kernel = np.ones((3,3), np.uint8)
    dilated = cv2.dilate(canny, kernel, iterations=2)
    eroded= cv2.erode(dilated,kernel)
    k=np.ones((3,3),np.uint8)
    img_four=cv2.dilate(eroded,k)
    content,d=cv2.findContours(img_four,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    c=sorted(content,key=lambda x:cv2.contourArea(x),reverse=True)
    a=c[0]


    leftmost=tuple(a[a[:,:,0].argmin()][0])
    rightmost=tuple(a[a[:,:,0].argmax()][0])
    topmost=tuple(a[a[:,:,1].argmin()][0])
    bottommost=tuple(a[a[:,:,1].argmax()][0])
    sx=min(leftmost[0],rightmost[0],topmost[0],bottommost[0])
    sy=min(leftmost[1],rightmost[1],topmost[1],bottommost[1])
    tx=max(leftmost[0],rightmost[0],topmost[0],bottommost[0])
    ty=max(leftmost[1],rightmost[1],topmost[1],bottommost[1])

    xd=(tx-sx)/3
    yd=(ty-sy)/3
    lst=[]
    for i in range(0,3):
        for j in range(0,3):
            b=imgobj[int(sy+i*yd):int(sy+(i+1)*yd),int(sx+j*xd):int(sx+(j+1)*xd)]
            b=cv2.resize(b,(100,100))
            #b=cv2.cvtColor(b,cv2.COLOR_BGR2HSV)
            cv2.imwrite(str(num)+str(i)+str(j)+'.jpg',b)
            lst.append(b)
    ans.append(lst)
def Check1(a):
    if a>=0 and a<=43:
        return 0
    return 100
def Check2(a):
    if a>=150:
        return 0
    return 100
def Judge(a):
    tmp=1e10
    id=0
    for i in range(0,6):
        tot=0
        for j in range(0,1000):
            x=random.randint(0,99)
            y=random.randint(0,99)
            tot+=1.0*(a[x][y][0]-ans[i][4][x][y][0])**2
            tot+=1.0*(Check1(a[x][y][1])-Check1(ans[i][4][x][y][1]))**2
            tot+=1.0*(Check2(a[x][y][2])-Check2(ans[i][4][x][y][2]))**2
        if tot<tmp:
            tmp=tot
            id=i
        print(i,id,tot)
    if id==0:
        return 'y'
    if id==1:
        return 'b'
    if id==2:
        return 'r'
    if id==3:
        return 'g'
    if id==4:
        return 'o'
    if id==5:
        return 'w'
f=open("str.txt",'w')
a=0
for i in range(0,1):
    for j in range(0,1):
        a=0
        f.write(str(Judge(ans[i][j])))