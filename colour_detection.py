import cv2 as cv
import numpy as np

#Read the Image from path
img = cv.imread("Test_Image.jpeg")

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

lower_white = np.array([0,0,0])
upper_white = np.array([0,0,229])

#Set Masks
mask1 = cv.inRange(img_HSV, lower_yellow, upper_yellow)
mask2 = cv.inRange(img_HSV, lower_green, upper_green)
mask3 = cv.inRange(img_HSV, lower_red, upper_red)
mask4 = cv.inRange(img_HSV, lower_blue, upper_blue)
mask5 = cv.inRange(img_HSV, lower_orange, upper_orange)
mask6 = cv.inRange(img_HSV, lower_white, upper_white)

#Get contours of a given image, here we'll be using the masks
def getContours(img):

	contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
	boxes = []

	for cnt in contours:
		area = int(cv.contourArea(cnt))

		if((area > 500) or (((area)<250) and (area>220))):
			boxes.append(cnt)

	return boxes

#Get the center of a given contour of a square
def getCenter(cnt):

	center = {}

	peri = cv.arcLength(cnt, True) #Gets the perimeter of the contour.
	approx = cv.approxPolyDP(cnt, 0.02*peri, True) #Get the corner points

	width = abs(approx[0][0][0] - approx[2][0][0])
	height = abs(approx[0][0][1] - approx[2][0][1])

	center["x"] = approx[0][0][0] + int(width/3)
	center["y"] = approx[1][0][1] - int(height/2)

	return center

#Get the squares
yellow_boxes = {"box": getContours(mask1), "colour": "Yellow"}
green_boxes = {"box": getContours(mask2), "colour": "Green"}
red_boxes = {"box": getContours(mask3), "colour": "Red"}
blue_boxes = {"box": getContours(mask4), "colour": "Blue"}
orange_boxes = {"box": getContours(mask5), "colour": "Orange"}
white_boxes = {"box": getContours(mask6), "colour": "White"}

final_boxes = [yellow_boxes, green_boxes, red_boxes, blue_boxes, orange_boxes, white_boxes]

for boxes in final_boxes:
	for box in boxes["box"]:
		box_center = getCenter(box)
		cv.putText(img, boxes["colour"], (box_center["x"], box_center["y"]), cv.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0))

#Show the labelled image in a new window
cv.imshow("New", img)

#Delay so that output window is visible
cv.waitKey(0)
cv.destroyAllWindows()