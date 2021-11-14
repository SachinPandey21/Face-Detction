import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('FB_IMG_1595146257606.jpg')        # image name ( image ki file present honi chahiye python ke folder me tb ye run krega)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (1, 0, 0), 2)          # 1 for colour of the rectangular box 

cv2.imshow('img', img)

cv2.waitKey()