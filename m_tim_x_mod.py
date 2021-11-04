def brute_force_inverse(n1,n2,mod):
    for i in range(0,10000):
        if  (n2  % mod == n1 * i % mod):
            return i

print(brute_force_inverse(11,10,13))