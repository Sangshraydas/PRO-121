import cv2
import time
import numpy as np

#To save the output in a file output.avi
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

#Starting the webcam
cap = cv2.VideoCapture(0)

#Allowing the webcam to start by making the code sleep for 2 seconds
time.sleep(2)
bg = 0

#Capturing background for 60 frames
for i in range(60):
    ret, bg = cap.read()
#Flipping the background
bg = np.flip(bg, axis=1)

#Reading the captured frame until the camera is open
while (cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break
    #Flipping the image for consistency
    img = np.flip(img, axis=1)

    #Converting the color from BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #Generating mask to detect red colour
    #These values can also be changed as per the color
    u_black = np.array([0, 120, 50])
    r_black = np.array([10, 255,255])
    mask = cv2.inRange(frame,u_black,r_black)

    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask= cv2.inRange(hsv, lower_red, upper_red)

    #Open and expand the image where there is mask 1 (color)
    mask_1 = cv2.morphologyEx(mask_1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
  
    res_1 = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("magic", final_output)
    cv2.waitKey(1)


cap.release()
output_file.release()
cv2.destroyAllWindows()