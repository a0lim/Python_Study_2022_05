# 6041
from regex import B, F


a,b=input().split()
a=int(a); b=int(b)
print(a%b)

# 6042
a=float(input())
print(format(a, ".2f")) ## , 다음에 공백 넣기

# 6043
f1,f2=input().split()
f1=float(f1)
f2=float(f2)
print(format((f1/f2), ".3f"))

# 6044
a,b=input().split()
a=int(a); b=int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b) # 몫
print(a%b) # 나머지
print(format(a/b, ".2f"))

# 6045
a,b,c=map(int,input().split())
#a=int(a); b=int(b); c=int(c)
#a,b,c=int(a,b,c)
sum=a+b+c
median=float(sum/3)
print(sum, format(median, "0.2f"))


# 6046
a=input()
a=int(a)
print(a<<1) ## 비트연산: print(a<<1)이면 a*2가 출력됨


# 6047
a,b=map(int,input().split())
print(a<<b)

# 6048
a,b=input().split()
a=int(a); b=int(b)
print(a<b)

# 6049
a,b=input().split()
a=int(a); b=int(b)
print(a==b)

# 6050
a,b=input().split()
a=int(a); b=int(b)
print(b>=a)

# 6051
a,b=input().split()
a=int(a); b=int(b)
print(a!=b)

# 6052
a=input()
a=int(a)
print(a!=0)

# 6053
a=input()
a=int(a)
print(not int(a))

# 6054
a,b=input().split()
a=int(a); b=int(b)
print(a==1 & b==1)

# 6055
a,b=input().split()
a=int(a); b=int(b)
print(bool(a) or bool(b)) ## bool은 T/F란 의미/bool(a): a가 True

# 6056
a,b=input().split()
a=int(a); b=int(b)
print(bool(a)!=bool(b))
#print(a!=b)

# 6057
a,b=input().split()
a=int(a); b=int(b)
print(bool(a)==bool(b))
#print(a==b)

# 6058
a,b=input().split()
a=int(a); b=int(b)
print(bool(a)==bool(b)==False)

# 6059
a=int(input())
print(~a)

# 6060
a,b=input().split()
a=int(a); b=int(b)
print(a&b)

# 6061
a,b=input().split()
a=int(a); b=int(b)
print(a|b)

# 6062
a,b=input().split()
a=int(a); b=int(b)
print(a^b)

# 6063
a,b=input().split()
a=int(a); b=int(b)
print(a if (a>b) else b)

# 6064
a,b,c=input().split()
a=int(a); b=int(b); c=int(c)
print((a if (a<b) else b) if ((a if (a<b) else b)<c) else c)

# 6065
a, b, c = input().split()

a=int(a)
b=int(b)
c=int(c)

if a%2==0:
    print(a)
    
if b%2==0:
    print(b)
    
if c%2==0:
    print(c)
 
# 6066
a, b, c = map(int, input().split())

if (a % 2 == 0):
    print("even")
else:
    print("odd")
    
if (b % 2 == 0):
    print("even")
else:
    print("odd")
    
if (c % 2 == 0):
    print("even")
else:
    print("odd")

# 6067
n=int(input())

if n<0:
  if n%2==0:
    print('A')
  else:
    print('B')
else:
  if n%2==0:
    print('C')
  else:
    print('D')

# 6038
a=int(input())

if a>=90:
    print("A")
elif a>=70:
    print("B")
elif a>=40:
    print("C")
else:
    print("D")


# 6039
a=input()

if a=='A':
    print("best!!!")
elif a=='B':
    print("good!!")
elif a=='C':
    print("run!")
elif a=='D':
    print("slowly~")
else:
    print("what?") 

# 6040
a=int(input())
if a//3==1:
    print("spring")
elif a//3==2:
    print("summer")
elif a//3==3:
    print("fall")
else:
    print("winter")
