# This function replaces a specific type of character with something else. 

def char_replacer(string):
    for c in string:
        # change isupper() with a function that checks if c is of the type of character that you want to replace (e.g isdigit(), isalpha(), etc)# 
        if c.isupper(): 
            string = string.replace(c,    ) # <- write the replacement after the comma #
        else:
            #Makes sure that the other characters stay the same
            c = c
    
    # returns the string with the character replaced #
    return string 