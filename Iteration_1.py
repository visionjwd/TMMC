import cv2
import numpy as np
#import imutils

def nothing(x):
    pass

img = cv2.imread('White_6.jpg')


cv2.namedWindow('Treshed')

cv2.createTrackbar('Treshold','Treshed',0,255,nothing)


while(1):
  
    clone = img.copy()
    
    gray = cv2.cvtColor(clone, cv2.COLOR_BGR2GRAY)
    
    r = cv2.getTrackbarPos('Treshold','Treshed')
    
    ret,gray_threshed = cv2.threshold(gray,r,255,cv2.THRESH_BINARY)
    
    bilateral_filtered_image = cv2.bilateralFilter(gray_threshed, 5, 175, 175)
    
    edge_detected_image = cv2.Canny(bilateral_filtered_image, 75, 200)
    
    contours, _= cv2.findContours(edge_detected_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contour_list = []
    for contour in contours:

        approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
        area = cv2.contourArea(contour)
        if ((len(approx) > 6) & (area > 1000) ):
            contour_list.append(contour)
    

    cv2.drawContours(clone, contour_list,  -1, (255,0,0), 2)

    print('Number of found circles: {}'.format(int(len(contour_list)/2)))
     
    cv2.imshow('Objects Detected', clone)
    cv2.imshow("Treshed", gray_threshed)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()