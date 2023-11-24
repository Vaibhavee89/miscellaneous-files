T= int(input())

for i in range(T):
    A,B,C= list(map(int,input().split()))
    for K in range(1,100):
        if A%K!=0 and B%K!=0 and C%K!=0:
            print(K)
    
