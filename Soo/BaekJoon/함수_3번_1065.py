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
