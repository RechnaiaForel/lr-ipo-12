# main.py
from transport.client import Client

def main():
    # Создание клиента
    client1 = Client("Иван", 120.5)
    print(client1)

    # Обновление груза
    client1.update_cargo(200)
    print(client1)

    # Установка VIP-статуса
    client1.set_vip(True)
    print(client1)

if __name__ == "__main__":
    main()