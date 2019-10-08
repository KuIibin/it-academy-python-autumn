# Посчитать количество строчных (маленьких) и прописных (больших)
# букв в введенной строке. Учитывать только английские буквы.

sents = input('Введите предложение: ')
sents = sents.replace(' ', '')
upperCount = 0
lowerCount = 0

for i in sents:
    if 'a' <= i <= 'z':
        lowerCount += 1
    elif 'A' <= i <= 'Z':
        upperCount += 1

print('Маленьких - {lowerCount} букв'.format(lowerCount=lowerCount))
print('Больших - {upperCount} букв'.format(upperCount=upperCount))
