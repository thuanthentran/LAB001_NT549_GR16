from itertools import product

K, M = map(int, input().split())

lists = []

for _ in range (K):
    arr = list(map(int, input().split()))
    lists.append(arr[1:])

max_value = 0

for combination in product(*lists):
    total = sum(x*x for x in combination)
    value = total%M
    if value > max_value:
        max_value = value
        
print (max_value)
