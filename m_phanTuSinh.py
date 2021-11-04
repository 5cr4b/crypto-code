def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

def euler(n):
    result = []
    for i in range(1,n):
        if gcd(i,n) == 1:
            result.append(i)
    return result,len(result)

def level_euler(n):
    level = []
    for  i in euler(n):
        for j in range(1,1000):
            pow1 = pow(i,j)
            if pow1 % n == 1:
                level.append(j)
            break
    return level

def PTTSNT(n):
    coso = []
    count = 0 
    i = 2
    while n > 1:
        while n % i == 0 :
            n = n / i
            count += 1 
        if count >= 1 :
            count = 0
            coso.append(i)
        i += 1  
    return coso    

def phanTuSinh(n):
    result = []
    euler1 = euler(n)
    coso = PTTSNT(euler1[1])
    for i in euler1[0]:
        storage = []
        for j in coso:
            t = int(euler1[1] / j)
            x = (i**t) % n
            storage.append(x)
        if 1 not in storage:
            result.append(i)
    return len(result)

print(phanTuSinh(int(input("n : "))))

