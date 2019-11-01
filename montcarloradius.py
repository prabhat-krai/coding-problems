"""
The area of a circle is defined as πr^2. Estimate π to 3 decimal places 
using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.


"""
#learning to run a monte carlo simulation

import random
import math
from numpy import mean
# Number of points inside the circle
inside = 0
# Total number of points to be generated
total = 10000
pi_list =[]

for _ in range(100):
    for i in range(0, total):
        # Generate random x, y in [0, 1].
        x2 = random.random()**2    #distance from origin of x-axis
        y2 = random.random()**2    #distance from origin of y-axis

        # Increment if inside unit circle.
        if(math.sqrt(x2 + y2) < 1.0): # seeing that the resulting point is inside the circle
            inside += 1

    # inside / total = pi / 4
    pi = (float(inside) / total) * 4
    pi_list.append(pi)
    pi=0.0
    inside=0

pi_final = mean(pi_list) 

print(round(pi_final,5))