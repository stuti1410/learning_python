# Problem Overview
Given:
* An array of integers.
* Two disjoint sets:
* Set A: The integers you like.
* Set B: The integers you dislike.

**Initial Happiness:**

You start with a happiness of 0. For each integer in the array:
* If the integer is in set A, you gain 1 unit of happiness.
* If the integer is in set B, you lose 1 unit of happiness.
* If the integer is in neither set, your happiness doesn't change.

**Objective:**

At the end, output your total happiness.

**Input**
* The first line contains two integers n (the size of the array) and m (the size of sets A and B).
* The second line contains n space-separated integers representing the elements of the array.
* The third line contains m space-separated integers representing the elements of set A.
* The fourth line contains m space-separated integers representing the elements of set B.
```
3 2
1 5 3
3 1
5 7
```

**Output**

Output a single integer representing your total happiness.
```
1
```
