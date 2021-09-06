import cv2
import numpy as np

tree = cv2.imread(r"/home/syechuri6/tree.jpg", 1)

print(tree.shape)

(rows, cols, depth) = tree.shape

fliptree = tree[range(rows-1, 0, -1), :, :]


cv2.imshow("tree in Australia", fliptree)
cv2.waitKey(5000)
cv2.destroyAllWindows()
