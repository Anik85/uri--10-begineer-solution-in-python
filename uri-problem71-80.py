#problem71
n=int(input())
for num in range(1, n+1):
    #print(num, num**2, num**3)
    #print(num, num**2+1,num**3+1)
    print(num,num**2,num**3)

#problem72
for i in range(1,10):
    X=int(input())
    if X==0:
        break
    else:
        for j in range(1,X):
            print(j,end=" ")
            if j==(X-1):
                print(X)
#another
while(True):
    a=int(input())
    r=''
    if(a==0):
        break
    for i in range(1,a+1):
        r += str(i) + " "
    print(r[:-1])
#problem73
X,Y=map(int,input().split(' '))
count=0
if X<Y and 1 < X < 20 and X < Y < 100000:
    for i in range(1,Y+1):
        print(i,end=" ")
        count = count + 1
        if count == X:
            print()
            count=count-count
#another
n1,n2 = list(map(int,input().split()))
cont = 1
for i in range(1,(int((n2/n1))+1)):
    r = ""
    for y in range(n1):
        r += str(cont) + " "
        cont += 1
    print(r[:-1])
#problem74
N=int(input())
first=0
second=1
count=0
if 0 < N < 46:
    for i in range(0,N-1):
        if i<=1:
            fibo=i
        else:
            fibo=first+second
            first=second
            second=fibo
        print(fibo,end=" ")
        count=count+1
        if count==N-1:
            print(first+second)
#problem75
N=int(input())
fact=1
if 0 < N < 13:
    for i in range(1,N+1):
        fact=fact*i
    print(fact)
#problem76
sum=0
count=0
for i in range(1,1000000000):
    x=int(input())
    if x<0:
        break
    else:
        sum=sum+x
        count=count+1
print("%.2f"%(sum/count))
#problem77
S=0
for i in range(1,101):
    S=S+1/i
print("%.2f"%S)
#just practice
x,y=map(int,input().split())
result=(y/x)*100
if result<70:
    print("%.2f"%result+"%, Not Allowded")
else:
    print("%.2f"%result+"%, Allowed")
#problem78
sum=0
for i in range(1,10):
    x=int(input())
    if x==0:
        break
    else:
        for j in range(x,x+10):
            if j%2==0:
                sum=sum+j
    print(sum)
    sum=sum-sum
#problem79
N=int(input())
for i in range(1,N+1):
    X=int(input())
    count = 0
    for j in range(2,X):
        if X%j==0:
            count=count+1
    if count==0:
        print("%d eh primo"%X)
    else:
        print("%d nao eh primo"%X)
#problem80
N=int(input())
for i in range(1,N+1):
    X=int(input())
    sum = 0
    for j in range(1,X):
        if X%j==0:
            sum=sum+j
    if sum==X:
        print("%d eh perfeito"%X)
    else:
        print("%d nao eh perfeito"%X)















