import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread('white_5.jpg')

clone = img.copy()
gray = cv2.cvtColor(clone, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray,1)
brightness_increase = 10    
brightened_image = np.clip(gray.astype(np.int16) + brightness_increase, 0, 255).astype(np.uint8)
ret,gray_threshed = cv2.threshold(brightened_image,np.mean(gray)-20,255,cv2.THRESH_BINARY)

edge_detected_image = cv2.Canny(gray_threshed, 20, 200)

cv2.imshow('threshold', gray_threshed)
cv2.imshow('canny', edge_detected_image)
    
contours, _= cv2.findContours(edge_detected_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contour_list = []
for contour in contours:

    approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    area = cv2.contourArea(contour)
    if ((len(approx) > 8) & (area > 1000)):
        print(area)
        contour_list.append(contour)
        x,y,w,h = cv2.boundingRect(approx)
        cv2.rectangle(clone, (x,y), (x+w , y+h) , (0,255,0), 2)
        cv2.putText(clone, "area: " + str(int(area)), (x+w-5, y + h ), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.6, (0,255,0), 1)

print(len(contour_list))

cv2.drawContours(clone, contour_list,  -1, (255,0,0), 2)

cv2.imshow("Treshed", clone)

cv2.waitKey(0)
cv2.destroyAllWindows()

