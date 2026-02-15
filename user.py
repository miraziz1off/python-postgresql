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


def edit_user(con):
    email = input('Введите email для изменения: ').strip().lower()

    cursor = con.cursor()
    cursor.execute(f''' SELECT id, name, email FROM users WHERE email='{email}'; ''')
    user = cursor.fetchone()

    if user:
        print(f"Найден пользователь: ID: {user[0]}, Имя: {user[1]}, Почта: {user[2]}")

        new_name = input(f"Введите новое имя (оставьте пустым, если не хотите менять): ").strip()
        new_email = input(f"Введите новый email (оставьте пустым, если не хотите менять): ").strip().lower()

        if new_name:
            cursor.execute(f'''UPDATE users SET name = '{new_name}' WHERE id = {user[0]}''')

        if new_email:
            cursor.execute(f'''UPDATE users SET email = '{new_email}' WHERE id = {user[0]}''')

        con.commit()
        print('Данные успешно обновлены!')

    else:
        print('ПОльзователь не найден')

    cursor.close()

def delete_user(con):
    email = input('Введите email пользователя для удаления: ').strip().lower()

    cursor = con.cursor()
    cursor.execute(f'''SELECT id FROM users WHERE email='{email}' ''')
    user = cursor.fetchone()

    if user:
        cursor.execute(f'''DELETE FROM users WHERE id='{user[0]}'; ''')
        con.commit()
        print("Пользователь успешно удален.")
    else:
        print("Пользователь не найден.")

    cursor.close()