# Задание 2

def user_report(**kwargs):
    return kwargs


params = user_report(name='John', surname='Smith', birth='02-01-2001', city='New York', email='John_smith@gmail.com',
                     phone='+73475175379')

print(params.get('name'), params.get('surname'), params.get('birth'), params.get('city'), params.get('mail'),
      params.get('phone'))

# вариант с получением данных от пользователя

n = input("Name: ")
s = input("Surname: ")
b = input("Birth date: ")
c = input("City: ")
e = input("E-mail: ")
p = input("Phone: ")

def user_report(**kwargs):
    return kwargs

params = user_report(name=n, surname=s, birth=b, city=c, email=e, phone=p)

print("User info:", params.get('name'), params.get('surname'), params.get('birth'), params.get('city'),
      params.get('email'), params.get('phone'))
