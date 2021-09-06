import cv2
import apriltag

orig = cv2.imread(r"/home/syechuri6/apriltags_36h11.png", 1)
img = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
font = cv2.FONT_HERSHEY_SIMPLEX
detector = apriltag.Detector(apriltag.DetectorOptions(families='tag36h11'))

tags = detector.detect(img)
for tag in tags:
    id = str(tag.tag_id)
    for i in range(4):
        point = [int(x) for x in tag.corners[i]]
        cv2.circle(orig, point, 2, (255, 0, 0), 10)
        cv2.putText(orig, str(tag.tag_id), [x + 7 for x in point], font, 0.8, (255, 0, 0), 1)


cv2.imshow('AprilTags:', orig)

cv2.waitKey(10000)
cv2.destroyAllWindows()