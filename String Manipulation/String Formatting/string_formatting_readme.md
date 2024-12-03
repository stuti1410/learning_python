To print the decimal, octal, hexadecimal, and binary representations of a number, use the built-in functions `oct()`, `hex()`, and `bin()` for octal, hexadecimal, and binary respectively.

The `[2:]` is **Slice Notation**. It is used to extract a portion of a string.<br>
The slicing syntax is: `sequence[start:stop:step]`<br>
**Examples:**
1. `hex(255)` Returns `0xff` and `hex(255)[2:]` Returns `ff`.<br>
2. `alphabets[i:size]` - Here, `i:size` slice selects a portion of the string starting at the position i and ending before size.
3. If `subset = 'abc'`, then: `subset[::-1]  # Reverse the string`.

`.upper()` converts the remaining hexadecimal digits to uppercase.

`.rjust()`, `.ljust()`, and `.center()` are used for adjusting the characters as right justified, left justified and center respectively.
