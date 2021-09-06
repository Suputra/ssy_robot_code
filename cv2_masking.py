import cv2
import time
import numpy as np

tree = cv2.imread(r"/home/syechuri6/tree.jpg", 1)

print(tree.shape)

(rows, cols, depth) = tree.shape

mask = np.zeros((rows,cols), dtype="uint8")
cv2.rectangle(mask, (200, 200), (550, 400), 255, -1)
masked = cv2.bitwise_and(tree, tree, mask=mask)

cv2.imshow("tree, but just this part", masked)
cv2.waitKey(5000)
cv2.destroyAllWindows()
