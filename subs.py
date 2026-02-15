def subscribe_user(con):
    email = input('Введите email: ').strip().lower()

    cursor = con.cursor()

    cursor.execute(f'''SELECT id FROM users WHERE email='{email}'; ''')
    user = cursor.fetchone()

    if user is None:
        print('Пользователь не найден!')
        cursor.close()
        return

    user_id = user[0]

    cursor.execute("SELECT id, title FROM magazines;")
    magazines = cursor.fetchall()

    if not magazines:
        print("Нет доступных журналов.")
        cursor.close()
        return

    print("Доступные журналы:")
    for i, magazine in enumerate(magazines, 1):
        print(f"{i}. {magazine[1]}")

    magazine_choice = input('Введите номер журнала, на который хотите подписаться: ').strip()

    try:
        magazine_choice = int(magazine_choice)
        if magazine_choice < 1 or magazine_choice > len(magazines):
            print("Неверный выбор журнала.")
            cursor.close()
            return
    except ValueError:
        print("Введите корректный номер.")
        cursor.close()
        return

    magazine_id = magazines[magazine_choice - 1][0]

    cursor.execute(f'''SELECT id FROM subscriptions WHERE user_id={user_id} AND magazine_id={magazine_id};''')
    result = cursor.fetchone()

    if result:
        print('Пользователь уже подписан на этот журнал.')
    else:
        cursor.execute(f'''INSERT INTO subscriptions (user_id, magazine_id) VALUES ({user_id}, {magazine_id});''')
        con.commit()
        print(f'Пользователь успешно подписан на журнал {magazines[magazine_choice - 1][1]}.')

    cursor.close()


def unsubscribe_user(con):
    email = input('Введите email пользователя: ').lower().strip()
    cursor = con.cursor()

    cursor.execute(f'''SELECT id FROM users WHERE email='{email}'; ''')
    user_id = cursor.fetchone()

    if user_id is None:
        print('Пользователь не найден!')
        cursor.close()
        return

    user_id = user_id[0]

    cursor.execute(f'''SELECT m.id, m.title FROM magazines m
                        JOIN subscriptions s ON m.id = s.magazine_id
                        WHERE s.user_id = {user_id};''')
    subscriptions = cursor.fetchall()

    if not subscriptions:
        print('Пользователь не подписан ни на один журнал.')
        cursor.close()
        return

    print("Журналы, на которые вы подписаны:")
    for i, subscription in enumerate(subscriptions, 1):
        print(f"{i}. {subscription[1]} (ID: {subscription[0]})")

    magazine_choice = input('Введите номер журнала, от которого хотите отписаться: ').strip()

    try:
        magazine_choice = int(magazine_choice)
        if magazine_choice < 1 or magazine_choice > len(subscriptions):
            print("Неверный выбор журнала.")
            cursor.close()
            return
    except ValueError:
        print("Введите корректный номер.")
        cursor.close()
        return

    magazine_id = subscriptions[magazine_choice - 1][0]

    cursor.execute(f'''SELECT id FROM subscriptions WHERE user_id={user_id} AND magazine_id={magazine_id}; ''')
    delete_id = cursor.fetchone()

    if delete_id is None:
        print(f'Пользователь не подписан на журнал с ID {magazine_id}!')
        cursor.close()
        return

    delete_id = delete_id[0]
    cursor.execute(f'''DELETE FROM subscriptions WHERE id={delete_id}; ''')
    print(f'Пользователь успешно отписан от журнала с ID {magazine_id}!')
    con.commit()
    cursor.close()