if __name__ == "__main__":
    n = int(input())
    A = set(map(int, input().split()))
    N = int(input())
    for _ in range(N):
        entry, _ = input().split()
        other = set(map(int, input().split()))
        getattr(A, entry)(other)
    print(sum(A))
