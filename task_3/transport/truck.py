# transport/truck.py
from transport.vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, capacity: float, color: str):
        super().__init__(capacity)
        if not isinstance(color, str) or not color.strip():
            raise ValueError("Цвет грузовика должен быть непустой строкой.")
        self.color = color.strip()

    def __str__(self):
        return (f"Грузовик {self.color} | ID: {self.vehicle_id} | "
                f"Грузоподъемность: {self.capacity} т | "
                f"Текущая загрузка: {self.current_load} т")
