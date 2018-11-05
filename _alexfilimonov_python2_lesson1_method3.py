#3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

b = b'attribute'
#b = b'класс'
#b = b'функция'
b = b'type'

print('Bytes can only contain ASCII literal character, because of that «attribute» and «type» can be in 1 byte per character format, the words in cyrillic are not!') 
