# transport/ship.py
from transport.vehicle import Vehicle

class Ship(Vehicle):
    def __init__(self, capacity: float, name: str):
        super().__init__(capacity)
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Название судна должно быть непустой строкой.")
        self.name = name.strip()

    def __str__(self):
        return (f"Судно '{self.name}' | ID: {self.vehicle_id} | "
                f"Грузоподъемность: {self.capacity} т | "
                f"Текущая загрузка: {self.current_load} т")
