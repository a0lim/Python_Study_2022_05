# 6011
print(float(input()))

# 6012
a=int(input())
b=int(input())
print(a)
print(b)

# 6013
a=input()
b=input()
print(b)
print(a)

# 6014
a=input()
print(a)
print(a)
print(a)

# 6015
a, b = input().split()
print(int(a))
print(int(b))

# 6016
a,b=input().split()
print(b,a)

# 6017
a=input()
print(a,a,a)

# 6018
a,b=input().split(':')
print(a,b,sep=':')

# 6019
a,b,c=input().split('.')
print(c,b,a,sep='-')

# 6020
a,b=input().split('-')
print(a,b,sep='')

# 6021
a=input()
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

# 6022
a=input()
yy=a[0:2] # 0번째 이상, 2번째 미만
mm=a[2:4]
dd=a[4:6]
print(yy,mm,dd)

# 6023
a,b,c=input().split(':')
print(b)

# 6024
a,b=input().split(' ')
print(a+b)

# 6025
a,b=input().split(' ')
print(int(a)+int(b))

# 6026
a=float(input())
b=float(input())
print(a+b)

# 6027
a=int(input())
print('%x'%a)

# 6028
a=int(input())
print('%X'%a)

# 6029
a=input() ## 16진 정수 입력
n=int(a,16) ## a를 16진수로 인식한 값
print('%o'%n) ## 8진수로 출력

# 6030
n=ord(input()) # 입력 받은 문자를 10진수 유니코드 값으로 변환
print(n)

# 6031
n=int(input()) # 10진 정수 값을 유니코드 값으로 변환
print(chr(n))

# 6032
a=int(input())
print(a*(-1))

# 6033
a=ord(input()) ## 문자를 유니코드 값으로 변환
print(chr(a+1)) # a 문자의 다음 문자(c->d)를 출력 + 문자로 변경

# 6034
a,b=input().split(' ')
print(int(a)-int(b))

# 6035
a,b=input().split()
print(float(a)*float(b))

# 6036
a,b=input().split()
print(a*int(b))

# 6037
num=input()
line=input()
print(line*int(num))

# 6038
a,b=input().split()
print(int(a)**int(b))

# 6039
a,b=input().split()
print(float(a)**float(b))

# 6040
a,b=input().split()
print(int(a)//int(b))











