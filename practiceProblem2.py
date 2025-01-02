def checkoutTime(n, c, t):
    t.sort(reverse=True)
    lines = [0] * c
    for i in range(n):
        lines[lines.index(min(lines))] += t[i]
        print(lines)
    return max(lines)

print(checkoutTime(5, 3, [2,3,10,4,5]))