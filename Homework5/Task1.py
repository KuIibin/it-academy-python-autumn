# Define a dict comprehension which returns a dictionary
# where the keys are numbers between 1 and n (both included)
# and the values are square of keys. n – function argument.
# Default is 20.
# Define a code which count and return the numbers of each
# character in a count_me_string argument.
# Example:
# If the following string is given as argument to the function:
# abcdefgabc
# Then, the return result of the function should be:
# {'a': 2, 'b': 2, 'c': 2, 'd': 1, 'e': 1, 'f': 1, 'g': 1}

number = int(input('Введите число: '))
dct = {el: el**2 for el in range(1, number + 1)}
print(dct)

sent = input('Введите предожение: ')
dct2 = {el: sent.count(el) for el in sent}
print(dct2)

# second solution
sent2 = input('Введите предожение: ')
dctWithFrequency = {} 
  
for el in sent2: 
    if el in dctWithFrequency: 
        dctWithFrequency[el] += 1
    else: 
        dctWithFrequency[el] = 1
print(dctWithFrequency)
