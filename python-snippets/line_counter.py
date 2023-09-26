# A function that counts how many lines of code are in a file. It was created for python files but it can be adapted for other languages.
import sys
def line_counter(file_name):

    try:
        f = open(file_name)
        lines = f.readlines()
        count = 0
        for line in lines:
            line = line.strip(" ")
            # Doesn't count comments and blank lines, 
            # therefore if a line doesn't start with '#' or isn't blank it adds 1 to the counter.
            if line.startswith("#") == False and line.isspace() == False:
                count += 1
        return count

    except FileNotFoundError:
        sys.exit("File does not exist")