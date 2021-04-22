n=int(input())
a=[]
for i in range(0,n+1):
    a.append(int(input()))
for i in range(0,n+1):
    for j in range(i+1,n+1):
        if(a[i]>a[j]):
            t=a[i]
            a[i]=a[j]
            a[j]=t
        print(a[1])
        break