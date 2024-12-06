## Overview
In Python, while operations like union, intersection, difference, and symmetric difference return new sets without modifying the original set, set mutations perform in-place updates to the set.

## Mutation Operations
### `.update()` or `|=`
Updates the set by adding elements from another iterable (e.g., list, tuple, or another set).

**Example:**
```
H = set("Hacker")
R = set("Rank")
H.update(R)
print(H)
```
**Output:**
```
{'a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'}
```

### `.intersection_update()` or `&=`
Keeps only elements present in both the original set and another iterable.

**Example:**
```
H = set("Hacker")
R = set("Rank")
H.intersection_update(R)
print(H)
```
**Output:**
```
{'a', 'k'}
```

### `.difference_update()` or `-=`
Removes elements from the set that are found in another iterable.

**Example:**
```
H = set("Hacker")
R = set("Rank")
H.difference_update(R)
print(H)
```
**Output:**
```
{'c', 'e', 'H', 'r'}
```

### `.symmetric_difference_update()` or `^=`
Keeps only elements found in either set but not in both.

**Example:**
```
H = set("Hacker")
R = set("Rank")
H.symmetric_difference_update(R)
print(H)
```
**Output:**
```
{'c', 'e', 'H', 'n', 'r', 'R'}
```

# Problem Overview
You are given a set A and several other sets. Perform specific mutation operations on A using the given sets. At the end, print the sum of elements in A.

**Input**

* The first line contains the number of elements in set A.
* The second line contains the elements of set A (space-separated).
* The third line contains the number of other sets, N.
* For the next N sections:
    * The first line contains the operation name and the size of the other set.
    * The second line contains the elements of the other set.
 
```
16
1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
4
intersection_update 10
2 3 5 6 8 9 1 4 7 11
update 2
55 66
symmetric_difference_update 5
22 7 35 62 58
difference_update 7
11 22 35 55 58 62 66
```

**Output**

Print the sum of elements in set A after performing all operations.

```
38
```

# My Notes

In the line:
```
getattr(A, entry)(other)
```
The `getattr()` function is used to dynamically call a method of the set object A based on the operation name provided as input `(entry)`.

The `getattr()` function retrieves an attribute of an object by name. Here:

* `A`: The set object.
* `entry`: The operation name (e.g., 'intersection_update', 'update').
* `getattr(A, entry)`: Retrieves the method from A that matches the name in entry.
  
For example:

If `entry = 'update'`, `getattr(A, 'update')` is equivalent to calling `A.update`.
If `entry = 'intersection_update'`, `getattr(A, 'intersection_update')` is equivalent to calling `A.intersection_update`.

### How it works
```
getattr(A, entry)(other)
```
* `getattr(A, entry)`: Finds the method of set A corresponding to the string entry.<br>
   For example, if `entry = 'difference_update'`, this returns the method `A.difference_update`.
* `(other)`: Calls the retrieved method with the argument other, which is the second set involved in the operation.<br>
   Equivalent to `A.difference_update(other)` if `entry = 'difference_update'`.
