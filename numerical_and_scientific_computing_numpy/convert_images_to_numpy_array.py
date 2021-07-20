#converting images
# requires the OpenCV library
import cv2

im_g=cv2.imread("smallgray.png", 0)
print(im_g)

# returns 
# [[187 158 104 121 143]
#  [198 125 255 255 147]
#  [209 134 255  97 182]]
#compare this to the picture in the directory, you can see the 255 is the white, and the lower number are the darker areas

col_im_g=cv2.imread("smallgray.png", 1)
print(col_im_g)
#returns 
# [[[187 187 187]   this is the blue layer
#   [158 158 158]
#   [104 104 104]
#   [121 121 121]
#   [143 143 143]]

#  [[198 198 198] # the green layer 
#   [125 125 125]
#   [255 255 255]
#   [255 255 255]
#   [147 147 147]]

#  [[209 209 209] # the red layer
#   [134 134 134]
#   [255 255 255]
#   [ 97  97  97]
#   [182 182 182]]]

#you get one array per colour layer, that overlay to create colour

#create image from numpy array
cv2.imwrite("newsmallgray.png", im_g)