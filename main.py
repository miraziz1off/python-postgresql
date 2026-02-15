from connection import connect_to_db
from init_db import init_db
from user import create_user, search_user_by_email
from magazine import create_magazine, search_magazine_by_title, get_info
from subs import subscribe_user, unsubscribe_user

def main():
    connection = connect_to_db()
    if not connection:
        return

    init_db(connection)

    while True:
        print("\n--- МЕНЮ УПРАВЛЕНИЯ ЖУРНАЛАМИ ---")
        print("1. Добавить пользователя")
        print("2. Добавить журнал")
        print("3. Подписать пользователя на журнал")
        print('4. Отвязать пользователя от журнала')
        print("5. Поиск пользователей по email")
        print("6. Поиск журналов по названию")
        print("7. Получить информацию о всём")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == '1':
            create_user(connection)
        elif choice == '2':
            create_magazine(connection)
        elif choice == '3':
            subscribe_user(connection)
        elif choice == '4':
            unsubscribe_user(connection)
        elif choice == '5':
            search_user_by_email(connection)
        elif choice == '6':
            search_magazine_by_title(connection)
        elif choice == '7':
            get_info(connection)
        elif choice == '0':
            connection.close()
            print("Соединение закрыто. Пока!")
            break
        else:
            print("Неверный ввод, попробуйте снова.")


if __name__ == "__main__":
    main()
