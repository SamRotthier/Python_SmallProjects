import math

print(6 * 7)  # eenvoudige vermenigvuldiging
print(2 ** 3)  # machtsverheffing
print((2 + 4) * (9 - 2))  # haakjes
print(60 * math.sin(math.pi / 4))  # # goniometrische functies (radialen)

a = 3 * 14
print(a)
print(a * 7 + 3)
a = "bla"
print(a)
a = 'bla'
print(a)
a = 42.5
print(a)
a = True
print(a)

var = 'Python', 
print(type(var)) #<class 'tuple'>

a = [1, 2, 3] 
b = [1, 2, 3] 
print(a is b) #"a is b" will return False because they are not the same object.

var = 3 * ['a']
print(var)

print(10 // 3) #Floor devision

for i in range(100): #Every time we loop through "range(100)", we assign a value to "i". This assignment persists even after the loop has terminated. 99 was the last value assigned, so that's new value of "i".
    pass 
print(i)