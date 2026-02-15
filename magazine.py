def create_magazine(con):
    title = input('Введите название журнала: ').strip()
    description = input('Введите описание журнала : ').strip()

    if not title:
        print('Title Не может быть пустым')
        return
    cursor = con.cursor()
    cursor.execute(f''' SELECT title FROM magazines WHERE title='{title}' ''')

    exists = cursor.fetchone()

    if exists:
        print(f'Ошибка: уже есть журнал с названием {title}')
        cursor.close()
        return

    cursor.execute(f''' INSERT INTO magazines (title, description) VALUES ('{title}','{description}');  ''')
    print(f'Журнал {title} добавлен успешно!')
    con.commit()
    cursor.close()

def get_info(con):
    cursor = con.cursor()
    cursor.execute("SELECT id, name, email FROM users;")
    users = cursor.fetchall()

    if users:
        print('Пользователи: ')
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")
    else:
        print("Нет пользователей.")

    cursor.execute("SELECT id, title FROM magazines;")
    magazines = cursor.fetchall()

    if magazines:
        print("\nЖурналы:")
        for magazine in magazines:
            print(f"ID: {magazine[0]}, Title: {magazine[1]}")
    else:
        print("Нет журналов.")

    cursor.execute("""
            SELECT u.name, u.email, m.title
            FROM subscriptions s
            JOIN users u ON s.user_id = u.id
            JOIN magazines m ON s.magazine_id = m.id;
        """)
    subscriptions = cursor.fetchall()

    if subscriptions:
        print("\nПодписки:")
        for sub in subscriptions:
            print(f"Пользователь: {sub[0]} ({sub[1]}) подписано на журнал {sub[2]}")
    else:
        print("Нет подписок.")

    cursor.close()

def search_magazine_by_title(con):
    title = input('Введите название журнала для поиска: ')
    cursor = con.cursor()
    cursor.execute(f"SELECT id, title, description FROM magazines WHERE title LIKE '%{title}%'; ")
    magazines = cursor.fetchall()

    if magazines:
        print("Найденные журналы:")
        for magazine in magazines:
            print(f"ID: {magazine[0]}, Название: {magazine[1]}, Описание: {magazine[2]}")
    else:
        print("Журнал не найден.")
    cursor.close()


def edit_magazine(con):
    title = input('Введите название журнала для редактирования: ').strip()

    cursor = con.cursor()
    cursor.execute(f'''SELECT id, title, description FROM magazines WHERE title = '{title}' ''')
    magazine = cursor.fetchone()

    if magazine:
        print(f"Найден журнал: ID: {magazine[0]}, Название: {magazine[1]}, Описание: {magazine[2]}")

        new_title = input(f"Введите новое название журнала (оставьте пустым если не хотите менять): ").strip()
        new_description = input(f"Введите новое описание журнала (оставьте пустым если не хотите менять): ").strip()

        if new_title:
            cursor.execute(f'''UPDATE magazines SET title = '{new_title}' WHERE id = {magazine[0]}''')
        if new_description:
            cursor.execute(f'''UPDATE magazines SET description = '{new_description}' WHERE id = {magazine[0]}''')

        con.commit()
        print("Данные журнала успешно обновлены.")
    else:
        print("Журнал не найден.")

    cursor.close()


def delete_magazine(con):
    title = input('Введите название журнала для удаления: ').strip()

    cursor = con.cursor()
    cursor.execute(f'''SELECT id FROM magazines WHERE title = '{title}' ''')
    magazine = cursor.fetchone()

    if magazine:
        cursor.execute(f'''DELETE FROM magazines WHERE id = {magazine[0]}''')
        con.commit()
        print("Журнал успешно удален.")
    else:
        print("Журнал не найден.")

    cursor.close()
