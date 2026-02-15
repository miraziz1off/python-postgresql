import psycopg2

def connect_to_db():
    while True:
        print('Подключение к PostgreSQL')

        host = input("Host (например localhost): ").strip()
        port = input("Port (обычно 5432): ").strip()
        dbname = input("Название бд: ").strip()
        user = input("Username: ").strip()
        password = input("Password: ").strip()

        if not all([host, port, dbname, user,password]):
            print('Все поля должны быть заполнены')
            continue

        try:
            connection = psycopg2.connect(
                host=host,
                port=port,
                dbname=dbname,
                user=user,
                password=password
            )
            print('Подключение Успешно!')
            return connection
        except Exception as e:
            print(f'Ошибка: {e}')

            retry = input('Попробовать еще? (y/n): ').lower()

            if retry != 'y':
                print('Выход')
                break
