# ЭТОТ КОД БЫЛ СГЕНЕРИРОВАН ИИ ДЛЯ ЗАПОЛНЕНИЕ ДАННЫХ


from connection import connect_to_db


def seed_data():
    con = connect_to_db()
    if not con: return

    cursor = con.cursor()
    try:
        # Добавляем пользователей
        users = [
            ('Ivan', 'ivan@example.com'),
            ('Maria', 'maria@example.com'),
            ('Petr', 'petr@example.com')
        ]
        cursor.executemany("INSERT INTO users (name, email) VALUES (%s, %s) ON CONFLICT DO NOTHING", users)

        # Добавляем журналы
        magazines = [
            ('National Geographic', 'Природа и наука'),
            ('Vogue', 'Мода и стиль'),
            ('PC Gamer', 'Игры и железо')
        ]
        cursor.executemany("INSERT INTO magazines (title, description) VALUES (%s, %s) ON CONFLICT DO NOTHING",
                           magazines)

        con.commit()
        print("Тестовые данные успешно добавлены!")
    except Exception as e:
        con.rollback()
        print(f"Ошибка при заполнении: {e}")
    finally:
        cursor.close()
        con.close()


if __name__ == "__main__":
    seed_data()