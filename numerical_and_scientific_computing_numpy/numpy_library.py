#numpy 
import numpy
n = numpy.arange(27)
print(n)
#prints numbers 1-26 in an array, as its only a one dimensional input

print(n.reshape(3,9))
#stores as a two dimensional array, 3 rows in nine columns

print(n.reshape(3,3,3))
#3x3 matrix repeated 3 times within an array

m = numpy.asarray([[123, 12, 123, 12, 33], [], []], dtype=object)
print(m)