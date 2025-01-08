# List Operations Program

This Python program allows you to perform various operations on a list based on user input. It demonstrates the use of list manipulation methods such as `insert`, `remove`, `append`, `sort`, `pop`, and `reverse`.

## How It Works

1. The program first takes an integer input `N` representing the number of commands to execute.
2. It processes `N` commands, one by one.
3. Depending on the command, the program performs the corresponding operation on the list `l`.

## Supported Commands

The following commands are supported:

### 1. `insert`
Inserts the integer `e` at index `i`.

**Example:**
```text
insert 1 5
```
**Action:** Inserts `5` at index `1`.

### 2. `print`
Prints the current state of the list.

**Example:**
```text
print
```
**Action:** Prints the list.

### 3. `remove`
Removes the first occurrence of the integer `e` from the list.

**Example:**
```text
remove 5
```
**Action:** Removes the first occurrence of `5` from the list.

### 4. `append`
Appends the integer `e` to the end of the list.

**Example:**
```text
append 3
```
**Action:** Adds `3` to the end of the list.

### 5. `sort`
Sorts the list in ascending order.

**Example:**
```text
sort
```
**Action:** Sorts the list in-place.

### 6. `pop`
Removes the last element of the list.

**Example:**
```text
pop
```
**Action:** Removes the last element.

### 7. `reverse`
Reverses the list.

**Example:**
```text
reverse
```
**Action:** Reverses the list in-place.

## Input Format
1. An integer `N` representing the number of commands.
2. `N` lines of commands as described above.

**Example Input:**
```text
5
append 1
append 2
insert 1 3
print
reverse
```

## Output Format
The program outputs the result of the `print` command(s).

**Example Output:**
```text
[1, 3, 2]
```

## Example Usage
**Input:**
```text
7
append 3
append 1
append 2
sort
print
pop
reverse
```

**Output:**
```text
[1, 2, 3]
[2, 1]
```

## Code
```python
if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        query, *line = input().split()
        numbers = list(map(int, line))
        if query == "insert":
            l.insert(numbers[0], numbers[1])
        if query == "print":
            print(l)
        if query == "remove":
            l.remove(numbers[0])
        if query == "append":
            l.append(numbers[0])
        if query == "sort":
            l.sort()
        if query == "pop":
            l.pop()
        if query == "reverse":
            l.reverse()
