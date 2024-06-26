# Posit Python Library

A Python library for posit number representation.

## Features

- Create posit numbers from integer and floating-point values.
- Perform arithmetic operations on posit numbers (addition, subtraction, multiplication, division).
- Convert between posit numbers and floating-point values.

## Installation

You can install the library using pip:

```bash
pip install posit-python-library
```

## Usage

Here is an example of how to use the Posit library:

```python
from posit import Posit

# Create Posit numbers
posit1 = Posit(2.5, total_bits=16, exponent_bits=1)
posit2 = Posit(1.5, total_bits=16, exponent_bits=1)

# Print Posit numbers
print("posit1:", posit1)
print("posit2:", posit2)

# Perform arithmetic operations
posit3 = posit1 + posit2
print("posit1 + posit2:", posit3)

posit4 = posit1 - posit2
print("posit1 - posit2:", posit4)

posit5 = posit1 * posit2
print("posit1 * posit2:", posit5)

posit6 = posit1 / posit2
print("posit1 / posit2:", posit6)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
