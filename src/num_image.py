import cv2
import numpy as np

img = cv2.imread('data/number_detection1.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
b, g, r = cv2.split(img)
h, s, v = cv2.split(hsv)

# # clahe = cv2.createCLAHE(clipLimit =10)
# # contrast = clahe.apply(v)

# # canny = cv2.Canny(contrast, 20, 110)

ret,r1 = cv2.threshold(r,200,210,cv2.THRESH_BINARY)
ret,g1 = cv2.threshold(g,190,200,cv2.THRESH_BINARY)
ret,b1 = cv2.threshold(b,200,210,cv2.THRESH_BINARY)
ret,h1 = cv2.threshold(h,200,210,cv2.THRESH_BINARY)
ret,s1 = cv2.threshold(s,200,210,cv2.THRESH_BINARY)
ret,v1 = cv2.threshold(v,200,210,cv2.THRESH_BINARY)
# th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
#             cv2.THRESH_BINARY,11,2)
# th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
#             cv2.THRESH_BINARY,11,2)

cv2.imshow('i', img)
cv2.imshow('b', b1)
cv2.imshow('g', g1)
cv2.imshow('r', r1)
cv2.imshow('h', h1)
cv2.imshow('s', s1)
cv2.imshow('v', v1)
cv2.imshow('stack', v1+r1+g1)
#Help
# lower = np.array([22, 93, 0])
# upper = np.array([45, 255, 255])

# mask = cv2.inRange(hsv, lower, upper)

# cv2.imshow('screen', mask)

# cv2.imshow('stack',  cv2.addWeighted(r1, g1, v1, 0.0))
# cv2.imshow('canny', canny)
cv2.waitKey(0)

# cv2.imwrite("data/detection0.png", canny)
# s, hが良さそう