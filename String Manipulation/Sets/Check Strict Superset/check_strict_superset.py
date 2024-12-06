A = set(map(int, input().split()))
n = int(input())
T = True
for items in range(n):
    other = set(map(int, input().split()))
    if not A > other:
        T = False
        break
print(T)
