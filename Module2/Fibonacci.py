def FibList(n):
    solution = [0,1]
    if n > 1:
        for i in range(2,n+1):
            solution.append(solution[i-1] + solution[i-2])
    
    return solution[n]

print(FibList(7))

def EuclidDGC(a,b):
    print(a,b)
    if b ==0:
            return a
    return EuclidDGC(b, a%b)
    
print(EuclidDGC(48,18))