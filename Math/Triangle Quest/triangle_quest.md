## Problem Overview
Given a positive integer `n`, print a numerical triangle with `n` rows. Each row contains the number `i` repeated `i` times, where `i` is the row number. The challenge is to write only two lines in code.
```
1
22
333
4444
55555
......
```

**Input**
A single line containing integer `n`.
```
5
```

**Output**
```
1
22
333
4444
55555
```

### Code
```
for i in range(1, int(input())): 
    print(((10**i) // 9) * i)
```
