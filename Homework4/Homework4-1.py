# Write a program that prints the numbers from 1 to 100,
# but for multiples of three print “Fizz” instead of the number
# and for multiples of five print “Buzz”. For numbers which are
# multiples of both three and five, print “FizzBuzz”.

lst = []
for el in range(1, 101):
    if (el % 15) == 0:
        el = 'FizzBuzz'
        lst.append(el)
    elif (el % 3) == 0:
        el = 'Fizz'
        lst.append(el)
    elif (el % 5) == 0:
        el = 'Buzz'
        lst.append(el)
    else:
        lst.append(el)
print(lst)
