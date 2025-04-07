# With the else clause
current_key = 'Mike'
default_val = 'Cohen'
dict_1 = {'John': 'Doe', 'Jane': 'Doe', 'Mike': 'Smith', 'Anna': 'Taylor'}
try:
    johns = dict_1.pop(current_key)
except KeyError:  # Non-existent key
    dict_1[current_key] = default_val
    print(f"{len(dict_1)} remaining key(s) in the dictionary")
else:
    print(f"{len(dict_1)} remaining key(s) in the dictionary")
print(dict_1)