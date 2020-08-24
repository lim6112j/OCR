import cv2
import pytesseract
import sys
# img = cv2.imread('images/old3.png')
img = cv2.imread('images/old.png')
kSize = int(sys.argv[1])
img = cv2.GaussianBlur(img, (kSize, kSize), sigmaX=0)
h, w, c = img.shape
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(thresh, blackAndWhiteImage) = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# img = cv2.bitwise_not(blackAndWhiteImage)
# cv2.imshow('gray', gray)
# img = gray
print(thresh)
# img = blackAndWhiteImage
boxes = pytesseract.image_to_boxes(img, lang="kor", config="-c tessedit_char_whitelist=서울루나0123456789 --oem 0 --user-patterns kor.user-patterns") 
for b in boxes.splitlines():
    b = b.split(' ')
    print(b)
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)