# Реалізація багаторівневого наслідування на Python

# Базовий клас "Рослина"
class Plant:
    def __init__(self, plant_type):
        self.plant_type = plant_type

    def get_plant_type(self):
        return f"Тип рослини: {self.plant_type}"

    def grow(self):
        return "Рослина росте."

# Похідний клас "Дерево", що успадковує клас "Рослина"
class Tree(Plant):
    def __init__(self, plant_type, height):
        super().__init__(plant_type)
        self.height = height

    def get_height(self):
        return f"Висота дерева: {self.height} метрів"

# Похідний клас "Плодовите дерево", що успадковує клас "Дерево"
class FruitTree(Tree):
    def __init__(self, plant_type, height, fruit_type):
        super().__init__(plant_type, height)
        self.fruit_type = fruit_type

    def get_fruit_type(self):
        return f"Тип плодів: {self.fruit_type}"

# Створення об'єкту класу "Плодовите дерево"
fruit_tree = FruitTree("Плодовите дерево", 5, "Яблука")

# Виклик методів
plant_type = fruit_tree.get_plant_type()
tree_height = fruit_tree.get_height()
fruit_type = fruit_tree.get_fruit_type()

plant_type, tree_height, fruit_type
