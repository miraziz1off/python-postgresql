def subscribe_user(con):
    email = input('Введите email: ').strip().lower()

    cursor = con.cursor()
    cursor.execute(f'''SELECT id from users WHERE email='{email}'; ''')

    exist = cursor.fetchone()

    if exist is None:
        print('Пользователь не найден!')
        cursor.close()
        return

    user_id = exist[0]

    title = input('Введите название журнала: ').strip()

    cursor.execute(f''' SELECT id FROM magazines WHERE title='{title}' ''')

    title_exists = cursor.fetchone()

    if title_exists is None:
        print('Журнал не найден!')
        cursor.close()
        return

    magazine_id = title_exists[0]

    cursor.execute(f''' SELECT id FROM subscriptions WHERE user_id={user_id} AND magazine_id={magazine_id}; ''')
    result = cursor.fetchone()

    if result:
        print('уже подписан')
        cursor.close()
        return

    cursor.execute(f''' INSERT INTO subscriptions (user_id, magazine_id) VALUES ({user_id}, {magazine_id}); ''')

    con.commit()
    cursor.close()