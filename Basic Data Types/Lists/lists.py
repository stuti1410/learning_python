if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        query, *line = input().split()
        numbers = list(map(int, line))
        if query == "insert":
            l.insert(numbers[0], numbers[1])
        if query == "print":
            print(l)
        if query == "remove":
            l.remove(numbers[0])
        if query == "append":
            l.append(numbers[0])
        if query == "sort":
            l.sort()
        if query == "pop":
            l.pop()
        if query == "reverse":
            l.reverse()
