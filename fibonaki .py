pos=int(input())
if (pos==0 or pos ==1):
    print(pos)
else:
    a=0
    b=1
    i=2
    while (i <=pos):
        c=a+b
        a=b
        b=c
        i+=1
    print(c)

