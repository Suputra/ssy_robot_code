import cv2
import time
import numpy as np

tree = cv2.imread(r"/home/syechuri6/tree.jpg", 1)

print(tree.shape)

(rows, cols, depth) = tree.shape

cv2.line(tree, (200, 200), (550, 400), (255, 255, 255), 10)
cv2.rectangle(tree, (200, 200), (550, 400), (255, 255, 255), 10)
cv2.circle(tree, (375, 300), 100, (255, 255, 255), 10)

cv2.imshow("tree, but with random shapes on it", tree)
cv2.waitKey(0)
cv2.destroyAllWindows()
