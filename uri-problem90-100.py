'''#just practice
digit={
    "1": "one ",
    "2": "two",
    "3": "three",
    "4": "four"
}
phone=input()
output=""
for ch in phone:
    output += digit.get(ch,"!")+" "
print(output)

def function(N):
    for i in range(1,N):
        print(i,end=" ")
    print(N)
N=int(input())
if 1<=N<=1000:
    function(N)
#lucky divisions
n=int(input())
if 1<=n<=1000:
    arr=[4,7,47,74,44,444,447,474,477,777,774,744]
    flag=0
    for i in range(len(arr)):
        if n%arr[i]==0:
            flag=True
    if flag:
        print("YES")
    else:
        print("NO")'''