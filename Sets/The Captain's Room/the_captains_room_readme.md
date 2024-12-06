## Problem Overview
The INFINITE hotel has:

* A Captain who stays in a separate room.
* Multiple groups of tourists, each group consisting of k members.

Each room number appears exactly k times in the hotel records, except for the Captain's room number, which appears only once.

**Input:**

The first input is an integer, k, the size of each group.<br>
The second input is an unordered list of room numbers representing the hotel room assignments.

```
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
```

**Output:**

The room number of the Captain.

```
8
```

## My Notes
The `*` operator in `print(*elem)` is called the **unpacking operator**. It is used to unpack the elements of an iterable (e.g., list, set, tuple) and pass them as separate arguments to the `print()` function.

* **Without `*`**:

  ```
  elem = {8}
  print(elem)
  ```
  **Output**
  ```
  {8}
  ```
* **With `*`**:
  ```
  elem = {8}
  print(*elem)
  ```
  **Output**
  ```
  8
  ```
