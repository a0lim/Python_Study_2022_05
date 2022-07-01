#문제
#어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. 
#N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

#입력
#첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

#출력
#첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

def save_num_of_Han(N):
    num_of_Han=99
    if N<100:
      num_of_Han=N
    elif 100<=N<=1000:
       for n in range(100,N+1):
         N_list=[int(i) for i in str(n)]
         N_100=N_list[0]
         N_10=N_list[1]
         N_1=N_list[2]
         if N_100-N_10==N_10-N_1:
             num_of_Han += 1
    return num_of_Han

N=int(input())
print(save_num_of_Han(N))
