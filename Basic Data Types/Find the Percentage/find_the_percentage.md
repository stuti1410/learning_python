This program calculates and displays the average marks of a specific student based on the input provided.

**Input**

The first line enters an integer, `n`, the number of student's records.
The next `n` lines contain student name and their marks (space separated value).
Last line contains `query_name`, the name of the student for which score is to be calculated.
```
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
```

**Output**

Average marks obtained by the particular student upto exactly two decimal places.
```
56.00
```

## Code Explanation
```
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{avg:.2f}")
```

### Input Handling
- `n = int(input())`: Number of students.
- `name, *line = input().split()`: Splits each student's name and their scores.
  The `*line` syntax is a feature of Python's extended unpacking introduced in Python 3.
  It is used when the number of values to unpack isn't fixed, allowing you to gather multiple elements into a list.
### Calculations
- `scores = list(map(float, line))`: Converts scores to a list of floats.
- `avg = sum(student_marks[query_name]) / len(student_marks[query_name])`: Computes the average for the queried student.
### Output
- `print(f"{avg:.2f}")`: Prints the average with two decimal places.
  The `:.2f` format specification tells to print upto two decimal places.
  `.` refers to the decimal point, `2` specifies the number of decimal places to show, and `f` stands for "fixed-point notation," which means the number will always be displayed as a floating-point value.
