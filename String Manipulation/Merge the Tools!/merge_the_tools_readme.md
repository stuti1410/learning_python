# Merge the Tools

This program takes a string and an integer `k` as input, splits the string into substrings of length `k`, and processes each substring to remove duplicate characters while maintaining the order of their first appearance.
The unique characters of each substring are then printed on separate lines.

## How It Works

1. **Input**: The program accepts two inputs:
   - A string (`string`) containing the data to process.
   - An integer (`k`) which determines the size of the substrings.

2. **Splitting into Substrings**: The string is split into consecutive non-overlapping substrings of length `k`.

3. **Removing Duplicates**: For each substring:
   - Iterate through the characters.
   - Add characters to a new string only if they have not appeared before.

4. **Output**: The unique characters from each substring are printed on separate lines.

## Code Explanation

```python
# Function to process the string
def merge_the_tools(string, k):
    size = len(string)  # Get the length of the string
    t = ""  # Temporary string to hold substrings

    # Loop through the string in steps of k
    for i in range(0, size, k):
        t = string[i:i+k]  # Extract substring of length k
        u = ""  # String to hold unique characters

        # Loop through characters in the substring
        for j in t:
            if j not in u:  # Check for duplicates
                u += j
        print(u)  # Print the result for the current substring

# Main block
if __name__ == '__main__':
    string, k = input(), int(input())  # Take input from the user
    merge_the_tools(string, k)  # Call the function
```

## Example

### Input
```
AABCAAADA
3
```

### Output
```
AB
CA
AD
```

### Explanation
- The input string `AABCAAADA` is divided into three substrings of length 3:
  1. `AAB`
  2. `CAA`
  3. `ADA`
- For each substring, duplicate characters are removed while maintaining the order of first appearance:
  1. `AAB` -> `AB`
  2. `CAA` -> `CA`
  3. `ADA` -> `AD`

## Key Concepts

- **String slicing**: Used to extract substrings of a fixed length.
- **Set operations**: Avoided for ordering; manual check ensures order is preserved.
- **Loops**: Nested loops handle substring processing and duplicate removal.

## Usage

1. Copy the code into a Python environment.
2. Run the script.
3. Provide the string and integer `k` as input when prompted.

## Notes

- The value of `k` must be a divisor of the length of the string for the program to work correctly.
- The function ensures that only unique characters in their first occurrence order are retained for each substring.
