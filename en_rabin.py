def  euclid_extend(a,b): #tim nghịch đảo
    x1 , x2 = 0 , 1
    y1 , y2= 1 , 0
    while b != 0 :
        q = a // b 
        r = a % b
        a = b
        b = r 
        x = x2 - x1*q
        x2 ,x1, = x1 , x
        y = y2 - y1*q
        y2 , y1 = y1 , y
    return x2,y2
f = lambda x : [x for x in range]

def rabin(p,q ,m):
    n = p*q
    euclid_inverse =  euclid_extend(p,q)
    a , b  = euclid_inverse[0] , euclid_inverse[1]
    t , u = abs(a), abs(b)
    z = pow(m,2) % n
    r ,  s  = pow(z,u) % p  ,  pow(z,t) % q 
    x1 =  (a*p*s +  b*q*r) % n #nghiệm 1
    x2 = n - x1                #2 
    x3 =  (a*p*s -  b*q*r) % n #3
    x4 = n - x3                 #4
    return x1 , x2 ,x3 ,x4 

print(rabin(int(input('p: ' )),int(input('q : ')),int(input('m : '))))
# convert m ( bản mã) sang hex trước