def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return (s[0] == 4 and s[1] == 4)

def successors(s):
    x, y, z = s
    if x > 0:
        ty = 5-y
        tz = 3-z
        if y < 5: ## x to y
            if x > ty:
                yield ((x-ty, 5, z), ty)
            else:
                yield ((0, y+x, z), x)
        if z < 3: ## x to z
            if x > tz:
                yield ((x-tz, y, 3), tz)
            else:
                yield ((0, y, z+x), x)
    if y > 0:
        tz = 3-z
        yield ((x+y, 0, z), y) ## y to x
        if z < 3: ## y to z
            if y > tz:
                yield ((x, y-tz, 3), tz)
            else:
                yield ((x, 0, z+y), y)
    if z > 0:
        ty = 5-y
        yield ((x+z, y, 0), z) ## z to x
        if z < 3: ## z to y
            if z > ty:
                yield ((x, 5, z-ty), ty)
            else:
                yield ((x, y+z, 0), z)