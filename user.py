def create_user(con):
    name = input('Введите имя: ').strip()
    email = input('Введите email: ').strip().lower()

    if not name or not name.strip():
        print('Ошибка: Name не может быть пустым')
        return

    if not email or not email.strip():
        print('Ошибка: Email не может быть пустым')
        return

    cursor = con.cursor()
    query = f'''SELECT email FROM users WHERE email = '{email}' '''
    cursor.execute(query)
    exists = cursor.fetchone()

    if exists is not None:
        print(f'Пользователь с email {email} уже зарегистрирован!')
    else:
        cursor.execute(f''' INSERT INTO users (name, email) VALUES ('{name}', '{email}'); ''')
        print(f'Пользователь {name} добавлен успешно!')
        con.commit()
    cursor.close()

def unsubscribe_user(con):
    email = input('Введите email пользователя: ').lower().strip()
    cursor = con.cursor()

    cursor.execute(''' SELECT id FROM  ''')