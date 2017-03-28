import cv2
import numpy as np

camera = cv2.VideoCapture ("video.avi")
camera.open("video.avi")
car_cascade = cv2.CascadeClassifier('cars.xml')
while True:
    (grabbed,frame) = camera.read()
    grayvideo = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(grayvideo, 1.1, 1)
    for (x,y,w,h) in cars:
     cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
     cv2.imshow("video",frame)
    if cv2.waitKey(1)== ord('q'):
        break
camera.release()
cv2.destroyAllWindows()

