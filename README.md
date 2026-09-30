# OOP Calculator

This project is a command-line calculator built in Python. It supports addition and subtraction while keeping a history of calculations during the current session. I built the project in stages to practice object-oriented programming, testing, error handling, and continuous integration.
## Installation

Clone the repository and move into the project folder:

```bash
git clone YOUR-REPOSITORY-URL
cd YOUR-REPOSITORY-NAME

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