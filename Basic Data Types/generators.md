Generators are higly involved with iterators, so before diving into genrators let's first understand what are iterators and how these work.

**Iterators** are object that allows you to loop through all the elements of a collection (like a list or tuple) one at a time without needing to access them by index.

**Generators** are a routine that can be used to control the iteration behaviour of a loop. A generator is very similar to a function that returns an array.

## Example for Iterators
Let's traverse through the numbers 1 to 10 without using the `range()` function and the `while` loop.

```
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  #A list holding numbers 1 to 10.

for elem in x:
  print(elem)  #This will simply loop through the list.
```

**Output:**
```
1
2
3
4
5
6
7
8
9
10
```

The problem here is that we are storing the numbers in memory which is not very efficient.
For ten numbers it's fine but for a large dataset it would not make sense to store the entire data in the memory.

Now, to overcome this issue, we can use `range()` function.
```
for i in range(1, 11):
  print(i)              #this gives the same result.
```

If we check the size of the data structure and the `range()` function, the `range()` will have lesser size because it doesn't need to store all the elements.
```
import sys

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  #A list holding numbers 1 to 10.

print(sys.getsizeof(x))
print(sys.getsizeof(range(1, 11)))

for elem in x:
  print(elem)  

for i in range(1, 11):
  print(i)              
```

**Output:**
```
136
48
1
.
.
.
10
```
