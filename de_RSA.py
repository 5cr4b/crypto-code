
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
    result = 1
    for i in range(2,n):
        if math.gcd(i,n) == 1:
            result += 1 
    return result

def de_rsa(p ,  q , d , c):
    n = p *q
    level_euler_q = euler(q)
    level_euler_p = euler(p) 
    level_n =level_euler_p * level_euler_q
    print(level_n)
    if math.gcd(level_n , d) == 1:
        e = euclid_extend(d, level_n) % level_n # mu~ ma~ hoa'
        m =  pow(c,d) % n
    print('mu~ ma~ hoa\' e : ',  e)
    print('ban? tin da~ ma~ hoa\': ',m)

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
    result = 1
    for i in range(2,n):
        if math.gcd(i,n) == 1:
            result += 1 
    return result

def de_rsa(p ,  q , d , c):
    n = p *q
    level_euler_q = euler(q)
    level_euler_p = euler(p) 
    level_n =level_euler_p * level_euler_q
    print(level_n)
    if math.gcd(level_n , d) == 1:
        e = euclid_extend(d, level_n) % level_n # mu~ ma~ hoa'
        m =  pow(c,d) % n
    print('mu~ ma~ hoa\' e : ',  e)
    print('ban? tin da~ ma~ hoa\': ',m)

de_rsa(int(input('nhap p: ')),int(input('nhap q: ' )),int(input('nhap d(mu~ ma~ hoa): ')),int(input('nhap c (ciphertext) : ')))