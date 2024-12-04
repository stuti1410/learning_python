import string

def print_rangoli(size):
    if 0 < size < 27: 
        width = ((size * 2) - 1) + (((size * 2) - 1) - 1)
        alphabets = string.ascii_lowercase
        rows = []
        for i in range(size):
            subset = alphabets[i:size]
            row = "-".join(subset[::-1] + subset[1:])
            rows.append(row.center(width, "-"))
        pattern = rows[::-1] + rows[1:]
        print("\n".join(pattern))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
