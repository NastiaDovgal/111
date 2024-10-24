# Базовий клас Vehicle
class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

    def move(self):
        return "Vehicle is moving"

# Клас Car, що наслідується від Vehicle
class Car(Vehicle):
    def __init__(self, wheels, fuel):
        super().__init__(wheels)
        self.fuel = fuel

    def fuel_type(self):
        return f"Fuel type: {self.fuel}"

# Клас Electric
class Electric:
    def charge(self):
        return "Battery charging"

# Клас ElectricCar, що наслідується від Car та Electric (множинне наслідування)
class ElectricCar(Car, Electric):
    def __init__(self, wheels):
        # Ініціалізація класу Car (у ElectricCar немає палива, лише електрика)
        super().__init__(wheels, fuel="Electric power")

    # Перевизначення методу fuel_type для електрокара
    def fuel_type(self):
        return "Fuel type: Electric power"

# Створення об'єкта класу ElectricCar
electric_car = ElectricCar(4)

# Створення об'єкта класу Car
car = Car(4, "Petrol")

# Виклик методів для об'єкта класу ElectricCar
electric_car_move = electric_car.move()
electric_car_fuel_type = electric_car.fuel_type()
electric_car_charge = electric_car.charge()

# Виклик методів для об'єкта класу Car
car_move = car.move()
car_fuel_type = car.fuel_type()

electric_car_move, electric_car_fuel_type, electric_car_charge, car_move, car_fuel_type
