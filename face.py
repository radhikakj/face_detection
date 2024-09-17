import cv2
hm="haarcascade_frontalface_default.xml"
haar_cascade= cv2.CascadeClassifier(hm)
cam= cv2.VideoCapture(0)
_,img=cam.read()
grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=haar_cascade.detectMultiScale(grayImg,1.3,4)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),9)

cv2.imshow('face Detected',img)
cv2.imwrite('face.jpg',img)
