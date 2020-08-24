import cv2
import pytesseract
import numpy as np
import sys
if(len(sys.argv)==1):
    print('need gausian value')
    exit(1)
img = cv2.imread('./images/Arial.png')

height, width, channel = img.shape
# cv2.imshow('img', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh, bw = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
gaussianBlurSize = int(sys.argv[1])
img_blurred = cv2.GaussianBlur(gray, ksize=(gaussianBlurSize, gaussianBlurSize), sigmaX=0)
cv2.imshow('blured', img_blurred)
c, h = cv2.findContours(img_blurred,     mode=cv2.RETR_LIST, 
    method=cv2.CHAIN_APPROX_SIMPLE)
temp_result = np.zeros((height, width, channel), dtype=np.uint8)
for contour in c:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(temp_result, pt1=(x, y), pt2=(x+w, y+h), color=(255, 255, 255), thickness=2)
cv2.imshow('bw', bw)
cv2.imshow('bound', temp_result)
cv2.waitKey(0)