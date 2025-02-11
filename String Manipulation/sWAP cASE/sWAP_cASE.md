# swap_case Function

## Description
This Python script defines a function `swap_case(s)`, which takes a string `s` as input and returns a new string with its case swapped — lowercase letters are converted to uppercase, and uppercase letters are converted to lowercase.

## Implementation
```python
def swap_case(s):
    return s.swapcase()
```

## Usage
To use this script, run it in a Python environment and provide an input string:

```bash
$ python script.py
```

Example input and output:
```bash
Input:  "Hello World"
Output: "hELLO wORLD"
```

## Running the Script
The function can be tested using an interactive Python shell or included in a script with user input handling:

```python
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
```
This allows the function to process user input from the command line and print the result.

