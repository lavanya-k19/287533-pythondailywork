n=int(input())
s=set()
for i in range(0,n+1):
    s.add(int(input()))
#for i in range(0,n+1):
print("min is",min(s))
print("max is",max(s))