import string

def print_rangoli(size):
    if 0 < size < 27: 
        width = ((size * 2) - 1) + (((size * 2) - 1) - 1)
        alphabets = string.ascii_lowercase
        rows = []
        for i in range(size):
            subset = alphabets[i:size] # subset = abcde; bcde
            # Create the pattern: reverse + forward (without duplicating the center)
            row = "-".join(subset[::-1] + subset[1:]) # edcba + bcde => edcbabcde => e-d-c-b-a-b-c-d-e; edcb + cde => edcbcde => e-d-c-b-c-d-e
            # Center the row with dashes
            rows.append(row.center(width, "-")) # e-d-c-b-a-b-c-d-e; --e-d-c-b-c-d-e--
        # Combine rows: top half + bottom half
        pattern = rows[::-1] + rows[1:]
        print("\n".join(pattern))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
