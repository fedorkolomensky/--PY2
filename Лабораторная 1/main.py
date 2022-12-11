import doctest

class Car:
    def __init__(self, fuel_tank_capacity: float, fuel_level: float):
        """
        Создание и подготовка к работе объекта "Автомобиль"
        :param fuel_tank_capacity: Объем топливного бака
        :param fuel_level: Уровень топлива
        Примеры:
        >>> car = Car(45, 0)  #инициализация экземпляра класса
        """
        if not isinstance(fuel_tank_capacity, (int, float)):
            raise TypeError("Объем топливного бака должен быть типа int или float")
        if fuel_tank_capacity <= 0:
            raise TypeError("Объем топливного бака должен быть положительным числом")
        self.fuel_tank_capacity = fuel_tank_capacity

        if not isinstance(fuel_level, (int, float)):
            raise TypeError("Уровень топлива должен быть типа int или float")
        if fuel_level < 0:
            raise TypeError("Уровень топлива не может быть отрицательным числом")
        self.fuel_level = fuel_level

    def is_tank_full(self) -> bool:
        """
        Функция, которая проверяет, является ли топливный бак полным
        :return: Является ли топливный бак полным
        Примеры:
        >>> car = Car(45, 45)
        >>> car.is_tank_full()
        """

    def refuel(self, fuel: float) -> float:
        """
        Функция заправки автомобиля
        :param fuel: Объем заправляемого топлива
        :raise ValueError: Если объем заправляемого топлива превышает свободное место в топливном баке, то вызываем ошибку
        Примеры:
        >>> car = Car(45, 0)
        >>> car.refuel(15)
        """
        if not isinstance(fuel, (int, float)):
            raise TypeError("Объем заправляемого топлива должен быть типа int или float")
        if fuel <= 0:
            raise ValueError("Объем заправляемого топлива должен быть положительным числом")
        ...

class Triangle:
    def __init__(self, a: float, b: float, c: float):
        """
        Создание и подготовка к работе объекта "Треугольник"
        :param a: Длина первой стороны треугольника
        :param b: Длина второй стороны треугольника
        :param c: Длина третьей стороны треугольника
        Примеры:
        >>> triangle = Triangle(5, 6, 7)  #инициализация экземпляра класса
        """
        if not isinstance(a, (int, float)):
            raise TypeError("Длина стороны треугольника должна быть типа int или float")
        if a <= 0:
            raise TypeError("Длина стороны треугольника должна быть положительным числом")
        if a > b + c:
            raise TypeError("Длина стороны треугольника не может быть больше суммы длин двух других сторон")
        self.a = a

        if not isinstance(b, (int, float)):
            raise TypeError("Длина стороны треугольника должна быть типа int или float")
        if b <= 0:
            raise TypeError("Длина стороны треугольника должна быть положительным числом")
        if b > a + c:
            raise TypeError("Длина стороны треугольника не может быть больше суммы длин двух других сторон")
        self.b = b

        if not isinstance(c, (int, float)):
            raise TypeError("Длина стороны треугольника должна быть типа int или float")
        if c <= 0:
            raise TypeError("Длина стороны треугольника должна быть положительным числом")
        if c > a + b:
            raise TypeError("Длина стороны треугольника не может быть больше суммы длин двух других сторон")
        self.c = c

    def triangle_perimiter(self) -> float:
        """
        Функция, которая считает периметр треугольника
        :return: Периметр треугольника
        Примеры:
        >>> triangle = Triangle(5, 6, 7)
        >>> triangle.triangle_perimiter()
        """
        ...

    def triangle_square(self) -> float:
        """
        Функция, которая считает площадь треугольника по формуле Герона
        :return: Площадь треугольника
        Примеры:
        >>> triangle = Triangle(5, 6, 7)
        >>> triangle.triangle_square()
        """
        ...

class Wardrobe:
    def __init__(self, size: int, color: str):
        """
        Создание и подготовка к работе объекта "Гардероб"
        :param size: Размер одежды
        :param color: Цвет одежды
        Примеры:
        >>> wardrobe = Wardrobe(48, "green")  # инициализация экземпляра класса
        """
        if not isinstance(size, int):
            raise TypeError("Размер одежды должен быть целым числом")
        if size <= 0:
            raise TypeError("Размер одежды должен быть положительным числом")
        self.size = size

        if not isinstance(color, str):
            raise TypeError("Цвет должен быть строкой")
        self.color = color

    def is_item_of_size(self) -> bool:
        """
        Функция, которая определяет наличие в гардеробе предмета одежды данного размера
        :return: Предмет одежды
        Примеры:
        >>> wardrobe = Wardrobe(48, "red")
        >>> wardrobe.is_item_of_size()
        """

    def is_item_of_color(self) -> bool:
        """
        Функция, которая определяет наличие в гардеробе предмета одежды данного цвета
        :return: Предмет одежды
        Примеры:
        >>> wardrobe = Wardrobe(50, "purple")
        >>> wardrobe.is_item_of_color()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()  #тестирование примеров, которые находятся в документации
    
