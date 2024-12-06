T = int(input())
for items in range(T):
    n = int(input())
    A = set(map(int, input().split()))
    m = int(input())
    B = set(map(int, input().split()))
    result = getattr(B, "intersection")(A)
    if result == A:
        print("True")
    else:
        print("False")
