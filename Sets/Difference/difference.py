if __name__ == "__main__":
    n = int(input())
    Eng_roll = set(map(int, input().split()))
    b = int(input())
    Fre_roll = set(map(int, input().split()))
    print(len(Eng_roll - Fre_roll))
