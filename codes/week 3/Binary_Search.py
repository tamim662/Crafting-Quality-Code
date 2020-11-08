L=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
v=12
b = 0
e = len(L) - 1
while b <= e:
    
    m = (b + e) // 2
    if L[m] < v:
        b = m + 1
    else:
        e = m - 1
if b == len(L) or L[b] != v:
    print("nai")

else:
    print(b)