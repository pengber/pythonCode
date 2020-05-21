import cv2 as cv
import numpy as np
import math
import copy


gauss  = np.array([1,2,1,2,4,2,1,2,1])

def spilt( a ):
    if a/2 == 0:
        x1 = x2 = a/2
    else:
        x1 = math.floor( a/2 )
        x2 = a - x1
    return -x1,x2

def gaussian_b0x(a, b):
    judge = 10
    sum = 0
    box =[]
    x1, x2 = spilt(a)
    y1, y2 = spilt(b)
    for i in range (x1, x2 ):
        for j in range(y1, y2):
            t = i*i + j*j
            re = math.e ** (-t/(2*judge*judge))
            sum = sum + re
            box.append(re)

    box = np.array(box)
    box  = box / sum
    # for x in box :
    #     print (x)
    return box

def original (i, j, k,a, b,img):
    x1, x2 = spilt(a)
    y1, y2 = spilt(b)
    temp = np.zeros(a * b)
    count = 0
    for m in range(x1, x2):
        for n in range(y1, y2):
            if i + m < 0 or i + m > img.shape[0] - 1 or j + n < 0 or j + n > img.shape[1] - 1:
                temp[count] = img[i, j, k]
            else:
                temp[count] = img[i + m, j + n, k]
            count += 1
    return  temp

def gaussian_function(a, b, img, gauss_fun ):
    img0 = copy.copy(img)
    for i in range (0 , img.shape[0]  ):
        for j in range (2 ,img.shape[1] ):
            for k in range (img.shape[2]):
                temp =  original(i, j, k, a, b, img0)
                img[i,j,k] = np.average(temp ,weights = gauss_fun)#按权分配
    return  img

def main():
    gauss_new = gaussian_b0x(3 , 3)
    img0 = cv.imread(r"lena.tif")
    gauss_img = gaussian_function(3, 3, copy.copy(img0), copy.copy(gauss_new))
    cv.imshow("guassian_img", gauss_img)
    cv.imshow("yuantu", img0)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__  ==  "__main__":
    main()


