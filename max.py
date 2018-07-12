a=input()
a=a.split()
print(a)
b=[int(a[x]) for x in range(len(a))]
print(max(b))
