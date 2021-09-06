import numpy as np
import cv2

cap = cv2.VideoCapture(0)
dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_APRILTAG_36h11)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    (corners, ids, _) = cv2.aruco.detectMarkers(gray, dictionary)
    if len(corners) > 0:
        cv2.aruco.drawDetectedMarkers(frame, corners)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

cap.release()
cv2.destroyAllWindows()