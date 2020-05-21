import cv2
import numpy

img = cv2.imread("lena.tif")
cv2.namedWindow("lena")
cv2.imshow("lena",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(img.shape)