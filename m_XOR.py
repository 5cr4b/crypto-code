def xOR(text , key):
    result = []
    for i in range(len(text)):
        print(ord(text[i]) , ord(key[i]))
        j = ord(text[i]) ^ ord(key[i])
        result.append(j)
    return result ,
print(xOR(input("plain text : " ) , input("key  : ")))