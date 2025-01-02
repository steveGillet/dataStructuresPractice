def dependentTest(n):
    k = set()
    k.add(1)
    for i in range(1,n//2+1):
        k.add(n//i)
    return sum(k)

print(dependentTest(13))