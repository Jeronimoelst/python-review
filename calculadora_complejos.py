z = 3 + 6j
n = 4 - 5j

print(z / n)
print(n * z)
print (z + n)
print(n - z)
print(type(n))
print(type(z))

assert z + n == 7 + 1j, "error en la suma"

print(n.real)
print(z.real)
print(z.imag)
print(n.imag)
print(z.conjugate)
print(n.conjugate)