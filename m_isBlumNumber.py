def isBlumInteger(n):
 
    prime = [True]*(n + 1)

    i = 2
    while (i * i <= n):
        if (prime[i] == True) :
            for j in range(i * 2, n + 1, i):
                prime[j] = False
        i = i + 1

    for i in range(2, n + 1) :
        if (prime[i]) :

            if ((n % i == 0) and
                        ((i - 3) % 4) == 0):
                q = int(n / i)
                return (q != i and prime[q]
                       and (q - 3) % 4 == 0)
             
    return False
 
n = int(input('n : '))
if (isBlumInteger(n)):
    print("Yes")
else:
    print("No")