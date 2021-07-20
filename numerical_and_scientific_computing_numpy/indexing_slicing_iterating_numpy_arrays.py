#indexing

import cv2
import numpy

im_g=cv2.imread("smallgray.png", 0)
print(im_g)
print(im_g.shape)
print(im_g[0:2, 2:4])


# iterating
for i in im_g:
    print(i)
#prints the rows because i represents rows within the outer array
for i in im_g.T:
    print(i)
#transpose to iterating other way
for i in im_g.flat:
    print(i)
# iteratings on each number individually by flattening the arrays
print(" ")

#stacking and splitting numpy arrays
ims = numpy.hstack((im_g, im_g))
print(ims)
#stores the array side by side within one larger array, you can add many arrays but must be fed is as a tuple

imv = numpy.vstack((im_g, im_g))
print(imv)
# vertically stacks

lst = numpy.hsplit(ims, 2)
print(lst)
# you can split howver you want as long as it produces even sizes. you could use this to split by row/ column, or two split merged arrays
