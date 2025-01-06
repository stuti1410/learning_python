# Generators
**Generators** are a type of iterable, like lists or tuples. However, unlike lists, they do not store all their values in memory at once. Instead, they generate values on the fly and provide them one at a time, which makes them memory-efficient.

- Generators are a way to create iterators using functions.
- Instead of returning a single value and terminating, a generator function can yield multiple values, one at a time, pausing and resuming its state between each yield.

## Key Features
- **Lazy Evaluation:** Generators compute values as needed, which saves memory.
- **State Retention:** They retain their state between yields, making them efficient for tasks like streaming data.
- **Iterable Nature:** You can use a generator in a `for` loop or convert it to a list using `list()`.

## How to Create Generators
### 1. Using Generator Functions
A generator function uses the `yield` keyword to produce values one at a time.
```
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# Using the generator
gen = count_up_to(5)
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
```

### 2. Using Generator Expressions
Generator expressions are like list comprehensions but use parentheses `()` instead of square brackets `[]`.
```
gen_exp = (x ** 2 for x in range(5))
print(next(gen_exp))  # Output: 0
print(next(gen_exp))  # Output: 1
```
## Generator Methods
- `next()`: Fetch the next value from the generator.
- `send(value)`: Sends a value to the generator, resumes its execution, and can modify its state.
- `close()`: Stops the generator.

Example with send():
```
def interactive_gen():
    value = 0
    while True:
        value = yield value
        if value == 'stop':
            break

gen = interactive_gen()
print(next(gen))       # Output: 0
print(gen.send(10))    # Output: 10
gen.close()
```
