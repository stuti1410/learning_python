## `.strip()`
The `.strip()` method is used to remove any leading (spaces at the beginning) and trailing (spaces at the end) whitespace characters from a string.
It can also remove other specified characters if passed as an argument.

**Example**
```
text = "  Hello, World!  "
clean_text = text.strip()
print(clean_text)  # Output: "Hello, World!"
```
If you want to remove specific characters, you can pass them as an argument:
```
text = "***Hello, World!***"
clean_text = text.strip('*')
print(clean_text)  # Output: "Hello, World!"
```
The `.strip()` method doesn't modify the original string but returns a new string with the unwanted characters removed.

## `.replace()`
If you want to remove asterisks from both the beginning, end, and middle, you can use the `.replace()` method to remove all occurrences of the asterisk in the string.
```
text = "***Hello,*** World***"
clean_text = text.replace('*', '')
print(clean_text)  # Output: "Hello, World"
```
