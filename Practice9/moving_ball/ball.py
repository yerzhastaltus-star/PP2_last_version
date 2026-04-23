def x_move(x, width, radius, speed, side):
    if side == "right":
        if x+radius > width:
            x = width - radius
            return x
        return x
    else:
        if x-radius < 0:
            x = 0 + radius
            return x
        return x

def y_move(y, height, radius, speed, side):
    if side == "up":
        if y-radius < 0:
            y = 0 + radius
            return y
        return y
    else:
        if y+radius > height:
            y = height - radius
            return y
        return y
        