# f the names of 2 friends are same; what will happen to the program in problem 6?
dict_with_duplicates = {'a': 1, 'b': 2, 'b': 3, 'c': 4}
print(dict_with_duplicates)  # Output: {'a': 1, 'b': 3, 'c': 4}
'''When merging dictionaries, overlapping keys from the second dictionary will overwrite the values of the first dictionary.
When creating a dictionary with duplicate keys, Python will only keep the last value for each key, effectively overwriting earlier values with the same key.Dono me resut same hi aayega '''