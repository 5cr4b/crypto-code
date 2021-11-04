f =  lambda a,p,private_key : pow(a,private_key) % p 

a = int(input('a :'))
p = int(input('p or z :'))
private_key = int(input('private key : '))

print('khoa cong khai : ',p,a,f(a,p,private_key))

print('decrypt elgamal')



t = lambda a,k,p: pow(a,k) % p 
u = lambda x,p,a,private_key,k : x*pow(f(a,p,private_key),k) % p

k =  int(input('k : '))
x = int(input('x: '))
print('ban ma~ : ' ,t(a,k,p), u(x,p,a,private_key,k))


