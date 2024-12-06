K = int(input())
rooms = list(map(int, input().split()))
seen = set()
duplicates = set()
for items in rooms:
    if items not in seen:
        seen.add(items)
    else:
        duplicates.add(items)
elem = seen - duplicates
print(*elem)
