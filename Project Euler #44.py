import math
import time
start = time.time()
Pentagon_Numbers = []

def Pentagon_number_generator():
    for x in range(100,3000):
        Pentagon_Numbers.append(int((x*(3*x-1))/2))

Pentagon_number_generator()

def Finder():
    for x in Pentagon_Numbers:
        for y in Pentagon_Numbers:
            if x > y:
                if ((math.sqrt(24*(x+y)+1)+1)/6).is_integer() and ((math.sqrt(24*(x-y)+1)+1)/6).is_integer() == True:
                    print(abs(x - y))
                    end = time.time()
                    print(end - start)
                    return None
            else:
                break

Finder()
