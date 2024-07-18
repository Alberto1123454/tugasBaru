#Operasi Bitwise

#Operasi OR

a = 10
b = 20

c = a | b

#Bitwise OR
print("\n=============OR============")
print("nilai a, maka: ", a, "binary: ", format(a, '08b'))
print("nilai b, maka: ", b, "binary: ", format(b, '08b'))
print("-----------------------------------------------------(|)")
print("nilai c, maka: ", c, "binary: ", format(c, '08b'))

c = a & b

print("\n=============AND============")
print("nilai a, maka: ", a, "binary: ", format(a, '08b'))
print("nilai b, maka: ", b, "binary: ", format(b, '08b'))
print("-----------------------------------------------------(&)")
print("nilai c, maka: ", c, "binary: ", format(c, '08b'))

c = a^b

print("\n=============XOR============")
print("nilai a, maka: ", a, "binary: ", format(a, '08b'))
print("nilai b, maka: ", b, "binary: ", format(b, '08b'))
print("-----------------------------------------------------(^)")
print("nilai c, maka: ", c, "binary: ", format(c, '08b'))