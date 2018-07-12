a=input()
a=a.split()
b=[int(a[x]) for x in range(len(a))]
print(max(b))
