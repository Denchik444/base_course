import math
h = 100
α = 45
β = 35
g = 9.8

SPEED = ((g*h * (math.tan(β) ** 2)) / (2 * (math.tan(α) ** 2) * (1 - math.tan(β) * math.tan(α))) ** 0.5) 
print(SPEED)