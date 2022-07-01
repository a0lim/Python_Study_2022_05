#문제
#N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

#입력
#첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

#출력
#입력으로 주어진 숫자 N개의 합을 출력한다.

def solve(a,b):
    result=0
    num_list=[int(i) for i in b]
    for i in range(a):    
        result += num_list[i]
    return result

num_of_num=int(input())
num=input()

print(solve(num_of_num, num))
