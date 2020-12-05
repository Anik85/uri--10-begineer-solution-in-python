#problem21
A=float(input())
N=A
print("NOTAS:")
print("%d nota(s) de R$ 100.00"%(N/100))
b=N%100
print("%d nota(s) de R$ 50.00"%(b/50))
d=b%50
print("%d nota(s) de R$ 20.00"%(d/20))
f=d%20
print("%d nota(s) de R$ 10.00"%(f/10))
h=f%10
print("%d nota(s) de R$ 5.00"%(h/5))
j=h%5
print("%d nota(s) de R$ 2.00"%(j/2))
l=j%2
print("MOEDAS:")
E=A*100
B=(int(E))
print("%d moeda(s) de R$ 1.00"%l)
m=B%100
print("%d moeda(s) de R$ 0.50"%(m/50))
o=m%50
print("%d moeda(s) de R$ 0.25"%(o/25))
q=o%25
print("%d moeda(s) de R$ 0.10"%(q/10))
s=q%10
print("%d moeda(s) de R$ 0.05"%(s/5))
u=s%5
print("%d moeda(s) de R$ 0.01"%u)
#problem22
A,B,C,D=map(int,input().split())
if B>C and D>A and (C+D)>(A+B) and C>=0 and D>=0 and A%2==0:
                print("Valores aceitos")
else:
    print("Valores nao aceitos")
# problem23
A,B,C =map(float,input().split())
d = B * B - 4 * A * C
e = pow(d,0.5)
if (d < 0 or A == 0):
    print("Impossivel calcular")
else:
    f = (-B + e) / (2 * A)
    g = (-B - e) / (2 * A)
    print("R1 = %.5f"%f)
    print("R2 = %.5f"%g)
# problem24
n=float(input())
if n<0.00 or n>100.00:
    print("Fora de intervalo")
elif n>=0.00 and n<=25.00:
    print("Intervalo [0,25]")
elif n>25.00 and n<=50.00:
    print("Intervalo (25,50]")
elif n>50.00 and n<=75.00:
    print("Intervalo (50,75]")
elif n>75.00 and n<=100.00:
    print("Intervalo (75,100]")
#problem24
snack={
    1:4.00,
    2:4.50,
    3:5.00,
    4:2.00,
    5:1.50
}
X,Y=map(int,input().split())
Total=snack[X]*Y
print("Total: R$ %.2f"%Total)
# problem25
N1,N2,N3,N4=map(float,input().split())
Media=((N1*2)+(N2*3)+(N3*4)+(N4*1))/10
print("Media: %.1f"%Media)
if Media>=7.0:
    print("Aluno aprovado.")
elif Media<5.0:
    print("Aluno reprovado.")
elif Media >=5.0 and Media<=6.9:
    print("Aluno em exame.")
    N5=float(input())
    print("Nota do exame:",N5)
    Media2=(N5+Media)/2
    if Media2>=5.0:
        print("Aluno aprovado.")
        print("Media final: %.1f"%Media2)
    elif Media2<=4.9:
        print("Aluno reprovado.")
        print("Media final: %.1f" % Media2)
# problem26
X,Y=map(float,input().split())
if(X==0 and Y==0):
    print("Origem")
elif(X==0):
    print("Eixo Y")
elif(Y==0):
    print("Eixo X")
elif(X>0 and Y>0):
    print("Q1")
elif(X<0 and Y>0):
    print("Q2")
elif(X<0 and Y<0):
    print("Q3")
elif(X>0 and Y<0):
    print("Q4")
# problem27
A,B,C=map(int,input().split())
list=[A,B,C]
list.sort()
for x in list:
    print(x)
print()
print(A)
print(B)
print(C)
#another
a,b,c=map(float,input().split())
if(a < b):
    temp = a
    a = b
    b = temp
if(b < c):
    temp = b
    b = c
    c = temp
if(a < b):
    temp = a
    a = b
    b = temp
print(a)
print(b)
print(c)

#problem28
A,B,C=map(float,input().split())
if (B+C)>A and (A+B)>C and (A+C)>B:
    Perimetro=A+B+C
    print("Perimetro = %.1f"%Perimetro)
else:
    Area=((1/2)*(A+B))*C
    print("Area = %.1f"%Area)
#problem29
A,B=map(int,input().split())
if A%B==0 or B%A==0:
    print("Sao Multiplos")
else:
    print("Nao Sao Multiplos")
#problem30
A,B,C=map(float,input().split())
list=[A,B,C]
list.sort(reverse=True)
print(list)
A=list[0]
B=list[1]
C=list[2]
if (A >= B + C):
    print("NAO FORMA TRIANGULO")
elif ((A*A)==((B*B) + (C*C))):
    print("TRIANGULO RETANGULO")
elif ((A*A)>((B*B) + (C*C))):
    print("TRIANGULO OBTUSANGULO")
elif ((A*A)<((B*B) + (C*C))):
    print("TRIANGULO ACUTANGULO")
if (A==B==C):
    print("TRIANGULO EQUILATERO")
elif (A==B or A==C or B==C):
    print("TRIANGULO ISOSCELES")