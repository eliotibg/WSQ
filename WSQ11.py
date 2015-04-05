def inverse(x):
    x=str(x)
    x=x[::-1]
    x=int(x)
    return x
n=[]
l=[]
x=int(input("Dame el numero menor de la serie: "))
x1=int(input("dae ele numero mayor de l seri: "))

for i in range(x1-x+1):
    n.append(x)
    x=x+1
r1=0
r2=0
r3=0
for i in n:
    y=inverse(i)
    if i==y:
        r1=r1+1
    else:
        z=i+y
        y1=inverse(z)
        for i1 in range(30):
            if z==y1:
                r2=r2+1
                break
            else:
                z=z+y1
                y1=inverse(z)
                if i1==29:
                    r3=r3+1
                    lychrel.append(i)
print("natural palindroms: ",r1)
print("non-lychrel: ",r2)
print("numero candidatos: ",r3)