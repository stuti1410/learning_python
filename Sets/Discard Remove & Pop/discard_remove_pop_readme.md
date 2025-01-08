# Overview
## `.remove(x)`
* Removes the element `x` from the set.
* If `x` does not exist in the set, it raises a `KeyError`.
* Returns `None`.
```python
s = {1, 2, 3, 4, 5}
s.remove(3)
print(s)  # Output: {1, 2, 4, 5}

s.remove(10)  # KeyError: 10
```

## `.discard(x)`
* Removes the element `x` from the set, but does not raise an error if `x` is not found.
* Returns `None`.
```python
s = {1, 2, 3, 4, 5}
s.discard(3)
print(s)  # Output: {1, 2, 4, 5}

s.discard(10)  # No error, set remains unchanged
```

## `.pop()`
* Removes and returns an arbitrary element from the set.
* If the set is empty, raises a `KeyError`.
```python
s = {1, 2, 3}
popped_element = s.pop()
print(popped_element)  # Output: 1 (or any arbitrary element)
print(s)  # Output: {2, 3}
```

# Problem Overview
You are given a set and a series of commands. Your task is to execute the commands, which could be `pop`, `remove`, or `discard`, and then compute the sum of the remaining elements in the set.

**Input**
* The first line contains the integer n, the number of elements in the set.
* The second line contains space-separated integers representing the elements of the set.
* The third line contains the integer m, the number of commands to execute.
* The next m lines contain commands followed by an integer argument for remove or discard.
```
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
pop
discard 5
```

**Output**

Output the sum of the remaining elements in the set after performing all operations.
```
4
```
