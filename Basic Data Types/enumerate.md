The `enumerate()` function is a built-in function that allows you to loop over an iterable (like a list, tuple, or string) while keeping track of the index of the current item.
It returns an iterator of tuples, where each tuple contains an index and the corresponding item from the iterable.

**Syntax**
```python
enumerate(iterable, start=0)
```

## Example Usage
### 1. Looping with Indices
```python
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")
```
**Output**
```
Index: 0, Fruit: apple
Index: 1, Fruit: banana
Index: 2, Fruit: cherry
```

### 2. Starting from a Different Index
```python
for index, fruit in enumerate(fruits, start=1):
    print(f"Index: {index}, Fruit: {fruit}")
```
**Output**
```
Index: 1, Fruit: apple
Index: 2, Fruit: banana
Index: 3, Fruit: cherry
```

