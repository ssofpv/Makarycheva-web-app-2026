
N = int(input())
records = []
for _ in range(N):
    name = input().strip()
    score = float(input())
    records.append((name, score))
scores = sorted(set(s for _, s in records))
second = scores[1]
names = sorted(n for n,s in records if s == second)
for n in names:
    print(n)
