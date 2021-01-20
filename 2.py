def line_name(user_name, surname, year, city, email, phone):
    return f'Имя: {user_name}, Фамилия: {surname}, год рождения: {year},' \
           f'город: {city}, email: {email}, Номер телефона: {phone}'


print(line_name(surname='Иванов', user_name='Вася', city='Москва',
                phone='+7 495 555 44 33', email='vasya95@mail.ru', year='1995'))
