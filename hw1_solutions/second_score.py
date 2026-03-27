n = int(input())
arr = list(map(int, input().split()))

unique = sorted(set(arr))

if len(unique) == 1:
    print(unique[0])
else:
    print(unique[-2])