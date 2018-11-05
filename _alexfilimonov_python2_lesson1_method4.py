#4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления 
#в байтовое и выполнить обратное преобразование (используя методы encode и decode).

a= 'разработка'.encode('Utf-8')
b= 'администрирование'.encode('Utf-8')
c= 'protocol'.encode('Utf-8')
d= 'standard'.encode('Utf-8')

print('Variable a has type - ',type(a),', content - ',a,' length - ', len(a)) 
print('Variable b has type - ',type(b),', content - ',b,' length - ', len(b)) 
print('Variable c has type - ',type(c),', content - ',c,' length - ', len(c)) 
print('Variable d has type - ',type(d),', content - ',d,' length - ', len(d)) 

a= a.decode('Utf-8')
b= b.decode('Utf-8')
c= c.decode('Utf-8')
d= d.decode('Utf-8')

print('')
print('After decoding from byte to string:')
print('Variable a has type - ',type(a),', content - ',a,' length - ', len(a)) 
print('Variable b has type - ',type(b),', content - ',b,' length - ', len(b)) 
print('Variable c has type - ',type(c),', content - ',c,' length - ', len(c)) 
print('Variable d has type - ',type(d),', content - ',d,' length - ', len(d)) 
