#problem41
count=0
sum=0
for i in range(1,7):
    x=float(input())
    if x>0:
        count=count+1
        sum = sum + x
print("%d valores positivos"%count)
print("%.1f"%(sum/count))
#problem42
count=0
for i in range(1,6):
    x=int(input())
    if x%2==0:
        count=count+1
print("%d valores positivos"%count)
#problem43
count1=0
count2=0
count3=0
count4=0
for i in range(1,6):
    x=int(input())
    if x%2==0:
        count1=count1+1
    else:
        count2 = count2 + 1
    if x > 0:
        count3 = count3 + 1
    elif x<0:
        count4 = count4 + 1
print("%d valor(es) par(es)"%count1)
print("%d valor(es) impar(es)"%count2)
print("%d valor(es) positivo(s)"%count3)
print("%d valor(es) negativo(s)"%count4)
#problem44
X=int(input())
for i in range(1,X+1):
    if i%2!=0:
        print(i)
#problem45
X=int(input())
for i in range(X,X+12):
    if i%2!=0:
        print(i)
#problem46
N=int(input())
count=0
count1=0
for i in range(N):
    X=int(input())
    if X>=10 and X<=20:
        count=count+1
    else:
        count1=count1+1
print("%d in"%count)
print("%d out"%count1)
#problem47
X=int(input())
Y=int(input())
sum=0
if X<Y:
    min=X
    max=Y
else:
    min=Y
    max=X
for i in range(min+1,max):
    if i%2!=0:
        sum=sum+i
print(sum)
#problem48
N=int(input())
for i in range(0,10000):
    if i%N==0:
        sum=i+2
        print(sum)
#problem49
j=0
loc=0
for i in range(100):
    n=int(input())
    if(n>j):
        j=n
        loc=i
print(j)
print(loc+1)
#problem50
N=int(input())
if N>5 and N<2000:
    for i in range(1,N+1):
        if i%2==0:
            print("%d^2 = %d"%(i,i*i))


