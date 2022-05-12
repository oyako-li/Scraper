import cv2
import numpy as np

img = cv2.imread('data/numbers.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

clahe = cv2.createCLAHE(clipLimit =10)
contrast = clahe.apply(v)

canny = cv2.Canny(contrast, 20, 110)
cv2.imshow('i', img)
cv2.imshow('v', v)
cv2.imshow('c', contrast)
cv2.imshow('canny', canny)
cv2.waitKey(0)

cv2.imwrite("edges.png", canny)
