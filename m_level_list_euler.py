def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

def euler(n):
    result = []
    for i in range(1,n):
        if gcd(i,n) == 1:
            result.append(i)
    return result


def level(n):
    level = []
    for  i in euler(n):
        for j in range(1,1000):
            pow1 = pow(i,j)
            if pow1 % n == 1:
                level.append(j)
                break
    return level
n  = int(input("nhap n"))
print(euler(n))
print(level(n))
print("level euler : " , len(level(n)))
