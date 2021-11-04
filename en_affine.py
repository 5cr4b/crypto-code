import string

def affine_en(text , key1 ,key2):
    letters = string.ascii_lowercase
    result = ""
    for i in text:
        try:
            j = (letters.index(i)* key1 + key2) % len(letters) 
            result += letters[j]
        except ValueError:
            result += i
    return result

print(affine_en(input("text :" ),int(input("key 1 : ")),int(input("key2 :"))))