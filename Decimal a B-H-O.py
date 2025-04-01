n = int(input("Ingresa un número decimal: "))

b = []
h = []
o = []

num = n 
while num > 0:
    b.append(num % 2)
    num //= 2 
if not b:
    b.append(0) 
b.reverse()

num = n 
hex_dicc = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f'] 
while num > 0:
    h.append(hex_dicc[num % 16]) 
    num //= 16 
if not h:
    h.append(0) 
h.reverse()

num = n 
while num > 0:
    o.append(num % 8)
    num //= 8 
if not o:
    o.append(0)
o.reverse()

binario = "".join(str(d) for d in b) 
hexadecimal = "".join(str(d) for d in h) 
octal = "".join(str(d) for d in o)

print("Binario:", binario) 
print("Hexadecimal:", hexadecimal)
print("Octal:", octal)
