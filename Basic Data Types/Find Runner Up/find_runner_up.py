if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    s = set(arr)  # converted the list to set to make the elements unique.
    sa = sorted(s)  # sorted in ascending order. At this point, the set is again converted to list.
    leng = len(sa)  # get the length of sorted list
    print(sa[leng-2])  # print the second last element of the list.
