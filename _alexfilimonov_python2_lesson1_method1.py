#1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате 
#и проверить тип и содержание соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать 
#строковые представление в формат Unicode и также проверить тип и содержимое переменных.

a= 'разработка'
b= 'сокет'
c= 'декоратор'
print('Variable a has type - ',type(a),', content - ',a,' length - ', len(a)) 
print('Variable b has type - ',type(b),', content - ',b,' length - ', len(b)) 
print('Variable c has type - ',type(c),', content - ',c,' length - ', len(c)) 

a= 'разработка'.encode('Utf-8')
b= 'сокет'.encode('Utf-8')
c= 'декоратор'.encode('Utf-8')

print('Variable a has type - ',type(a),', content - ',a,' length - ', len(a)) 
print('Variable b has type - ',type(b),', content - ',b,' length - ', len(b)) 
print('Variable c has type - ',type(c),', content - ',c,' length - ', len(c)) 