## 1. Concatenation `+`
```python
original = "Hello"
new_item = "World"
result = original + " " + new_item
print(result)  # 'Hello World'
```

## 2. Using `join()`
```python
original = "Hello"
additional_items = ["World", "!"]
result = " ".join([original] + additional_items)
print(result)  # 'Hello World !'
```

## 3. Adding at a Specific Position
Use slicing to insert items into a string at a specific position:
```python
original = "HelloWorld"
new_item = " "
position = 5  # Add space after "Hello"
result = original[:position] + new_item + original[position:]
print(result)  # 'Hello World'
```

## 4. Using String Formatting (`f-strings` or `.format()`)
```python
name = "Alice"
greeting = f"Hello, {name}!"
print(greeting)  # 'Hello, Alice!'
```

## 5. Appending Items in a Loop
```python
items = ["apple", "banana", "cherry"]
result = ""
for item in items:
    result += item + ", "
result = result.rstrip(", ")  # Remove trailing comma
print(result)  # 'apple, banana, cherry'
```
Or with `join()`:
```python
items = ["apple", "banana", "cherry"]
result = ", ".join(items)
print(result)  # 'apple, banana, cherry'
```

## 6. Adding Using List Conversion
Convert a string into a list, manipulate it, and then join it back:
```python
original = "HelloWorld"
characters = list(original)
characters.insert(5, " ")  # Insert a space at index 5
result = "".join(characters)
print(result)  # 'Hello World'
```
