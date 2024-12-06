The `.add()` method is used to insert a single element into an existing set. If the element is already present, it will not be added again, ensuring the uniqueness of the set.

**Syntax**
```
set.add(element)
```

# Problem Overview
Rupal has a collection of country stamps, and she wants to know how many distinct stamps she has.
Given a stack of stamps, your task is to help her count the total number of distinct country stamps using the `.add()` operation.

**Input**

* The first line contains an integer n, representing the total number of country stamps.
* The next n lines contain the name of a country where each stamp is from.
```
7
UK
China
USA
France
New Zealand
UK
France
```

**Output**

Output the total number of distinct country stamps on a single line.
```
5
```
