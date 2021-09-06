import cv2
import time
import numpy as np

tree = cv2.imread(r"/home/syechuri6/tree.jpg", 1)

print(tree.shape)

(rows, cols, depth) = tree.shape

for i in range(rows-1):
     tree[i,:,:] = np.zeros((1,cols,depth))
     cv2.imshow("climate change", tree)
     cv2.waitKey(20)


cv2.imshow("tree", tree) 
cv2.waitKey(10000)
cv2.destroyAllWindows()
