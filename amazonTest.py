def groupSort(arr):
    countArray = []
    for ele in arr:
        if [ele, arr.count(ele)] not in countArray:
            countArray.append([ele, arr.count(ele)])

    return sorted(countArray, key=lambda x: (x[1], -x[0]))


print(groupSort([2, 1, 2, 2, 3]))