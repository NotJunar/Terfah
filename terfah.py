import sys
import traceback
import os
from datetime import datetime

variables = {}
functions = {}

def out(statement):
    if isinstance(statement, str):
        print(statement)
    elif isinstance(statement, list):
        print(" ".join(map(str, statement)))
    else:
        print(statement)

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        out(f"Error: File '{filename}' not found")
        return ""

def write_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
    except Exception as e:
        out(f"Error writing to file: {e}")

def execute(code):
    i = 0
    while i < len(code):
        line = code[i].strip()

        if not line:  # Skip empty lines
            i += 1
            continue

        try:
            # Handle output
            if line.startswith("out"):
                statement = line[4:].strip()
                if statement in variables:
                    out(variables[statement])
                else:
                    out(eval_expression(statement))

            # Handle input
            elif line.endswith("= input"):
                var_name = line.split("=")[0].strip()
                user_input = input()
                variables[var_name] = eval_expression(user_input)

            # Handle variable assignment
            elif "=" in line:
                var_name, expression = map(str.strip, line.split("=", 1))
                variables[var_name] = eval_expression(expression)

            # Handle conditional statements
            elif line.startswith("if"):
                condition = line[3:].strip()
                if eval_expression(condition):
                    i += 1
                    while i < len(code) and code[i].strip() != "done":
                        inner_line = code[i].strip()
                        execute([inner_line])
                        i += 1

            # Handle elif statements
            elif line.startswith("elif"):
                condition = line[5:].strip()
                if eval_expression(condition):
                    i += 1
                    while i < len(code) and code[i].strip() != "done":
                        inner_line = code[i].strip()
                        execute([inner_line])
                        i += 1

            # Handle function definitions
            elif line.startswith("fn"):
                fn_name = line.split()[1]
                fn_body = []
                i += 1
                while i < len(code) and code[i].strip() != "done":
                    fn_body.append(code[i])
                    i += 1
                functions[fn_name] = fn_body  # Store the function body for later execution

            # Handle function calls with parameters
            elif line.split()[0] in functions:
                parts = line.split()
                fn_name = parts[0]
                args = parts[1:]
                fn_body = functions[fn_name]

                # Assign function arguments to variables
                for index, arg in enumerate(args):
                    variables[f"arg{index + 1}"] = eval_expression(arg)

                # Execute the function body
                execute(fn_body)

        except Exception as e:
            generate_crash_report(e, code)
            out(f"Error in script execution: {e}")
            break

        i += 1

def eval_expression(expression):
    try:
        # Check if it's a boolean value
        if expression.lower() == "yes":
            return True
        elif expression.lower() == "no":
            return False

        # Check if it's a variable
        if expression in variables:
            return variables[expression]

        # Try to evaluate as number or expression
        return eval(expression)
    except:
        return expression.strip('"')

def run_file(filename):
    code = read_file(filename)
    if code:
        execute(code.splitlines())

def run_repl():
    print("Terfah REPL - Type 'exit' to quit")
    while True:
        line = input(">>> ").strip()
        if line.lower() == "exit":
            break
        try:
            execute([line])
        except Exception as e:
            generate_crash_report(e, [line])
            print(f"Error: {e}")

def generate_crash_report(error, code):
    filename = "crashreport.tfah"
    crash_info = f"Crash Report: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    crash_info += f"Error: {str(error)}\n\n"
    crash_info += "Code Snippet that caused the error:\n"
    crash_info += "\n".join(code) + "\n\n"
    crash_info += "Advanced Analysis:\n"
    crash_info += traceback.format_exc()  # Get more detailed traceback for debugging
    
    # Write the crash report to a file
    with open(filename, 'w') as file:
        file.write(crash_info)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "terfah":
            run_repl()
        elif sys.argv[1] == "tfex" and len(sys.argv) > 2:
            run_file(sys.argv[2])
        else:
            print("Usage:")
            print("  terfah terfah           # Start REPL")
            print("  terfah tfex filename.tfah  # Run Terfah script")
    else:
        print("Usage:")
        print("  terfah terfah           # Start REPL")
        print("  terfah tfex filename.tfah  # Run Terfah script")
