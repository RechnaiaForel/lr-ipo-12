#Вариант 2
from transport.client import Client
from transport.ship import Ship
from transport.truck import Truck
from transport.company import TransportCompany

def show_menu():
    print("\n=== МЕНЮ ===")
    print("1. Добавить клиента")
    print("2. Показать всех клиентов")
    print("3. Добавить транспорт (судно или грузовик)")
    print("4. Показать весь транспорт")
    print("5. Запустить оптимизацию распределения грузов")
    print("6. Показать результат распределения")
    print("0. Выход")

def main():
    company = TransportCompany("TransLogistics")

    while True:
        show_menu()
        choice = input("Выберите пункт меню: ")

        if choice == "1":
            name = input("Имя клиента: ")
            try:
                weight = float(input("Вес груза (тонны): "))
                is_vip = input("VIP клиент? (y/n): ").lower() == "y"
                client = Client(name, weight, is_vip)
                company.add_client(client)
                print("✅ Клиент добавлен.")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "2":
            if not company.clients:
                print("Список клиентов пуст.")
            else:
                print("\n--- Клиенты ---")
                for c in company.clients:
                    print(c)

        elif choice == "3":
            transport_type = input("Тип транспорта (ship/truck): ").lower()
            try:
                capacity = float(input("Грузоподъемность (тонны): "))
                if transport_type == "ship":
                    name = input("Название судна: ")
                    ship = Ship(capacity, name)
                    company.add_vehicle(ship)
                    print("✅ Судно добавлено.")
                elif transport_type == "truck":
                    color = input("Цвет грузовика: ")
                    truck = Truck(capacity, color)
                    company.add_vehicle(truck)
                    print("✅ Грузовик добавлен.")
                else:
                    print("Неверный тип транспорта.")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "4":
            if not company.vehicles:
                print("Список транспорта пуст.")
            else:
                print("\n--- Транспорт ---")
                for v in company.vehicles:
                    print(v)

        elif choice == "5":
            company.optimize_cargo_distribution()
            print("✅ Оптимизация завершена.")

        elif choice == "6":
            print("\n--- Результат распределения ---")
            print(company)
            for v in company.vehicles:
                print(v)

        elif choice == "0":
            print("Выход...")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()

