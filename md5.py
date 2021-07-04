import hashlib
str = input('Enter string: ')
obj = hashlib.md5(str.encode())
print("md5 = "+obj.hexdigest())

