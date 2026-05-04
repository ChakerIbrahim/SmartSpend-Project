
def a():
    return 5
print (a())
# the result is 5

# the result is 10
def a():
    return 5
print(a()+a())

# the result is 5
def a():
    return 5
    return 10
print(a())

# the result is 5
def a():
    return 5
    print(10)
print(a())

# the result is 5 then none
def a():
    print(5)
x = a()
print(x)

# the result is 3 5 then error there is no return
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))

# the result will be 25 string+string
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

# the first result is 100 then 10
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

# 7 then 14 then 21
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

# result is 8
def a(b,c):
    return b+c
    return 10
print(a(3,5))

# 500 then 500 then 300 and then 500
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

# 500 then 500 then 300 then 500
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

# 500 then 500 then 300 then 300
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

# 1 then 3 then 2
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

# 1 then 3 then 5 then 10 
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
