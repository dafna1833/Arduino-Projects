import cv2
import numpy as np
from matplotlib import pyplot as plt
import numpy as np

#the image size is 1944x2592
img = cv2.imread('Bookshelf2.jpg',0)
edges = cv2.Canny(img,100,200,10)

cv2.imshow('new', edges)

