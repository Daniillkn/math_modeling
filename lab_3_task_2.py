import numpy as np
import math
h = 100
a = math.pi/3
B = 30
from lab_3_task_1 import g as g
v1 = g*h * np.tan(B)**2
v2 = 2 * np.cos(a)**2 * (1 - np.tan(B) * np.tan(a))
v3 = v1/v2
v = v3 ** (1/2)
print(v)