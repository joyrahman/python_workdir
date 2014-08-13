def fnc(x, y, z=0):
    x = x * x
    y = y * y
    z = z * z
    return x, y, z


a, b, c = fnc(10, 2, 4)
print (a, b, c)
