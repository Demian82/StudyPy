import math

def compute_distance(x1, y1, x2, y2):
    dstcX = math.fabs(x2-x1)
    dstcY = math.fabs(y2-y1)
    d = math.sqrt(math.pow(dstcX, 2) + math.pow(dstcY, 2))
    print(d)

compute_distance(10, 2, 3, 5)