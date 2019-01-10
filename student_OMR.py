import numpy as np
import cv2
import matplotlib.pyplot as plt

image2=cv2.imread(r"omr images\new2.png")
def student_image(image2):
    image=image2
    height, width, depth = image.shape
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    canny=cv2.Canny(blur,50,150)
    polygons=np.array([[(71,140),(185,140),(185,426),(71,426)],[(228,140),(340,140),(340,426),(228,426)]])
    lower=np.array([0,0,0])
    upper=np.array([15,15,15])
    shape=cv2.inRange(image,lower,upper)
    mask=np.zeros_like(canny)
    mask=cv2.fillPoly(mask,polygons,255)
    masked_image2=cv2.bitwise_and(shape,mask)
    imagem = cv2.bitwise_not(masked_image2)
    #cv2.imshow("gray",gray)
    blur=cv2.GaussianBlur(imagem,(5,5),0)
    #cv2.imshow("blur",imagem)
    _, contours, _= cv2.findContours(imagem, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contour_list = []
    cnt=np.array(contours)
    for contour in contours:
        approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
        area = cv2.contourArea(contour)
        if ((len(approx) > 8) & (area > 30) ):
            contour_list.append(contour)
    cv2.drawContours(image, contour_list,  -1, (255,0,0), 2)
    b=(np.max(cnt[0],axis=0)+np.min(cnt[0],axis=0))/2
    b=b.astype(int)
    #print("initial2",b)
    count=2
    for i in range(1,21,1):
        b=np.insert(b,count,(((np.max(cnt[i],axis=0)+np.min(cnt[i],axis=0))/2).astype(int))[0])
        a=(np.max(cnt[i],axis=0)+np.min(cnt[i],axis=0))/2
        a=a.astype(int)
        cv2.circle(image,(a[0][0],a[0][1]),5,(0,255,0),-1)
    cv2.imshow("detected point",image)
    b=b.reshape(21,2)
    return b

student_image(image2)
#-----print(" GANGOTRI MISHRA OFFICIAL (gangotricertification)")-----#

