L=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
v=12
i = 0
while i != len(L) and v != L[i]:
    i = i + 1
    if i == len(L):
        print("Not Exists") 
    else:
        print(i)