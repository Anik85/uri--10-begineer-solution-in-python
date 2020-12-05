#problem51
N=int(input())
for i in range(1,N+1):
    X=int(input())
    if X>0 and X%2==0:
        print("EVEN POSITIVE")
    elif X>0 and X%2!=0:
        print("ODD POSITIVE")
    elif X<0 and X%2==0:
        print("EVEN NEGATIVE")
    elif X<0 and X%2!=0:
        print("ODD NEGATIVE")
    elif X==0:
        print("NULL")
#problem52
N=int(input())
sum1=0
sum2=0
sum3=0
for i in range(1,N+1):
    A=input().split()
    val=int(A[0])
    if val>=1 and val<=15:
        if A[1]=='C':
            sum1=sum1+val
        elif A[1]=='R':
            sum2=sum2+val
        elif A[1]=='S':
            sum3=sum3+val
sum=sum1+sum2+sum3
print("Total: %d cobaias"%sum)
print("Total de coelhos: %d"%sum1)
print("Total de ratos: %d"%sum2)
print("Total de sapos: %d"%sum3)
print("Percentual de coelhos: %.2f"%((sum1*100)/sum),"%")
print("Percentual de ratos: %.2f"%((sum2*100)/sum),"%")
print("Percentual de sapos: %.2f"%((sum3*100)/sum),"%")
#problem53
N=int(input())
for i in range(1,11):
    print("%d x %d = %d"%(i,N,N*i))
#problem54
N=int(input())
for i in range(1,N+1):
    A,B,C=map(float,input().split())
    val=((A*2)+(B*3)+(C*5))/10
    print("%.1f"%val)
#problem55
i=1
j=60
while j!=-5:
    print("I=%d J=%d"%(i,j))
    i=i+3
    j=j-5
#problem56
j=7
k=6
l=5
for i in range(1,10,2):
    print("I=%d J=%d"%(i,j))
    print("I=%d J=%d"%(i,k))
    print("I=%d J=%d"%(i,l))
#problem57
j=7
k=6
l=5
for i in range(1,10,2):
    print("I=%d J=%d"%(i,j))
    print("I=%d J=%d"%(i,k))
    print("I=%d J=%d"%(i,l))
    j=j+2
    k=k+2
    l=l+2
#problem58
N=int(input())
for i in range(1,N+1):
  sum=0
  X,Y=map(int,input().split(" "))
  if X>Y:
    max=X
    min=Y
    for j in range(min+1,max):
      if j%2!=0:
        sum=sum+j
    print(sum)
  else:
    max = Y
    min = X
    for j in range(min+1, max):
      if j % 2 != 0:
        sum = sum + j
    print(sum)
#problem59
for i in range(1,4):
  sum = 0
  M,N=map(int,input().split(' '))
  if M>N:
    max=M
    min=N
    if max <= 0 or min <= 0:
      break
    else:
      for j in range(min, max + 1):
        sum = sum + j
        print(j, end=" ")
      print("Sum=%d" % sum)

  else:
    max = N
    min = M
    if max <= 0 or min <= 0:
      break
    else:
      for j in range(min, max + 1):
        sum = sum + j
        print(j, end=" ")
      print("Sum=%d" % sum)
#problem60
for i in range(1,100000000):
    X,Y=map(int,input().split(' '))
    if X<Y:
        print("Crescente")
    elif X>Y:
        print("Decrescente")
    elif X==Y:
        break


















