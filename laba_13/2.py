# Базовий клас A
class A:
    def method(self):
        return "Метод класу A"

# Клас B, що наслідується від A
class B(A):
    def method(self):
        return "Метод класу B"

# Клас C, що також наслідується від A
class C(A):
    def method(self):
        return "Метод класу C"

# Клас D, що наслідується від B та C
class D(B, C):
    pass

# Створення об'єкту класу D
d = D()

# Перевірка виклику методу
result_method = d.method()

# Виведення MRO для класу D
mro_tuple = D.__mro__

result_method, mro_tuple
