import numpy as np
import cv2

arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
tag = np.zeros((300, 300, 1), dtype="uint8")

for id in range(50):
    print(id)
    cv2.aruco.drawMarker(arucoDict, id, 300, tag, 1)
    cv2.imshow('ArUco Marker:', tag)
    if cv2.waitKey(1000) & 0xFF == ord('e'):
        break

cv2.destroyAllWindows()