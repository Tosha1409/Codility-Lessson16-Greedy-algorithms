def solution(A, B):
    l=len(A)
    result=l
    currentA=-1
    currentB=-1
    x=0
    while x<l:
        if (currentB>=A[x]): result -=1
        else: 
            currentA=A[x]
            currentB=B[x]
            while (x<l-1) and (B[x]==B[x+1]):
                result -=1
                if A[x]<A[x-1]: currentA=A[x+1]
                x += 1
        x +=1
    return(result)