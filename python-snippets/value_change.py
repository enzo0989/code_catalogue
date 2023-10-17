# Snippet that changes a value in a specific row in a dictionary of a csv file.

import pandas as pd

df = pd.read_csv(list)
num_mod = int(input("Number of the row you want to change: "))

new_value = input("new value: ")

df.loc[num_mod,"placeholder_key"] = new_value
df.to_csv(list, index=False)

# Num_mod is used as an index for placeholder_key, 
# Which is a valid key of the dictionary inside the csv file.
# Then, changes the previous value for a new one. 
#e.g if num_mod is equal to 1, the task N°1 will be replaces with the value of new_task.

