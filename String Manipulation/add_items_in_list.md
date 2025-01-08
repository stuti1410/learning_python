## 1. Using `append()`
Adds a single element to the end of the list.
```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
```

## 2. Using `extend()`
Adds all elements of another iterable (e.g., list, tuple) to the list.
```python
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
```

## 3. Using `insert()`
Inserts an element at a specific index.
```python
my_list = [1, 2, 3]
my_list.insert(1, 10)  # Insert 10 at index 1
print(my_list)  # Output: [1, 10, 2, 3]
```

## 4. Using `+` Operator
Concatenates lists to create a new list.
```python
my_list = [1, 2, 3]
new_list = my_list + [4, 5, 6]
print(new_list)  # Output: [1, 2, 3, 4, 5, 6]
```

## 5. Using List Comprehension
Adds elements by processing an existing list or other iterables.
```python
my_list = [1, 2, 3]
my_list = [x * 2 for x in my_list]  # Double each element
print(my_list)  # Output: [2, 4, 6]
```

## 6. Using a Loop
Add elements dynamically based on conditions.
```python
my_list = [1, 2, 3]
for i in range(4, 7):
    my_list.append(i)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
```

### Choosing the Right Method
* Use `append()` for single elements.
* Use `extend()` for multiple elements.
* Use `insert()` for inserting at specific positions.
* Use `+` for creating a new list without modifying the original.
