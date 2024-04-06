import requests
from colorama import init
init()
from colorama import Fore
print(Fore.CYAN + "Программа разработана discplus.")
print("Ссылка на GitHub: https://github.com/discplus")
print("Ссылка на файл: https://github.com/discplus/FunBoostApi")
print()
print()
print()


def authenticate_user():
    user_login = input("Введите ваш логин: ")
    with open("baza.txt", "r") as file:
        for line in file:
            login, key, service = line.strip().split(" : ")  
            if login == user_login:
                return key, service
    return None, None

key, service = authenticate_user()

if key is None or service is None:
    print("Вы ввели неправильный логин.")
    exit(1)

for x in range(30):
  print()
print("Выберите действие:\n1 - посмотреть все сервисы\n2 - посмотреть баланс\n3 - заказать накрутку\n4 - узнать статус заказа\n5 - сделать рефил\n6 - отменить заказ\n7 - выход")
print()

while True:
    action = int(input("Выбирете действие: "))
    if action == 1:
        response = requests.get(f"{service}/api/v2?action=services&key={key}")
        data = response.json()
        print()
        for item in data:
            print(f"Название: {item['name']}")
            print(f"Id: {item['service']}")
            print(f"Цена: {item['rate']}")
            if item['type'] == "like":
                print("Тип: лайки")
            elif item['type'] == "subscribe":
                print("Тип: подписчики")
            elif item['type'] == "comment":
                print("Тип: комментарии")
            elif item['type'] == "like_to_comment":
                print("Тип: лайки и комментарии")
            elif item['type'] == "dislike":
                print("Тип: дизлайки")
            elif item['type'] == "dislike_to_comment":
                print("Тип: дизлайки и комментарии")
            elif item['type'] == "repost":
                print("Тип: репосты")
            elif item['type'] == "friend":
                print("Тип: друзья")
            elif item['type'] == "vote":
                print("Тип: голоса")
            elif item['type'] == "retweet":
                print("Тип: ретвиты")
            elif item['type'] == "follow":
                print("Тип: подписчики")
            elif item['type'] == "favorite":
                print("Тип: добавление в избранное")
            else:
                print("Ошибка при получении данных")
            print(f"Описание: {item['category']}")
            print(f"Минимальное количество для заказа: {item['min']}")
            print(f"Максимальное количество для заказа: {item['max']}")
            if item['refill'] == "True":
                print("Доступен ли рефилл заказа: да")
            elif item['refill'] == "False":
                print(f"Доступна ли отмена заказа: {item['cancel']}")
            else:
                print("Ошибка при получении данных")
            print()
            print()

    if action == 2:
        response = requests.get(f"{service}/api/v2?action=balance&key={key}")
        data = response.json()
        print()
        print(f"Ваш баланс: {data['balance']} {data['currency']}")
        print()

    if action == 3:
        id = int(input("Введите id сервиса: "))
        link = input("Введите ссылку на место накрутки: ")
        quantity = int(input("Введите количество накрутки: "))
        response = requests.get(f"{service}/api/v2?action=add&service={id}&link={link}&quantity={quantity}&key={key}")
        data = response.json()
        print()
        print(f"Id заказа: {data['order']}")
        print("Пожайлуста, сохраните его до оканчания накрутки.")
        print()

    elif action == 4:
        id = int(input("Введите id заказа: "))
        response = requests.get(f"{service}/api/v2?action=status&order={id}&key={key}")
        data = response.json()

        print()
        print(f"Потрачено на заказ: {data['charge']}{data['currency']}")
        print(f"Количество перед выполнением заказа: {data['start_count']}")
        if data['status'] == "In progress":
            print("Статус заказа: выполнение")
        elif data['status'] == "Comleted":
            print("Статус заказа: выполнен")
        elif data['status'] == "Awaiting":
            print("Статус заказа: ожидает начала выполнения")
        elif data['status'] == "Canceled":
            print("Статус заказа: отменен")
        elif data['status'] == "Fail":
            print("Статус заказа: ошибка")
        elif data['status'] == "Partial":
            print("Статус заказа: частично выполнен")
        print(f"Осталось до выполнения: {data['remains']}")
        print()

    elif action == 5:
        response = requests.get(f"{service}/api/v2?action=refill&order={id}&key={key}")
        id = int(input("Введите id заказа: "))
        data = response.json()
        
        if 'error' in data:
            print()
            print(f"Ошибка: {data['error']}")
            print()
        elif 'refill' in data:
            print()
            print(f"Заявка на рефилл успешно отправлена!")
            print()
        else:
            print()
            print("Не удалось определить статус рефилла.")
            print()


    elif action == 6:
        id = int(input("Введите id заказа: "))
        response = requests.get(f"https://vexboost.ru/api/v2?action=cancel&order={id}&key={key}")
        data = response.json()
        print()

        if 'error' in data:
            print(f"Ошибка: {data['error']}")
            print()
        elif 'ok' in data:
            print(f"Заявка на отмену успешно отправлена!")
            print()
        else:
            print("Не удалось определить статус отмены заказа.")
            print()

    elif action == 7:
        print()
        print("Выход из программы.")
        break