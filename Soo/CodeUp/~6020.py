#6015
#공백을 두고 입력된정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.

a,b=input().split()     #split()
print(int(a))
print(int(b))

#6018
#24시간 시:분 형식으로 시간이 입력될 때, 그대로 출력하는 연습을 해보자.

a, b = input().split(':')         #콜론 ':' 기호를 기준으로 자른다.
print(a, b, sep=':')              #콜론 ':' 기호를 사이에 두고 값을 출력한다.
