import cv2 as cv
import numpy as np

#Read the Image from path
img = cv.imread("C:/Users/IB/Desktop/Test_Image.jpg")

#Convert Image to HSV format
img_HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

#HSV value range for different colours
lower_yellow = np.array([22, 50, 0])
upper_yellow = np.array([56, 255, 255])

lower_green = np.array([33, 30, 30])
upper_green = np.array([117, 255, 255])

lower_red = np.array([0, 30, 39])
upper_red = np.array([17, 255, 255])

lower_blue = np.array([64, 30, 0])
upper_blue = np.array([174, 255, 255])

lower_orange = np.array([4, 29, 20])
upper_orange = np.array([25, 255, 255])

#Set Masks
mask1 = cv.inRange(img_HSV, lower_yellow, upper_yellow)
mask2 = cv.inRange(img_HSV, lower_green, upper_green)
mask3 = cv.inRange(img_HSV, lower_red, upper_red)
mask4 = cv.inRange(img_HSV, lower_blue, upper_blue)
mask5 = cv.inRange(img_HSV, lower_orange, upper_orange)

#Get Mask contours
contours1 = (cv.findContours(mask1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE))[0]
contours2 = (cv.findContours(mask2, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE))[0]
contours3 = (cv.findContours(mask3, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE))[0]
contours4 = (cv.findContours(mask4, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE))[0]
contours5 = (cv.findContours(mask5, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE))[0]


#If any contour has an area of greater than 500 pixels, get the center of the contour and set label

#For yellow squares
for cnt in contours1:
	area1 = cv.contourArea(cnt)

	if (area1 > 500) :
		M = cv.moments(cnt)
		cx = int(M["m10"]/M["m00"])  #Get Center of the contour
		cy = int(M["m01"]/M["m00"])

		cv.putText(img, "Yellow", (cx-20, cy), cv.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0))

#For Green squares
for cnt in contours2:
	area2 = cv.contourArea(cnt)

	if (area2 > 500) :
		M = cv.moments(cnt)
		cx = int(M["m10"]/M["m00"])	#Get Center of the contour
		cy = int(M["m01"]/M["m00"])

		cv.putText(img, "Green", (cx-20, cy), cv.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0))

#For Red squares
for cnt in contours3:
	area3 = cv.contourArea(cnt)

	if (area3 > 500) :
		M = cv.moments(cnt)
		cx = int(M["m10"]/M["m00"])	#Get Center of the contour
		cy = int(M["m01"]/M["m00"])

		cv.putText(img, "Red", (cx-20, cy), cv.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0))

#For Blue squares
for cnt in contours4:
	area4 = cv.contourArea(cnt)

	if (area4 > 500) :
		M = cv.moments(cnt)
		cx = int(M["m10"]/M["m00"])	#Get Center of the contour
		cy = int(M["m01"]/M["m00"])

		cv.putText(img, "Blue", (cx-20, cy), cv.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0))

#For Orange squares
for cnt in contours5:
	area5 = cv.contourArea(cnt)

	if (area5 > 500) :
		M = cv.moments(cnt)
		cx = int(M["m10"]/M["m00"]) #Get Center of the contour
		cy = int(M["m01"]/M["m00"])

		cv.putText(img, "Orange", (cx-20, cy), cv.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0))

#Show the labelled image in a new window
cv.imshow("New", img)

#Delay so that output window is visible
cv.waitKey(0)