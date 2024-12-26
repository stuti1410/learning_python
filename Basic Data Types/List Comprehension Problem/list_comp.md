## Problem Overview
Task is to output a list of three variables `x`, `y`, and `z` where the sum of the variables should not be equal to `n`. User inputs these three variables along an integer `n`.

**Input**

Four integers `x`, `y`, `z`, and `n`; each on a separate line.
```
1
1
1
2
```

**Output**
Print the list.
```
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
```

### Example
x = 1
y = 1
z = 2
n = 3
In this case, all combinations will be:
[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2]]

Print only those combinations that do not sum to n = 3.
[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]
