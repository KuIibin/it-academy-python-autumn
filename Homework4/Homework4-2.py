# List practice

# Use a list comprehension to construct the list ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
lst1 = [str(q + w) for q in 'ab' for w in 'bcd']
print(lst1)
# Use a slice on the above list to construct the list ['ab', 'ad', 'bc'].
lst2 = lst1[::2]
print(lst2)
# Use a list comprehension to construct the list ['1a', '2a', '3a', '4a'].
lst3 = [x+y for x in '1234' for y in 'a']
print(lst3)
# Simultaneously remove the element '2a' from the above list and print it.
print(lst3.pop(1))
# Copy the above list and add '2a' back into the list such that the original is still missing it.
lst3_copy = lst3[:]
lst3_copy.insert(1, '2a')
print(lst3_copy)
