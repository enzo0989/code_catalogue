import re
# Function that returns True if the string only has letters, numbers and spaces.
# requires: re module

def task_validation(string):
    task_pattern = r"^[a-zA-Z0-9 ]*$"

    if re.match(task_pattern,string):
        return True