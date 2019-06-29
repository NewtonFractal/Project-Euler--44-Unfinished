import math
Pentagon_Numbers = []


def Pentagon_number_generator(n):
    x = int((n*(3*n-1))/2)
    print(x)


for x in range(1,100):
    Pentagon_number_generator(x)

inverse = (math.sqrt(24*x+1)+1)/6
