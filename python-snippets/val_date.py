import re
#Snippet to validate a date in DD/MM/YYYY format.
#Requires: re module.


def date_validation(date):
    date_pattern = r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[012])-(20)[2-9]\d$"
    
    if re.match(date_pattern,date):
        return True
