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
    con.commit()
    cursor.close()