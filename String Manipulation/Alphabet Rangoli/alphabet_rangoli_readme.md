## Problem Overview
The task is to generate a rangoli pattern using the English alphabets where each row contains a series of letters. The pattern is as follows:
```
#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
```

## My Notes:

To print alphabets from a to z, use the string module or the `chr()` function with a range. For example,

### Method 1: Using `string.ascii_lowercase`
```
import string

# Print all lowercase alphabets
print(string.ascii_lowercase)
```
**Output:** abcdefghijklmnopqrstuvwxyz

### Method 2: Using `chr()` with a Range
The chr() function converts a Unicode code point (integer) to its corresponding character.
```
# Print alphabets using chr()
for i in range(97, 123):  # ASCII values for 'a' to 'z' are 97 to 122; 97 inclusive and 123 exclusive.
    print(chr(i), end="")
```
**Output:** abcdefghijklmnopqrstuvwxyz

### Method 3: List Comprehension
```
# Create a list of alphabets and join them
alphabets = "".join([chr(i) for i in range(97, 123)])    # The "".join() method takes the list of characters and concatenates them into a single string, with no separator ("").
print(alphabets)
```
**Output:** abcdefghijklmnopqrstuvwxyz
