# Snippet to delete a row in a csv file that uses dictionaries.
# Requires pandas
import pandas as pd

del_num = int(input(" Number of row : "))
df = pd.read_csv(list)
# Uses del_num as an index and deletes the entire row in that position. 
# e.g del_num = 2, all the content in the row N°2 gets deleted.

df = df.drop(df.index[del_num])
df.to_csv(list, index=False)


