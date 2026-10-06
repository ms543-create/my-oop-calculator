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


## Part 4 Reflection

The Command pattern gives different application actions the same `execute()` contract. `CalculateCommand`, `HistoryCommand`, `ClearHistoryCommand`, `HelpCommand`, and `CountCommand` perform different tasks, but the CLI can invoke them through the same method.

`CalculatorSession` acts as the receiver. It executes a calculation first and only adds it to history if the calculation succeeds. This is why a failed calculation, such as division by zero, does not increase the history or count.

The `count` feature belongs as an application action instead of a mathematical operation because it does not perform math on operands. It looks at the current calculator session and reports how many successful calculations have been saved.

A static operation performs the actual math, a `Calculation` object stores an operation with its inputs, and a `Command` represents an application action that can be executed.


## Part 5 Reflection

Statistics use the same calculation system as the earlier arithmetic operations. The mean and standard deviation functions validate the observations first and then use a pandas Series to calculate the result. Standard deviation supports `ddof=1` for sample deviation and `ddof=0` for population deviation.

CSV input is kept separate from the mathematical operations. The CSV reader turns a DataFrame column into a list of observations, and those observations are then passed through the same factory and numeric validation used for manually entered values. This means the source of the data does not change the mathematical request.

The flow for CSV data is DataFrame → Series → list → numeric tuple → stored operation → result. File reading belongs in `inputs.py`, mathematical rules belong in `statistics.py` and `operations.py`, construction belongs in the factory, and display belongs in the command and CLI layers.

For the independent exercise, I updated the CSV reader so a caller can select another documented column such as `observation`. The statistics and calculation components remain independent of the file structure because they only receive observations after the CSV reader has extracted the selected column.


## Part 6 Reflection

A successful power request starts with the CLI receiving the request and passing the operation name, values, and options to the factory. The factory selects the static operation and constructs a `Calculation` that stores the callable and its inputs. A command tells the session to execute the calculation. The session calls `get_result()` and adds the calculation to history only after it succeeds.

A failed division follows the same path through construction, but execution raises a `ZeroDivisionError`. Because the calculation never finishes successfully, the session does not add it to history. The application boundary catches the expected error so later work can continue.

Earlier in the calculator project, operations such as `Add` were subclasses of `Calculation`. The newer design uses composition instead. A `Calculation` stores a static callable such as `Operations.add` rather than inheriting the mathematical behavior. This makes it easier to add operations without creating another calculation subclass.

The factory and commands have different responsibilities. The factory creates a `Calculation` from an operation name, operands, and supported options. A command represents an application action, such as calculating, displaying history, clearing state, or reporting a summary.

`History.get_history()` returns a shallow copy. This protects the internal history list because adding or removing items from the returned list cannot change the stored list. The limitation is that the objects inside the copied list are still the same objects, so it is not a deep copy.

For sequence processing, iteration belongs in the sequence layer while successful recording stays in `CalculatorSession.calculate()`. Each item has its own `try` block so one failure does not stop later calculations. When raw requests are processed, factory construction is also inside the `try` block so preparation failures such as an unknown operation can be handled independently.

The session now retains failures separately from successful history. The summary action reports the number of successes and failures. I chose for `clear()` to reset both because they are both part of the current session state, and tests establish that rule.

Configured unary operations follow a contract before they are added to the factory. For example, `power` accepts exactly one operand, allows the `exponent` option, and defaults the exponent to 2. The factory handles operand counts and allowed option names while the operation performs the math.

Input structure stays separate from mathematical behavior. `inputs.py` understands CSV columns, while `Operations` and the statistics functions only work with numeric observations. This allows the input schema to change without adding file knowledge to the math layer.

The cumulative test suite provides evidence that the new behavior works and that earlier behavior still passes. The sequence tests specifically prove that a successful calculation after a failure still executes and that only successes enter history. Coverage also verifies that the implemented lines and branches are exercised. A limitation is that 100% coverage does not prove every possible requirement or input case is correct, and an older CI result would not prove the current revision works.