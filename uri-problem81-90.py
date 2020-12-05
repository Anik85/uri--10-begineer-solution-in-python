#problem81
'''j=1
sum=0
for i in range(1,40,2):
    sum=sum+(i/j)
    j=j*2
print("%.2f"%sum)
#problem82
X=[]
for i in range(1,11):
    n=int(input())
    X.append(n)
k=0
for j in X:
    if j<=0:
        j=1
        print("X[%d] = %d"%(k,j))
        k=k+1
    else:
        print("X[%d] = %d"%(k,j))
        k = k + 1
#problem83
V=int(input())
j=V
k=0
if V<50:
    for i in range(1,11):
            print("N[%d] = %d"%(k,j))
            j=j*2
            k=k+1
#problem84
list=[]
for i in range(1,101):
    x=float(input())
    list.append(x)
k=0
for j in list:
    if j<=10:
        print("A[%d] = %.1f"%(k,j))
        k=k+1
    else:
        k=k+1
#problem85
list=[]
for i in range(1,21):
    x=int(input())
    list.append(x)
print(list)
k=0
list.reverse()
for j in list:
    print("N[%d] = %d"%(k,j))
    k=k+1
#problem86
T=int(input())
for i in range(1,T+1):
    N=int(input())
    if 0 <= N <= 60:
        first = 0
        second = 1
        fibo=0
        for j in range(0,N+1):
            if j<=1:
                fibo=j
            else:
                fibo=first+second
                first=second
                second=fibo
        print("Fib(%d) = %d"%(N,fibo))
#problem87
T=int(input())
j=0
k=0
if 2 <= T <= 50:
    for i in range(0,20):
        print("N[%d] = %d"%(k,j))
        k=k+1
        j=j+1
        if j==T:
            j=j-j
#problem88
T = int(input())
for i in range(T):
    PA, PB, G1, G2 = input().split()
    PA = int(PA)
    PB = int(PB)
    G1 = float(G1)
    G2 = float(G2)
    a = 0
    while (PA <= PB):
        cpa = int((PA * (G1 / 100)))
        cpb = int((PB * (G2 / 100)))
        a =a+1
        PA =PA+cpa
        PB =PB+cpb
        if (a > 100):
            break
    if (a > 100):
        print("Mais de 1 seculo.")
    else:
        print("%d anos." % a)
#problem89
n = int(input())
lista = list(map(int, input().split()[:n]))
p = 0
m = lista[0]
count = 0
for i in lista:
    if (i < m):
        m = i
        p = count
    count += 1
print("Menor valor: %d" % m)
print("Posicao: %d" % p)
#problem90
n=float(input())
k=0
for i in range(1,101):
    print("N[%d] = %.4f"%(k,n))
    k=k+1
    n=n/2
#problem91
n=int(input())
T=input()
sum=0
count1=0
count2=0
for i in range(2):
    for j in range(2):
        x=float(input())
        if T=='S' and i==n:
            sum=sum+x
            count1=count1+1
        elif T=='M' and i==n:
            sum=sum+x
            count2 = count2 + 1
if count1>0:
    print("%.1f"%sum)
elif count2>0:
    print("%.1f"%sum/4.0)
#problem92
par = []
impar = []
for i in range(15):
    valor = int(input())
    if (valor % 2 == 0):
        par.append(valor)
    else:
        impar.append(valor)

    if (len(par) == 5):
        ix = 0
        for v in par:
            print("par[%d] = %d" % (ix, v))
            ix += 1
        par = []
    if (len(impar) == 5):
        ix = 0
        for v in impar:
            print("impar[%d] = %d" % (ix, v))
            ix += 1
        impar = []
if (len(impar) > 0):
    ix = 0
    for v in impar:
        print("impar[%d] = %d" % (ix, v))
        ix += 1

if (len(par) > 0):
    ix = 0
    for v in par:
        print("par[%d] = %d" % (ix, v))
        ix += 1
#just practice
N=int(input())
if 1<=N<=10000:
    yen=N%1000
    if yen==0:
        print(yen)
        print("We can pay the exact price.")
    else:
        if yen>=500:
            yen1=1000-yen
            print(yen1)
            print("We will use two 1000-yen bills to pay the price and receive %d yen in change."%yen1)
        else:
            print(yen)
            print("We will use two 1000-yen bills to pay the price and receive %d yen in change."%yen)
X=int(input())
if X>=-40 and X<=40:
    if X>=30:
        print("Yes")
    else:
        print("No")
x=input()
x=x.lower()
if len(x)==6:
    if x[2]==x[3] and x[4]==x[5]:
        print("Yes")
    else:
        print("No")
#problem93
x=input()
x=x.lower()
count=0
if len(x)==6:
    for i in range(2,len(x),2):
        for j in range(3,len(x),2):
            if x[i]==x[j]:
                count=count+1
    if count>1:
        print("Yes")
    else:
        print("No")
#problem94
c = int(input())
op = input()
s = 0
for i in range(2):
	for j in range(2):
		v = float(input())
		if (j == c):
			s += v
if(op == 'S'):
	print('%.1f' %s)
else:
	print('%.1f' %(s/12.0))
#problem95
O = input()
sum = 0
for i in range(12):
  for j in range(12):
    x = float(input())
    if j > i:
      sum += x
if O == "S":
  print("%.1f"%(sum))
elif O == "M":
  print("%.1f"%(sum / 66))
#another
N=int(input())
S =input()[:N]
substring = "ABC"
count = S.count(substring)
print("The count is:", count)
#just practice
K,X=map(int,input().split())
if 1<=K<=100 and 1<=X<=pow(10,5):
	if K*500>X:
		print("Yes")
	else:
		print("No")
#problem96
O=input()
sum=0
for i in range(12):
    for j in range(12):
        x=float(input())
        if j<i:
            sum=sum+x
if O=='S':
    print("%.1f"%sum)
elif O=='M':
    print("%.1f"%(sum/66.0))

#practice
def isSymmetric(mat, N):
    for i in range(N):
        for j in range(N):
            if (mat[i][j] != mat[j][i]):
                return False
    return True
mat = [[5, 1, 3], [2, 0, 2], [3, 1, 5]]
if (isSymmetric(mat, 3)):
    print("Yes")
else:
    print("No")
#problem97
O=input()
sum=0
for i in range(12):
    for j in range(12):
        x=float(input())
        if j<=(11-(i+1)):
            sum=sum+x
if O=='S':
    print("%.1f"%sum)
elif O=='M':
    print("%.1f"%(sum/66.0))
#problem98
O=input()
sum=0
for i in range(12):
    for j in range(12):
        x=float(input())
        if j>11-i:
            sum=sum+x
if O=='S':
    print("%.1f"%sum)
elif O=='M':
    print("%.1f"%(sum/66.0))
#problem99
O=input()
sum=0
for i in range(12):
    for j in range(12):
        x=float(input())
        if j>i and j<=(11-(i+1)):
            sum=sum+x
if O=='S':
    print("%.1f"%sum)
elif O=='M':
    print("%.1f"%(sum/30.0))
#problem100
while True:
    try:
        N=int(input())
        if 0<=N<=100:
            if N==0:
                print("vai ter copa!")
            else:
                print("vai ter duas!")
    except EOFError:
        break
#problem101
while True:
    try:
        L=int(input())
        V=input().split(' ')
        m=0
        for i in range(L):
            if int(V[i])>m:
                m=int(V[i])
        if m<10:
            N=1
            print(N)
        elif m>=10 and m<20:
            N=2
            print(N)
        elif m>=20:
            N=3
            print(N)

    except EOFError:
        break
#problem 102
ara=[]
for i in range(3):
    sum=0
    while True:
        ara=input()
        if(ara[0]=='c') :
            break
        if(ara[0]=='-'):
            if(ara[1]=='-'):
                if(ara[2]=='-') :
                    sum+=0
                else:
                    sum+=1
            else:
                if(ara[2]=='-'):
                    sum+=2
                else:
                    sum+=3
        elif(ara[0]=='*'):
            if(ara[1]=='-'):
                if(ara[2]=='-'):
                    sum+=4
                else:
                    sum+=5
            else:
                if(ara[2]=='-'):
                    sum+=6
                else:
                    sum+=7

    print("%d"%sum)

T=int(input())
for i in range(T):
    j1,j2=input().split(' ')
    win=""
    if j1==j2:
        win="De novo!"
    elif j1=="tesoura":
        if j2=="papel" or j2=="lagarto":
            win=j1
        else:
            win=j2
    elif j1=="papel":
        if j2=="pedra" or j2=="Spock":
            win=j1
        else:
            win=j2
    elif j1=="pedra":
        if j2=="lagarto" or j2=="tesoura":
            win=j1
        else:
            win=j2
    elif j1=="lagarto":
        if j2=="Spock" or j2=="papel":
            win=j1
        else:
            win=j2
    elif j1=="Spock":
        if j2=="tesoura" or j2=="pedra":
            win=j1
        else:
            win=j2
    if win == j1:
        win="Bazinga!"
    elif win==j2:
        win="Raj trapaceou!"
    print("Caso #%d:"%(i+1),win)

A,B,C=map(int,input().split(' '))
if A>B and B<=C:
    print(":)")
elif A<B and B>=C:
    print(":(")
elif A<B and B<C and B-A>C-B:
    print(":(")
elif A<B and B<C and C-B>=B-A:
    print(":)")
elif A>B and B>C and A-B>B-C:
    print(":)")
elif A>B and B>C and A-B<=B-C:
    print(":(")
elif A==B and B<C:
    print(":)")
elif A==B and B>C:
    print(":(")
else:
    print(":(")

a, b =list(map(int,input().split(' ')))#[int(x) for x in input().split()]
q=0
for r in range(abs(b)):
    if ((a - r) % b) == 0:
        q = int((a - r)/b)
        break
print(q,r)'''

A,B=map(int,input().split(' '))
arr=[4,7,47,74,44,444,447,474,477,777,774,744]
count=0
for i in range(A,B+1):
    for j in range(len(arr)):
        if i==arr[j] and i%arr[j]==0:
            print(arr[j],end=" ")
            count=count+1
if count==0:
    print("-1")



