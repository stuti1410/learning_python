if __name__ == '__main__':
    N = int(input())
    country_list = set()
    i = 0
    while i < N:
        x = input()
        country_list.add(x)
        i += 1
    print(len(country_list))
