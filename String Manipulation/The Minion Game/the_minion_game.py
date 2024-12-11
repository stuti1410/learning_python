def minion_game(string):
    size = len(string)
    count_kevin = 0
    count_stuart = 0
    for i in range(size):
        if string[i] in 'AEIOU':
            count_kevin += size - i
        else:
            count_stuart += size - i
    if count_kevin == count_stuart:
        print('Draw')
    elif count_kevin > count_stuart:
        print('Kevin ' + str(count_kevin))
    else:
        print('Stuart ' + str(count_stuart))

if __name__ == '__main__':
    s = input()
    minion_game(s)
