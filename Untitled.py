def toPalid(lis):
    "How many times operations can transfer to Palidrame"
    i,j = 0,len(lis)-1
    op = 0
    while True:
        if j <= i:
            break
        if lis[i] == lis[j]:
            i += 1
            j -= 1
        elif lis[i] < lis[j]:
            op += 1
            lis[i+1] += lis[i]
            i += 1
        elif lis[i] > lis[j]:
            op += 1
            lis[j-1] += lis[j]
            j -= 1
    return op

n = input()
lis = list(map(int,input().split()))
print(lis)
print(toPalid(lis))





assert toPalid([4,4]) == 0
assert toPalid([4535]) == 0
assert toPalid([3,4]) == 1
assert toPalid([1,1,1,3]) == 2
assert toPalid([3,4,5,6,7,8,9]) == 6
