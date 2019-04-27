import cv2
import numpy as np
from matplotlib import pyplot as plt
import numpy as np

#the image size is 1944x2592
img = cv2.imread('Bookshelf2.jpg',0)
edges = cv2.Canny(img,100,200)

ret,thresh = cv2.threshold(img,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img = cv2.drawContours(img, contours, -1, (0,255,0), 3)

cv2.imshow('new', img)

