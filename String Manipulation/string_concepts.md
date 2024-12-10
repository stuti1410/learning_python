# Convert character to int
The `ord()` function is used to get the Unicode code point (an integer representation) of a given character.
This function is the opposite of the `chr()` function, which converts an integer back into a character.

**Usage**
```
print(ord('a'))  # Output: 97
print(ord('A'))  # Output: 65
print(ord('1'))  # Output: 49
print(ord('@'))  # Output: 64
```
The `print(ord('1'))` returns 49, which is the Unicode code point for the character `'1'`.

If you want to convert the character `'1'` to the integer `1`, you can use the `int()` function instead:
```
print(int('1'))  # Output: 1
```
# Convert int to character
Using `chr()` with a Range
The `chr()` function converts a Unicode code point (integer) to its corresponding character.
```
# Print alphabets using chr()
for i in range(97, 123):  # ASCII values for 'a' to 'z' are 97 to 122; 97 inclusive and 123 exclusive.
    print(chr(i), end="")
```
Output: abcdefghijklmnopqrstuvwxyz

> Ascii value for lowercase alphabets ranges from 97 to 122 and uppercase alphabets are between 65 to 90.
