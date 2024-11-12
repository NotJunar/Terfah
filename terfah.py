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

        if not line:  
            i += 1
            continue

        try:

            line = replace_variables(line)

            if line.startswith("out"):
                statement = line[4:].strip()
                if statement in variables:
                    out(variables[statement])
                else:
                    out(eval_expression(statement))

            elif line.endswith("= input"):
                var_name = line.split("=")[0].strip()
                user_input = input()
                variables[var_name] = eval_expression(user_input)

            elif "=" in line:
                var_name, expression = map(str.strip, line.split("=", 1))
                variables[var_name] = eval_expression(expression)

            elif line.startswith("if"):
                condition = line[3:].strip()
                if eval_expression(condition):
                    i += 1
                    while i < len(code) and code[i].strip() != "done":
                        inner_line = code[i].strip()
                        execute([inner_line])
                        i += 1

            elif line.startswith("elif"):
                condition = line[5:].strip()
                if eval_expression(condition):
                    i += 1
                    while i < len(code) and code[i].strip() != "done":
                        inner_line = code[i].strip()
                        execute([inner_line])
                        i += 1

            elif line.startswith("fn"):
                fn_name = line.split()[1]
                fn_body = []
                i += 1
                while i < len(code) and code[i].strip() != "done":
                    fn_body.append(code[i])
                    i += 1
                functions[fn_name] = fn_body  

            elif line.split()[0] in functions:
                parts = line.split()
                fn_name = parts[0]
                args = parts[1:]
                fn_body = functions[fn_name]

                for index, arg in enumerate(args):
                    variables[f"arg{index + 1}"] = eval_expression(arg)

                execute(fn_body)

            elif line.startswith("content:modify"):
                parts = line.split()
                action = parts[1]
                filename = parts[-1]
                content = " ".join(parts[2:-1])  
                handle_content_modify(action, content, filename)

            elif line.startswith("content:replace"):
                parts = line.split()
                old_content = parts[1]
                new_content = parts[2]
                filename = parts[3]
                handle_content_replace(old_content, new_content, filename)

            elif line.startswith("content:delete"):
                filename = line.split()[1]
                handle_content_delete(filename)

            elif line.startswith("content:"):
                function_name = line.split(":")[1].strip()
                handle_content_function(function_name)

        except Exception as e:
            generate_crash_report(e, code)
            out(f"Error in script execution: {e}")
            break

        i += 1

def eval_expression(expression):
    try:

        if expression.lower() == "yes":
            return True
        elif expression.lower() == "no":
            return False

        if expression in variables:
            return variables[expression]

        return eval(expression)
    except:
        return expression.strip('"')

def replace_variables(line):
    """Replace all variables in the line with their values."""
    while "%" in line:
        start = line.find("%") + 1
        end = line.find("%", start)
        if start > 0 and end > start:
            var_name = line[start:end]
            if var_name in variables:
                line = line[:start-1] + str(variables[var_name]) + line[end+1:]
            else:
                line = line[:start-1] + "" + line[end+1:]
        else:
            break
    return line

def handle_content_modify(action, content, filename):
    if action == "modify":
        write_file(filename, content)
        out(f"File '{filename}' modified with new content.")

def handle_content_replace(old_content, new_content, filename):
    file_content = read_file(filename)
    modified_content = file_content.replace(old_content, new_content)
    write_file(filename, modified_content)
    out(f"Replaced '{old_content}' with '{new_content}' in '{filename}'.")

def handle_content_delete(filename):
    try:
        os.remove(filename)
        out(f"File '{filename}' deleted.")
    except FileNotFoundError:
        out(f"Error: File '{filename}' not found.")

def handle_content_function(function_name):

    out(f"Executing content-related function: {function_name}")

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
    crash_info += traceback.format_exc()  

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