import math
def euclid_extend(a , b ):
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
    return x2

def euler(n):
    result = []
    for i in range(1,n):
        if math.gcd(i,n) == 1:
            result.append(i)
    return result


def log_tren_z(a,b,n):
    euler1 = euler(n)
    level_euler  = len(euler1)

    m = math.ceil(math.sqrt(level_euler))        #m
    j1 = [(pow(a,x) % 61)  for x in range(m)]    
    a_inverse = euclid_extend(a,n)              
    a_inverse_multi_m =  pow(a_inverse, m) % n
    i1 = [b*pow(a_inverse_multi_m, x) % n for x in range(m)]
    for i in j1:
        for j in i1:
            if i == j:
                j2 = j1.index(j)
                i2 = i1.index(i)
                print(j1)
                print(i1)
                print('m = ',m)
                return (m * i2 + j2) 

print(log_tren_z(int(input("a : ")),int(input('b : ')),int(input('n : '))))