import cv2
import numpy as np
import math
import random
img=cv2.imread('D:\cube\Cube-solve\\test_photo\\t1.jpg')
rows=img.shape[0]
cals=img.shape[1]
a=img[int(rows/2):rows,0:cals]
cv2.imwrite('t2.jpg',a)
cals=int(cals/2)
p1=np.float32([[800,0],[3200,0],[800,800],[800,3200]])
p2=np.float32([[0,0],[4000,0],[0,1600],[4000,1600]])
M=cv2.getPerspectiveTransform(p1,p2)
c=cv2.warpPerspective(a,M,(rows,cals))
cv2.imwrite('t4.jpg',c)
