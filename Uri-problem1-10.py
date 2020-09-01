#problem1
A=int(input())
B=int(input())
X=A+B
print("X =",X)
#problem1
R=float(input())
pi=3.1416
A=pi*R*R
print("A=%.2f"%A)
#problem1
A=int(input())
B=int(input())
SOMA=A+B
print("SOMA =",SOMA)
#problem1
A=int(input())
B=int(input())
PROD=A*B
print("PROD =",PROD)
#problem1
A=float(input())
B=float(input())
MEDIA=(A*3.5+B*7.5)/(3.5+7.5)
print("MEDIA = %.5f"%MEDIA)
#problem6
A=float(input())
B=float(input())
C=float(input())
MEDIA=(A*2+B*3+C*5)/(2+3+5)
print("MEDIA = %.1f"%MEDIA)
#problem7
A=int(input())
B=int(input())
C=int(input())
D=int(input())
DIFERENCA=(A*B)-(C*D)
print("DIFERENCA =",DIFERENCA)
#problem8
A=int(input())
B=int(input())
C=float(input())
print("NUMBER =",A)
print("SALARY ="+" U$ %.2f"%(B*C))
#problem9
name=input()
fixedsalary=float(input())
totalvalue=float(input())
totalincome=(15*totalvalue)/100
total=totalincome+fixedsalary
print("TOTAL = R$ %.2f"%total)
#problem10
A, B, C = input().split()
D, E, F = input().split()

code1, unit1, value1 = A, B, C
code2, unit2, value2 = D, E, F

total = (int(unit1) * float(value1)) + (int(unit2) * float(value2))

print ("VALOR A PAGAR: R$ %0.2f" % total)



