from connection import connect_to_db
from init_db import init_db
from user import create_user, search_user_by_email, edit_user, delete_user
from magazine import create_magazine, edit_magazine, delete_magazine, search_magazine_by_title, get_info
from subs import subscribe_user, unsubscribe_user

def main():
    connection = connect_to_db()
    if not connection:
        return

    init_db(connection)

    actions = {
        '1': create_user,
        '2': create_magazine,
        '3': subscribe_user,
        '4': unsubscribe_user,
        '5': search_user_by_email,
        '6': search_magazine_by_title,
        '7': get_info,
        '8': edit_user,
        '9': edit_magazine,
        '10': delete_user,
        '11': delete_magazine
    }

    while True:
        print("\n--- МЕНЮ УПРАВЛЕНИЯ ЖУРНАЛАМИ ---")
        print("1. Добавить пользователя")
        print("2. Добавить журнал")
        print("3. Подписать пользователя на журнал")
        print("4. Отвязать пользователя от журнала")
        print("5. Поиск пользователей по email")
        print("6. Поиск журналов по названию")
        print("7. Получить информацию о всём")
        print("8. Редактировать данные пользователя")
        print("9. Редактировать данные журнала")
        print("10. Удалить пользователя")
        print("11. Удалить журнал")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == '0':
            connection.close()
            print("Соединение закрыто. Пока!")
            break

        action = actions.get(choice)
        if action:
            action(connection)
        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()
