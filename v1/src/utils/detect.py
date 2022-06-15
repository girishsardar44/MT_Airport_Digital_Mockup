import numpy as np
import cv2

img = cv2.imread('coruna_simple.png')
imgGry= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(imgGry, 200, 300,apertureSize = 5)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30 , maxLineGap=20)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1,y1),(x2,y2), (0, 0, 200),1)

cv2.imshow("lineEdges", edges)
cv2.imshow("linesDetected", img)
cv2.waitKey(0)
cv2.destroyAllWindows()