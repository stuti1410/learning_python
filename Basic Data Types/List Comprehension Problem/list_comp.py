if __name__ == '__main__':
    i = int(input())
    j = int(input())
    k = int(input())
    n = int(input())
    combinations = [[x, y, z] for x in range(i+1) for y in range(j+1) for z in range(k+1) if (x+y+z) != n] # list comprehension for nested for loops
    print(combinations)
