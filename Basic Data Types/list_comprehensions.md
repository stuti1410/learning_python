List comprehensions provide a concise way to create lists.
They are used for constructing new lists by applying an expression to each item in an iterable (like a list, tuple, or range) and can also include optional conditions for filtering.

**Syntax**
```
[expression for item in iterable if condition]
```

### Examples
1. **Basic List Comprehension**

Create a list of squares of numbers from 1 to 5:
```
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]
```

2. **List Comprehension with Condition**

Create a list of even numbers from 1 to 10:
```
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)  # Output: [2, 4, 6, 8, 10]
```

3. **Using String Methods**

Convert a list of strings to uppercase:
```
words = ['hello', 'world']
uppercase_words = [word.upper() for word in words]
print(uppercase_words)  # Output: ['HELLO', 'WORLD']
```

4. **Nested Loops in List Comprehension**

Generate all combinations of numbers from two lists:
```
combinations = [(x, y) for x in range(1, 3) for y in range(3, 5)]
print(combinations)  # Output: [(1, 3), (1, 4), (2, 3), (2, 4)]
```

5. **Filtering with Multiple Conditions**

Get numbers divisible by both 2 and 3 from 1 to 20:
```
divisible = [x for x in range(1, 21) if x % 2 == 0 and x % 3 == 0]
print(divisible)  # Output: [6, 12, 18]
```

6. **Flatten a Nested List**

Flatten a 2D list into a 1D list:
```
matrix = [[1, 2], [3, 4], [5, 6]]
flat_list = [num for row in matrix for num in row]
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6]
```
