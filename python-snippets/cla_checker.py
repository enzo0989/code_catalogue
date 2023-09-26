# Snippet that checks if a CLA is valid and if there are more or less than what the program needs.

import sys

if len(sys.argv) == "number": # change for a number lower than whats needed.
        sys.exit("Too few command-line arguments")
elif len(sys.argv) >= "number": # change for a number larger than whats needed.
        sys.exit("Too many command-line arguments")


if sys.argv[1].endswith(".extension") == False: # change extension for the type of file that you need.
        sys.exit("Not a valid file")

else:
    # write the code that you want to execute on the file
    sys.argv[1] = "something"