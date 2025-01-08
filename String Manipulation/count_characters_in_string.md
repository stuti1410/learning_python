To count the frequency of each character in a string:

## Using a Dictionary
```python
string = "Hello, World!"
char_count = {}

for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("Character count:")
for char, count in char_count.items():
    print(f"{char}: {count}")
```
Output
```
Character count:
H: 1
e: 1
l: 3
o: 2
,: 1
 : 1
W: 1
r: 1
d: 1
!: 1
```

## Using `collections.Counter`
```python
from collections import Counter

string = "Hello, World!"
char_count = Counter(string)

print("Character count:")
for char, count in char_count.items():
    print(f"{char}: {count}")
```
Output
```
Character count:
H: 1
e: 1
l: 3
o: 2
,: 1
 : 1
W: 1
r: 1
d: 1
!: 1
```

## Using a `for` loop with `set` to avoid duplicate counting
```python
string = "Hello, World!"

unique_chars = set(string)  # Get unique characters
print("Character count:")
for char in unique_chars:
    print(f"{char}: {string.count(char)}")
```
Output
```
Character count:
H: 1
e: 1
o: 2
d: 1
l: 3
,: 1
!: 1
 : 1
W: 1
r: 1
```
