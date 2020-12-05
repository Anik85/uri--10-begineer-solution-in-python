#problem61
for i in range(1,100000000):
    X=int(input())
    if X==2002:
        print("Acesso Permitido")
        break
    else:
        print("Senha Invalida")
#problem62
for i in range(1,10000000):
    X,Y=map(int,input().split(' '))
    if X>0 and Y>0:
        print("primeiro")
    elif X>0  and Y<0:
        print("quarto")
    elif X<0 and Y<0:
        print("terceiro")
    elif X<0 and Y>0:
        print("segundo")
    elif X==0 or Y==0:
        break
#problem63
N=int(input())
for i in range(1,N+1):
    X,Y=map(int,input().split(' '))
    if X >=0 and Y<0:
        val=X/Y
        print("%.1f"%val)
    elif X>=0 and Y>0:
        val = X / Y
        print("%.1f"%val)
    elif X<=0 and Y>0:
        val = X / Y
        print("%.1f"%val)
    elif X<=0 and Y<0:
        val = X / Y
        print("%.1f"%val)
    elif X==0 and Y==0:
        val = X / Y
        print("%.1f"%val)
    elif X>0 and Y==0:
        print("divisao impossivel")
    elif X<0 and Y==0:
        print("divisao impossivel")
#problem64
for i in range(1,100):
    x=float(input())
    count = 0
    if x>0.0 and x<=10.0:
        for j in range(1,100):
            y = float(input())
            if y>0.0 and y<=10.0:
                media=(x+y)/2
                print("media = %.2f"%media)
                count=count+1
                break
            else:
                print("nota invalida")
    else:
        print("nota invalida")
    if count>0:
        break

#problem64
for i in range(1,100):
    x=float(input())
    count = 0
    if x>0.0 and x<=10.0:
        for j in range(1,100):
            y = float(input())
            count1 = 0
            if y>0.0 and y<=10.0:
                media=(x+y)/2
                print("media = %.2f"%media)
                for k in range(1,10):
                    print("novo calculo (1-sim 2-nao)")
                    X=int(input())

                    if X < 1 or X > 2:
                        pass
                    elif X==1:
                        count1=count1+1
                        break
                    elif X==2:
                        count=count+1
                        break
            else:
                print("nota invalida")

            if count1>0:
                break
            elif count>0:
                break
    else:
        print("nota invalida")
    if count>0:
        break
#problem65
count1=0
count =0
count2=0
count3=0
for i in range(1,10):
    print("Novo grenal (1-sim 2-nao)")
    x,y=map(int,input().split(' '))
    if x>y:
        count1=count1+1
    elif x<y:
        count2=count2+1
    elif x==y:
        count3=count3+1
    count=count1+count2+count3

    if count1>0:

        w=int(input())
        if w==1:
            pass
        elif w==2:
            break
    elif count2>0:

        w = int(input())
        if w==1:
            pass
        elif w==2:
            break
    elif count3>0:

        w = int(input())
        if w==1:
            pass
        elif w==2:
            break
print("%d grenais"%count)
print("Inter:%d"%count1)
print("Gremio:%d"%count2)
print("Empates:%d"%count3)

if count1>count2:
    print("Inter venceu mais")
elif count1<count2:
    print("Gremio venceu mais")
elif count1==count2:
    print("Não houve vencedor")

#another
count =0
count1=0
count2=0
count3=0
for i in range(1,10000000000):
    print("Novo grenal (1-sim 2-nao)")
    x,y=map(int,input().split(' '))
    if x>y:
        count1=count1+1
        w = int(input())
        if w == 1:
            pass
        elif w == 2:
            break
    elif x<y:
        count2=count2+1
        w = int(input())
        if w == 1:
            pass
        elif w == 2:
            break
    elif x==y:
        count3=count3+1
        w = int(input())
        if w == 1:
            pass
        elif w == 2:
            break
count=count+count1+count2+count3
print("%d grenais"%count)
print("Inter:%d"%count1)
print("Gremio:%d"%count2)
print("Empates:%d"%count3)

if count1>count2:
    print("Inter venceu mais")
elif count1<count2:
    print("Gremio venceu mais")
elif count1==count2:
    print("Não houve vencedor")
#problem66
X=int(input())
Y=int(input())
if X>Y:
    max=X
    min=Y
else:
    max=Y
    min=X
for i in range(min+1,max):
    if i%5==2 or i%5==3:
        print(i)
#problem67
X=int(input())
Y=int(input())
sum=0
if X>Y:
    max=X
    min=Y
else:
    max=Y
    min=X
for i in range(min,max+1):
    if i%13!=0:
        sum=sum+i
print(sum)
#problem68
count=0
count1=0
count2=0
for i in range(1,100):
    x=int(input())
    if x>=1 and x<=4:
        if x==1:
            count=count+1
        elif x==2:
            count1 = count1 + 1
        elif x==3:
            count2 = count2 + 1
        elif x==4:
            break
    else:
        pass
print("MUITO OBRIGADO")
print("Alcool:",count)
print("Gasolina:",count1)
print("Diesel:",count2)
#problem69
N=int(input())
i=1
for i in range(i,4*N,4):
        print(i, end=" ")
        print(i + 1, end=" ")
        print(i + 2, end=" ")
        print("PUM")
#problem70
N=int(input())
if 1 < N < 1000:
    for i in range(1,N+1):
        print(i,end=" ")
        print(i*i,end=" ")
        print(i*i*i)











