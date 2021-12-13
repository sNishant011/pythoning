def twoSums(lis, target):
    for i in range(len(lis)):
        for j in range(len(lis)):
            if i != j:
                if (lis[i] + lis[j]) == target:
                    return [i, j]

print(twoSums([3,3], 6))