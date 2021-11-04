

f = lambda a,z : set(pow(a,x,z) for x in range(z) if x % 2 != 0)
print('bat thang du bac 2 :',f(int(input('a :')),int(input('z :'))))