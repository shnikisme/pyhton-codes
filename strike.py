T=input()
T=int(T)
i=0
while i<T:
        N=input()
        N=int(N)
        if N%2==0:
                P=1
                Q=10**(N/2)
                print(P,end=' ')
                print(Q)
        else:
                P=1
                Q=10**((N-1)/2)
                print(P,end=' ')
                print(Q)
                i=i+1
