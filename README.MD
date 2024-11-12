# Terfah - A Hobbyist Python-Based Programming Language

```
(ReadME is AI generated based on my code due to my laziness. I have proof-readed this but as all AI models are based on Transformer, which predicts the text and treat logical data like any novel, it may make up something, if something it said does not work. Please make a pull request. I will adjust the README.)
```

**Terfah** is a lightweight and flexible programming language inspired by Python, designed for hobbyists and learners interested in experimenting with a minimalist coding environment. With support for interactive execution in a REPL (Read-Eval-Print Loop) and the ability to run script files, Terfah provides an easy-to-use platform for understanding core programming concepts, testing code snippets, and more.

This README serves as a comprehensive guide for getting started with Terfah, covering installation, usage, syntax, error handling, and practical examples.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
    - [REPL Mode](#repl-mode)
    - [Script Mode](#script-mode)
4. [Code Syntax](#code-syntax)
    - [Variables](#variables)
    - [Functions](#functions)
    - [Conditional Statements](#conditional-statements)
    - [Input/Output](#inputoutput)
5. [Error Handling](#error-handling)
    - [Crash Reports](#crash-reports)
6. [Examples](#examples)
7. [Contributing](#contributing)
8. [License](#license)

---

## 1. Introduction

Terfah is a programming language built specifically for hobbyists, learners, and anyone interested in experimenting with simple coding constructs. Its design focuses on simplicity, making it ideal for testing small programs or learning how basic programming concepts like variables, functions, and conditionals work in practice. Terfah is Python-based and supports both interactive and script modes.

### Key Features:
- **REPL Mode**: Interactively test code line-by-line.
- **Script Mode**: Execute full `.tfah` script files.
- **Minimalist Syntax**: Focused on core programming constructs like variables, functions, conditionals, and basic input/output.

---

## 2. Installation

To run Terfah, you'll need Python 3 installed on your machine. Terfah doesn't require any external dependencies, making it easy to install and start using immediately.

### Installation Steps:
1. **Download Terfah**: Download the `terfah.py` script from the repository or save the file locally.
2. **Install Python**: Ensure Python 3.x is installed. You can download it from the [official Python website](https://www.python.org/downloads/).
3. **Run Terfah**:
    - Open your terminal or command prompt.
    - Navigate to the directory where `terfah.py` is located.
    - Start Terfah by running:
      ```bash
      python terfah.py
      ```

---

## 3. Usage

### REPL Mode

The REPL mode is designed for interactive use, allowing you to test and evaluate small pieces of code. It’s an excellent choice for quick experimentation, debugging, or learning.

To start the REPL, use the following command:
```bash
python terfah.py terfah
```

In the REPL, you can type Terfah code line-by-line. For example, entering a variable assignment and then printing the result would look like this:

**Example REPL session**:
```bash
Terfah REPL - Type 'exit' to quit
>>> x = 10
>>> out(x)
10
>>> y = x + 5
>>> out(y)
15
>>> exit
```

### Script Mode

In Script mode, you can run Terfah code from a `.tfah` script file. This is useful for executing larger programs that are too big for the REPL or for automation purposes.

To execute a script, use the following command:
```bash
python terfah.py tfex filename.tfah
```

**Example usage**:
```bash
python terfah.py tfex myscript.tfah
```

---

## 4. Code Syntax

Terfah’s syntax is simple and designed to be easy to understand. Below are the key components of the language.

### Variables

Variables are used to store values. In Terfah, you can store numbers, strings, booleans, and expressions in variables. Use the `=` operator to assign values to variables.

**Example**:
```terfah
x = 10           # Assigns the value 10 to variable x
name = "Alice"    # Assigns the string "Alice" to variable name
is_active = yes   # Assigns the boolean True to is_active
```

You can also use variables in expressions:
```terfah
z = x + 5         # Adds 5 to the value of x and assigns it to z
out(z)            # Prints the value of z (15 in this case)
```

### Functions

Functions in Terfah are defined using the `fn` keyword. A function’s body is enclosed in `done`. Functions can take parameters, which are passed when calling the function.

**Example**:
```terfah
fn greet
    out("Hello, " + name)
done

greet  # This will print: Hello, Alice
```

Functions can also accept parameters:
```terfah
fn add_numbers
    result = arg1 + arg2
    out(result)
done

add_numbers 5 7  # This will print: 12
```

### Conditional Statements

Terfah supports basic conditional constructs. You can use `if`, `elif`, and `else` to create branches in your program based on conditions.

**Example**:
```terfah
x = 10

if x > 5
    out("x is greater than 5")
done
else
    out("x is less than or equal to 5")
done
```

### Input/Output

Terfah provides simple commands for handling input and output.

- **Output**: The `out(statement)` function prints the given statement to the console.
  
  **Example**:
  ```terfah
  out("Enter your name:")
  ```

- **Input**: The `input` statement prompts the user for input and assigns the result to a variable.

  **Example**:
  ```terfah
  name = input
  out("Hello, " + name)
  ```

---

## 5. Error Handling

Terfah features built-in error handling with crash reports. If an error occurs during execution, Terfah will generate a crash report detailing the error and the code that caused it.

### Crash Reports

Crash reports are saved in a file named `crashreport.tfah` and include:
- The error message.
- The line(s) of code that caused the error.
- A traceback with detailed debugging information.

These crash reports are useful for identifying and fixing issues in your code.

**Example of a crash report**:
```text
Crash Report: 2024-11-11 15:25:30
Error: NameError: name 'foo' is not defined

Code Snippet that caused the error:
x = foo

Advanced Analysis:
Traceback (most recent call last):
  File "terfah.py", line 120, in execute
    eval_expression(statement)
  File "terfah.py", line 93, in eval_expression
    return eval(expression)
NameError: name 'foo' is not defined
```

---

## 6. Examples

Here are some practical examples to demonstrate the basic syntax and functionality of Terfah.

### Example 1: Hello World
```terfah
out("Hello, World!")
```

### Example 2: Simple Arithmetic
```terfah
x = 5
y = 10
out(x + y)  # Output will be 15
```

### Example 3: Function with Parameters
```terfah
fn add_numbers
    result = arg1 + arg2
    out(result)
done

add_numbers 5 7  # Output will be 12
```

### Example 4: Conditional Example
```terfah
x = 10

if x > 5
    out("x is greater than 5")
done
else
    out("x is less than or equal to 5")
done
```

---

## 7. Contributing

Terfah is an open-source project, and contributions are welcome! If you'd like to improve Terfah or add new features, feel free to open a pull request.

### Steps to Contribute:
1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and test them.
4. Commit and push your changes.
5. Open a pull request with a description of your changes.

---

## 8. License

Terfah is released under the **MIT License**. See [LICENSE](LICENSE) for more details.

---

Thank you for using Terfah! We hope it helps you in your programming journey. Whether you're learning, experimenting, or creating, Terfah is here to make coding fun and accessible.
