# Базовий клас "Туристичний маршрут"
class TourRoute:
    def __init__(self, name, country, duration, difficulty):
        self.name = name
        self.country = country
        self.duration = duration
        self.difficulty = difficulty

    def set_properties(self, name, country, duration, difficulty):
        self.name = name
        self.country = country
        self.duration = duration
        self.difficulty = difficulty

    def get_properties(self):
        return f"Маршрут: {self.name}, Країна: {self.country}, Тривалість: {self.duration} днів, Складність: {self.difficulty}"

# Похідний клас "Екстремальний маршрут" без super()
class ExtremeRoute(TourRoute):
    def __init__(self, name, country, duration, difficulty, obstacles):
        # Ручне викликання конструктора базового класу
        self.name = name
        self.country = country
        self.duration = duration
        self.difficulty = difficulty
        self.obstacles = obstacles

    def set_obstacles(self, obstacles):
        self.obstacles = obstacles

    def get_obstacles(self):
        return self.obstacles

    def calculate_cost(self):
        # Вартість маршруту залежить від тривалості, складності та кількості перешкод
        base_cost = 100 * self.duration
        difficulty_factor = {"легкий": 1, "середній": 1.5, "важкий": 2}.get(self.difficulty, 1)
        obstacle_cost = 50 * self.obstacles
        return base_cost * difficulty_factor + obstacle_cost

# Приклад використання
extreme_route = ExtremeRoute("Гімалаї", "Непал", 10, "важкий", 5)
print(extreme_route.get_properties())
print(f"Кількість перешкод: {extreme_route.get_obstacles()}")
print(f"Вартість екстремального маршруту: {extreme_route.calculate_cost()} грн")
