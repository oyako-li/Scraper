import numpy as np
import cv2


cap = cv2.VideoCapture(0)
while True:
    screen =  np.array(ImageGrab.grab())
    ret, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #Help
    lower = np.array([22, 93, 0])
    upper = np.array([45, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)

    cv2.imshow('screen', mask)



    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break