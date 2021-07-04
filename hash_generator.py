import hashlib
str = input('Enter string: ')
x = hashlib.md5(str.encode())
print("md5 = ", x.hexdigest())

y = hashlib.sha256(str.encode())
print("sha256 = ", y.hexdigest())

z = hashlib.blake2b(str.encode())
print("blake2b = ", z.hexdigest())