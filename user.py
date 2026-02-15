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


def search_user_by_email(con):
    email = input('Введите email для поиска: ').strip().lower()
    cursor = con.cursor()
    cursor.execute(f''' SELECT id, name, email FROM users WHERE email LIKE '%{email}%' ''')
    users = cursor.fetchall()

    if users:
        print('Найденные пользователи: ')
        for user in users:
            print(f'ID: {user[0]}, Имя: {user[1]}, Почта: {user[2]}')
    else:
        print('Пользователь не найден')
    cursor.close()
