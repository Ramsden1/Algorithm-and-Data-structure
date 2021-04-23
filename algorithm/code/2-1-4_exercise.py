def sum(a, b):
    c = ['']*(len(a)+1)
    carry = 0
    for i in range(len(a)-1, -1, -1):
        c[i+1] = (a[i] + b[i] + carry) % 2
        carry = (a[i] + b[i] + carry) // 2
    c[0] = carry
    return c

a = [1,0,1,0,1]
b = [1,1,0,1,1]
c = sum(a, b)
print(a)
print(b)
print(c)
