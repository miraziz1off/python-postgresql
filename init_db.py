def init_db(con):
    cursor = con.cursor()

    try:
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(150) UNIQUE NOT NULL
                );
            """)

        cursor.execute("""
                CREATE TABLE IF NOT EXISTS magazines (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(150) UNIQUE NOT NULL,
                    description TEXT
                );
            """)

        cursor.execute("""
                CREATE TABLE IF NOT EXISTS subscriptions (
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
                    magazine_id INTEGER REFERENCES magazines(id) ON DELETE CASCADE,
                    UNIQUE (user_id, magazine_id)
                );
            """)
        con.commit()
        print('База данных успешно создана')

    except Exception as e:
        con.rollback()
        print(f'Ошибка: {e}')

    finally:
        cursor.close()