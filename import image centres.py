import cv2
import numpy as np
import matplotlib.pyplot as plt

from reference_OMR import reference_image
from student_OMR import student_image

image1=cv2.imread(r"omr images\new1.png")
image2=cv2.imread(r"omr images\new2.png")

r_data=reference_image(image1)
s_data=student_image(image2)

#print("reference OMR centres : \n",r_data)
#print("student OMR centres : \n",s_data)

count=0
for i in range(1,21,1):
    a=np.sum(np.square((r_data[i]-s_data[i])),axis=0)
    #print(a)
    if a <= 49:
        count=count+1

print("total marks is : ",count)
print(" GANGOTRI MISHRA OFFICIAL (gangotricertification)")
