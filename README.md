# OOP Calculator

This project is a command-line calculator built in Python. It supports addition and subtraction while keeping a history of calculations during the current session. I built the project in stages to practice object-oriented programming, testing, error handling, and continuous integration.
## Installation

Clone the repository and move into the project folder:

```bash
git clone git@github.com:ms543-create/my-oop-calculator.git
cd my-oop-calculator

## Running the Calculator

Start the calculator with:

```bash
python -m calculator
```

The available commands are:

- `add` - Add two numbers
- `subtract` - Subtract the second number from the first
- `history` - Show calculations from the current session
- `remove` - Remove a calculation from history
- `help` - Show the available commands
- `exit` - Exit the calculator

## Testing

Run the test suite with:

```bash
python -m pytest
```

The project requires 100% line and branch coverage. The tests check the calculator operations, calculation history, command-line interface, and error handling.

## Design Choices

I used a `Calculation` abstract class as a shared contract for the different calculator operations. `Add` and `Subtract` inherit from it and each provide their own version of `get_result()`. This allows the program to work with different calculations through the same method without checking which type of calculation it is every time.

I used a separate `History` class to manage the calculations from the current session. History stores calculation objects and controls how they are added, viewed, and removed. Returning a copy of the history list prevents outside code from directly changing the internal list.

The command-line interface is kept separate from the calculation classes. Its job is to take user input, create the correct calculation object, display results, and handle invalid input without crashing the program.

## Reflection

### Adding Multiply

If I wanted to add multiplication, I would create a `Multiply` class that inherits from `Calculation` and give it its own `get_result()` method. I would also register `Multiply` in the CLI operations dictionary, add `multiply` to the help menu, and write tests for its results and CLI behavior. The `History` class would not need multiplication-specific code because it already works with any object that follows the `Calculation` contract.

### Email and Text Notifications

Email and text-message notification classes could share a common `send()` method. A parent notification class could require each notification type to implement `send()`, while the email and text classes handle the actual sending differently. Other parts of the program could then call `send()` without needing to know which type of notification object they received.

### Transferring the Design to Another Language

The main design ideas from this project can transfer to other programming languages. Ideas like classes, objects, inheritance, abstraction, polymorphism, encapsulation, and separating responsibilities are not limited to Python. I would still need to learn the other language's syntax and rules, such as how it defines classes, handles abstract methods, checks types, manages collections, and handles exceptions.


## Part 1 Reflection

I originally thought creating a `Calculation` would perform the operation immediately. After the refactor, I learned that construction only stores the operands and operation. The operation does not run until `get_result()` is called.

With composition, adding an absolute difference operation only required adding a new function and tests. With the previous inheritance design, I would have needed another `Calculation` subclass with its own `get_result()` implementation.


## Part 2 Reflection

The creation step now takes an operation name, normalizes it, selects the correct operation, and returns a configured `Calculation`. The math does not run during this process. It only runs later when `get_result()` is called.

The construction policy now lives in `CalculationFactory`. For example, `absolute_difference` is registered there instead of requiring each caller to know which function should be used.


## Part 3 Reflection

The old `a` and `b` interface changed because not every operation needs exactly two values. Storing a collection of values allows the same `Calculation` class to support unary, binary, and many-value operations.

The factory still validates requests because flexible arguments do not mean every combination of inputs is valid. It checks operation names, operand counts, allowed options, and numeric option values before constructing a calculation.

In a function definition, `*values` gathers positional arguments and `**options` gathers named arguments. At a call site, `*values` unpacks positional values and `**options` unpacks named settings.

For the independent exercise, I added `scale`, which takes one value and an optional `factor`. Its construction rules are registered in the factory, while a zero factor fails later when the calculation executes.