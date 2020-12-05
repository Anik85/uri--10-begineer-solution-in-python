#problem11
R=float(input())
pi=3.14159
VOLUME=(4.0/3)*pi*R*R*R
print("VOLUME = %.3f"%VOLUME)
#problem12
A,B,C=map(float,input().split())
pi = 3.14159
TRIANGULO=0.5*A*C
CIRCULO=pi*C*C
TRAPEZIO=((1*(A+B))/2)*C
QUADRADO=B*B
RETANGULO=A*B
print("TRIANGULO: %.3f"%TRIANGULO)

print("CIRCULO: %.3f"%CIRCULO)

print("TRAPEZIO: %.3f"%TRAPEZIO)

print("QUADRADO: %.3f"%QUADRADO)

print("RETANGULO: %.3f"%RETANGULO)
#problem13
a,b,c=map(int,input().split())
MaiorAB=(a+b+abs(a-b))/2
MaiorABC=(MaiorAB+c+abs(MaiorAB-c))/2
print("%d eh o maior"%MaiorABC)
#problem14
X=int(input())
Y=float(input())
print("%.3f km/l"%(X/Y))
#problem15
from math import  *
x1,y1=map(float,input().split())
x2,y2=map(float,input().split())
Distance=sqrt(pow(x2-x1,2)+pow(y2-y1,2))
print("%.4f"%Distance)
#problem16
Y=int(input())
distance=Y*2
print("%d minutos"%distance)
#problem17
x=int(input())
y=int(input())
val=(x*y)/12
print("%.3f"%val)
#problem18
notes = int(input())
print(notes)
print("%d nota(s) de R$ 100,00"%(notes/100))
aux = (notes%100)
print("%d nota(s) de R$ 50,00"%(aux/50))
aux = (aux%50)
print("%d nota(s) de R$ 20,00"%(aux/20))
aux = (aux%20)
print("%d nota(s) de R$ 10,00"%(aux/10))
aux = (aux%10)
print("%d nota(s) de R$ 5,00"%(aux/5))
aux = (aux%5)
print("%d nota(s) de R$ 2,00"%(aux/2))
aux = (aux%2)
print("%d nota(s) de R$ 1,00"%(aux/1))
#problem19
N=int(input())
print("%d ano(s)"%(N/365))
rem=N%365
print("%d mes(es)"%(rem/30))
rem=rem%30
print("%d dia(s)"%(rem/1))
#problem20
N=int(input())
print("%d:"%(N/3600),end="")
rem=N%3600
print("%d:"%(rem/60),end="")
rem=rem%60
print("%d"%(rem/1))
