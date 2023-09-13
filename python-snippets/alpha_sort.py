# This snippet is useful to sort dictionaries or lists.

dictionary = { }
# Assign the keys of dictionary to a list.
keys = dictionary.keys()
# Using the function sorted, the keys get sorted alphabetically.
sorted_dictionary = sorted(keys)
# creates a int variable to iterate through the sorted keys.
length = len(sorted_dictionary)
# This loop prints the value of a key and the key on his side.
for i in range(length):
        # It checks if the key is inside dictionary, and then retreats the value related to the key and prints both.
        if sorted_dictionary[i] in dictionary[i]:
                print(dictionary.get(sorted_dictionary[i]), sorted_dictionary[i])