import cv2

img_data = cv2.imread("solar-system.jpg")

cv2.putText(img_data, "Sun", (100, 100), cv2.FONT_HERSHEY_COMPLEX, 2,(255,255,255))

cv2.putText(img_data, "Mercury", (120, 160), cv2.FONT_HERSHEY_COMPLEX, 0.5,(255,255,255))

cv2.putText(img_data, "Venus", (190, 260), cv2.FONT_HERSHEY_COMPLEX, 0.5,(255,255,255))

cv2.putText(img_data, "Earth", (290, 260), cv2.FONT_HERSHEY_COMPLEX, 0.5,(255,255,255))

cv2.putText(img_data, "Mars", (390, 260), cv2.FONT_HERSHEY_COMPLEX, 0.5,(255,255,255))

cv2.putText(img_data, "Jupiter", (470, 340), cv2.FONT_HERSHEY_COMPLEX, 0.5,(255,255,255))

cv2.putText(img_data, "Saturn", (720, 260), cv2.FONT_HERSHEY_COMPLEX, 0.5,(255,255,255))

cv2.putText(img_data, "Uranus", (970, 300), cv2.FONT_HERSHEY_COMPLEX, 0.5,(255,255,255))

cv2.putText(img_data, "Neptune", (1110, 290), cv2.FONT_HERSHEY_COMPLEX, 0.5,(255,255,255))



cv2.imshow("Solar System", img_data)

cv2.waitKey(0)

