import cv2
import numpy as np

img = cv2.imread("white_3.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
brightness_increase = 35  # Adjust the value as desired
brightened_image = np.clip(gray.astype(np.int16) + brightness_increase, 0, 255).astype(np.uint8)
blur = cv2.medianBlur(brightened_image,3)

#thresh = cv2.threshold(blur,60 ,255,cv2.THRESH_BINARY)

circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1,minDist= 40, param1 = 100, param2 = 30, minRadius = 5)
circles = np.uint16(np.around(circles))
print(circles)

for i in circles[0, :]:
    cv2.circle(img, (i[0], i[1]), i[2]-10, (0,255,0), 2)
    cv2.circle(img, (i[0], i[1]), 2, (0,255,0), 3)


cv2.imshow("detected", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
