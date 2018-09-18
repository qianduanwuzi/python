def my_abs(x):
    if(x>0):
        return x
    else:
        return -x

print(my_abs(-5))

import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

print(move(100, 100, 60, math.pi / 6))
# (151.96152422706632, 70.0) 返回值是一个tuple

# practice 
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax2 + bx + c = 0
# 的两个解。


