def swap_case(s):
    for elem in s:
        if elem.islower():
            result = s.swapcase()
        if elem.isupper():
            result = s.swapcase()
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
