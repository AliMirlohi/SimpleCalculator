# SimpleCalculator

A simple calculator application built with Python using the Tkinter library for the graphical user interface.

## Features

- Perform basic arithmetic operations: addition, subtraction, multiplication, and division.
- User-friendly graphical interface with separate input fields for two numbers.
- Error handling for invalid inputs and division by zero.
- Real-time display of results in the interface.


## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/AliMirlohi/SimpleCalculator.git
   cd SimpleCalculator
   ```

2. Make sure `tkinter` is available. It comes pre-installed with most Python distributions. If not, install it:

   - On Ubuntu/Debian:
     ```bash
     sudo apt-get install python3-tk
     ```

   - On Windows/macOS: Tkinter is included by default with Python.

### Running the Calculator

```bash
python calculator.py
```

The calculator window will open, allowing you to enter two numbers and perform operations.

## Usage

1. Enter the first number in the "input number 1" field.
2. Enter the second number in the "input number 2" field.
3. Click one of the operation buttons: `+`, `-`, `*`, `/`.
4. The result will be displayed in the "result" field.
5. If an invalid input or division by zero is detected, an error message will be shown.

## Project Structure

```
SimpleCalculator/
│
├── calculator.py   # Main application script
├── README.md       # Project documentation
```

## Code Overview

- **calculator.py**: Contains the GUI setup and arithmetic logic using Tkinter.
- Variables and error handling ensure the calculator is robust for common usage scenarios.



---

*Created by AliMirlohi*
