import psycopg2
import json
import os

CONFIG_FILE = "db_config.json"


def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)


def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return None


def connect_to_db():
    config = load_config()

    if config:
        try:
            print("Пробуем подключиться по сохранённым данным...")
            connection = psycopg2.connect(**config)
            print("Подключение успешно (авто)!")
            return connection
        except Exception as e:
            print(f"Ошибка автоподключения: {e}")
            print("Переходим к ручному вводу...\n")

    while True:
        print('Подключение к PostgreSQL')

        host = input("Host (например localhost): ").strip()
        port = input("Port (обычно 5432): ").strip()
        dbname = input("Название бд: ").strip()
        user = input("Username: ").strip()
        password = input("Password: ").strip()

        if not all([host, port, dbname, user, password]):
            print('Все поля должны быть заполнены\n')
            continue

        config = {
            "host": host,
            "port": port,
            "dbname": dbname,
            "user": user,
            "password": password
        }

        try:
            connection = psycopg2.connect(**config)
            print('Подключение успешно!')

            save_config(config)
            print("Данные сохранены в файл db_config.json")

            return connection

        except Exception as e:
            print(f'Ошибка: {e}')
            retry = input('Попробовать еще? (y/n): ').lower()

            if retry != 'y':
                print('Выход')
                break
