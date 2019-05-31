def solution(K, A):
    S=0
    result =[]
    for x in range(0, len(A)):
        #print(S)
        if S<K: S +=A[x]
        elif S>=K: 
            result.append(S)
            S=A[x]
    if S>=K: result.append(S)    
    return (len(result))