## 1. Using `.find()`
The `.find()` method returns the index of the first occurrence of the substring. If the substring is not found, it returns `-1`.
```
text = "Hello, World!"
substring = "World"
index = text.find(substring)
if index != -1:
    print(f"Substring found at index {index}")
else:
    print("Substring not found")
```

## 2. Using `in` operator
The `in` operator checks if a substring exists within a string and returns `True` or `False`:
```
text = "Hello, World!"
substring = "World"
if substring in text:
    print("Substring found!")
else:
    print("Substring not found!")
```

## 3. Using `.index()`
Similar to `.find()`, the `.index()` method also returns the index of the first occurrence of the substring, but it raises a `ValueError` if the substring is not found.
```
text = "Hello, World!"
substring = "World"
try:
    index = text.index(substring)
    print(f"Substring found at index {index}")
except ValueError:
    print("Substring not found")
```

## 4. Using `.count()`
If you just want to know how many times a substring appears in the string, you can use `.count()`.
```
text = "Hello, World! World!"
substring = "World"
count = text.count(substring)
print(f"Substring appears {count} times")
```
