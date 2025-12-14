# vehicle.py
import uuid
from transport.client import Client

class Vehicle:
    def __init__(self, capacity: float):
        # Генерация уникального идентификатора
        self.vehicle_id = str(uuid.uuid4())
        
        # Валидация грузоподъемности
        if not isinstance(capacity, (int, float)) or capacity <= 0:
            raise ValueError("Грузоподъемность должна быть положительным числом.")
        
        self.capacity = float(capacity)
        self.current_load = 0.0
        self.clients_list = []

    def load_cargo(self, client: Client):
        """Загрузить груз клиента в транспорт"""
        # Проверка типа
        if not isinstance(client, Client):
            raise TypeError("Аргумент должен быть объектом класса Client.")
        
        # Проверка вместимости
        if self.current_load + client.cargo_weight > self.capacity:
            raise ValueError("Превышение грузоподъемности транспорта.")
        
        # Добавляем груз
        self.current_load += client.cargo_weight
        self.clients_list.append(client)

    def __str__(self):
        return (f"Транспорт ID: {self.vehicle_id}\n"
                f"Грузоподъемность: {self.capacity} тонн\n"
                f"Текущая загрузка: {self.current_load} тонн\n"
                f"Клиентов загружено: {len(self.clients_list)}")
