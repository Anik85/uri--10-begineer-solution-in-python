#priblem31
x,y=map(int,input().split())
diff=y-x
if diff<0:
  diff1=24+(y-x)
  print("O JOGO DUROU %d HORA(S)"%diff1)
elif x==y:
  print("O JOGO DUROU 24 HORA(S)")
else:
  print("O JOGO DUROU %d HORA(S)"%diff)
#problem32
w,x,y,z=map(int,input().split())
diff_hour=y-w
if diff_hour<0:
    diff_hour=24+(y-w)
diff_min=z-x
if diff_min<0:
    diff_min=60+(z-x)
    diff_hour=diff_hour-1
if y==w and z==x:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)"%(diff_hour,diff_min))
#problem33
salary=float(input())
if salary>=0 and salary<=400.00:
    Money_earned=0.15*salary
    new_salary=salary+Money_earned
    print("Novo salario: %.2f"%new_salary)
    print("Reajuste ganho: %.2f"%Money_earned)
    print("Em percentual: 15 %")
elif salary>=400.01 and salary<=800.00:
    Money_earned = 0.12 * salary
    new_salary = salary + Money_earned
    print("Novo salario: %.2f" % new_salary)
    print("Reajuste ganho: %.2f" % Money_earned)
    print("Em percentual: 12 %")
elif salary>=800.01 and salary<=1200.00:
    Money_earned = 0.1 * salary
    new_salary = salary + Money_earned
    print("Novo salario: %.2f" % new_salary)
    print("Reajuste ganho: %.2f" % Money_earned)
    print("Em percentual: 10 %")
elif salary>=1200.01 and salary<=2000.00:
    Money_earned = 0.07 * salary
    new_salary = salary + Money_earned
    print("Novo salario: %.2f" % new_salary)
    print("Reajuste ganho: %.2f" % Money_earned)
    print("Em percentual: 7 %")
elif salary>2000.00:
    Money_earned = 0.04 * salary
    new_salary = salary + Money_earned
    print("Novo salario: %.2f" % new_salary)
    print("Reajuste ganho: %.2f" % Money_earned)
    print("Em percentual: 4 %")
#problem34
x=input()
y=input()
z=input()
if x=="vertebrado":
    if y=="ave":
        if z=="carnivoro":
            print("aguia")
        elif z=="onivoro":
            print("pomba")
    elif y=="mamifero":
        if z=="onivoro":
            print("homem")
        elif z=="herbivoro":
            print("vaca")
elif x=="invertebrado":
    if y=="inseto":
        if z=="hematofago":
            print("pulga")
        elif z=="herbivoro":
            print("lagarta")
    elif y=="anelideo":
        if z=="hematofago":
            print("sanguessuga")
        elif z=="onivoro":
            print("minhoca")
#problem35
n = int(input())
details = {
    61: "Brasilia",
    71: "Salvador",
    11: "Sao Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitoria",
    31: "Belo Horizonte"
}
if n == 61:
    print(details[61])
elif n == 71:
    print(details[71])
elif n == 11:
    print(details[11])
elif n == 21:
    print(details[21])
elif n == 32:
    print(details[32])
elif n == 19:
    print(details[19])
elif n == 27:
    print(details[27])
elif n == 31:
    print(details[31])

else:
    print("DDD nao cadastrado")



from collections import Counter
L=input()
length=Counter(L)
for k,v in length.items():
    if v>1:
        print(k,"has",v,"times")
#another
string=input()
count = 0
for i in range(0, len(string)):
    for j in range(i + 1, len(string)):
        if (string[i] == string[j]):
            count=count+1
if count==0:
    print("yes")
else:
    print("No")

#problem37
n=int(input())
if n==1:
    print("January")
elif n==2:
    print("February")
elif n==3:
    print("March")
elif n==4:
    print("April")
elif n==5:
    print("May")
elif n==6:
    print("June")
elif n==7:
    print("July")
elif n==8:
    print("August")
elif n==9:
    print("September")
elif n==10:
    print("October")
elif n==11:
    print("November")
elif n==12:
    print("December")
#problem38
for i in range(1,100+1):
    if i%2==0:
        print(i)
#problem39
count=0
for i in range(1,7):
    n=float(input())
    if n>0:
        count=count+1
print("%d valores positivos"%count)
#problem40
valor = input().split()
d1 = int(valor[1])
valores = input().split(" : ")
h1,m1,s1 = list(map(int,valores))
valor = input().split()
d2 = int(valor[1])
valores = input().split(" : ")
h2,m2,s2 = list(map(int,valores))

d = d2 - d1

h = h2 - h1
if(h < 0):
    h = 24 + h
    d = d - 1

m = m2 - m1
if(m < 0):
    m = 60 + m
    h = h - 1

s = s2 - s1
if(s < 0):
    s = 60 + s
    m = m - 1

if(d <= 0):
    d = 0

print("%d dia(s)" %d)
print("%d hora(s)" %h)
print("%d minuto(s)" %m)
print("%d segundo(s)" %s)




