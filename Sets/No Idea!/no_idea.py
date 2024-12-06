if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    happy = 0
    for elem in arr:
        if elem in a:
            happy += 1
        if elem in b:
            happy -= 1     
    print(happy)
