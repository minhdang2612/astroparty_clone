import math
def AngleMovement(angle, speed):
    radian_angle = math.radians(angle)
    dx = abs(round((math.cos(radian_angle))*speed , 0))
    dy = abs(round((math.sin(radian_angle))*speed , 0))
    if angle >= 0 and angle < 90:
        dy = -abs(dy)
    elif angle >= 90 and angle < 180:
        dx = -abs(dx)
        dy = -abs(dy)
    elif angle >= 180 and angle < 270:
        dx = -abs(dx)
    else:
        dx = abs(dx)
        dy = abs(dy)
    return dx, dy