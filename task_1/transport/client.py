# client.py

class Client:
    def __init__(self, name: str, cargo_weight: float, is_vip: bool = False):
        # Валидация имени
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Имя клиента должно быть непустой строкой.")
        
        # Валидация веса
        if not isinstance(cargo_weight, (int, float)) or cargo_weight <= 0:
            raise ValueError("Вес груза должен быть положительным числом.")
        
        # Валидация VIP-статуса
        if not isinstance(is_vip, bool):
            raise ValueError("VIP-статус должен быть булевым значением (True/False).")
        
        self.name = name.strip()
        self.cargo_weight = float(cargo_weight)
        self.is_vip = is_vip

    def __str__(self):
        vip_status = "VIP" if self.is_vip else "Обычный"
        return f"Клиент: {self.name}, Груз: {self.cargo_weight} кг, Статус: {vip_status}"

    def update_cargo(self, new_weight: float):
        """Обновить вес груза с проверкой"""
        if not isinstance(new_weight, (int, float)) or new_weight <= 0:
            raise ValueError("Вес груза должен быть положительным числом.")
        self.cargo_weight = float(new_weight)

    def set_vip(self, status: bool):
        """Изменить VIP-статус"""
        if not isinstance(status, bool):
            raise ValueError("VIP-статус должен быть булевым значением.")
        self.is_vip = status
