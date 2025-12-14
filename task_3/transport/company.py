# transport/company.py
from transport.client import Client
from transport.vehicle import Vehicle

class TransportCompany:
    def __init__(self, name: str):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Название компании должно быть непустой строкой.")
        self.name = name.strip()
        self.vehicles = []
        self.clients = []

    def add_vehicle(self, vehicle: Vehicle):
        if not isinstance(vehicle, Vehicle):
            raise TypeError("Можно добавлять только объекты класса Vehicle или его наследников.")
        self.vehicles.append(vehicle)

    def list_vehicles(self):
        return [str(v) for v in self.vehicles]

    def add_client(self, client: Client):
        if not isinstance(client, Client):
            raise TypeError("Можно добавлять только объекты класса Client.")
        self.clients.append(client)

    def optimize_cargo_distribution(self):
        """Распределение грузов:
        - VIP клиенты загружаются первыми
        - Используется минимальное количество транспорта
        """
        # Сортировка клиентов: VIP первыми
        sorted_clients = sorted(self.clients, key=lambda c: not c.is_vip)

        # Сортировка транспорта: сначала с наибольшей вместимостью
        sorted_vehicles = sorted(self.vehicles, key=lambda v: v.capacity, reverse=True)

        for client in sorted_clients:
            for vehicle in sorted_vehicles:
                try:
                    vehicle.load_cargo(client)
                    break  # клиент загружен, переходим к следующему
                except ValueError:
                    continue  # пробуем следующий транспорт

    def __str__(self):
        return f"Транспортная компания '{self.name}' | Транспортных средств: {len(self.vehicles)} | Клиентов: {len(self.clients)}"
