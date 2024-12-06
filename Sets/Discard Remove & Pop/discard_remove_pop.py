if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    N = int(input())
    for _ in range(N):
        entry = input().split()
        command = entry[0]
        if command == "pop":
            if s:
                first_elem = min(s)
                s.remove(first_elem)
        elif command == "remove" or command == "discard":
            s.discard(int(entry[1]))
    print(sum(s))
