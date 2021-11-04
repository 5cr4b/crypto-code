def euclid(a , b ):
    x1, x2 = 0, 1 
    y1, y2 = 1, 0 
    while b != 0:
        q = a // b
        r = a % b 
        x = x2 - x1*q
        y = y2 - y1*q
        a = b 
        b = r 
        x2, y2 = x1, y1
        x1, y1 = x, y 
    return x2,y2
print(euclid(int(input("a = ")), int(input("b = "))))