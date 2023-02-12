if __name__ == "__main__":
    class Salary:
        def __init__(self, name: str, rate: float, hours: int, salary: float):
            """
            Создание и подготовка к работе класса "Зарплата"
            :param name: Имя сотрудника предприятия
            :param rate: Часовая ставка заработной платы
            :param hours: Количество отработанных часов
            :param salary: Заработная плата сотрудника
            """
            self.name = name
            self.rate = rate
            self.hours = hours
            self.salary = salary

        def head_print(self) -> str:
            """ Метод, распечатывающий заголовок зарплатной ведомости """

        def salary(self) -> float:
            """ Метод, рассчитывающий зарплату работника. """
            self.salary = self.rate * self.hours

        def __str__(self) -> str:
            return f"Сотрудник {self.name} получает зарплату в размере {self.salary}."

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(name={self.name!r}, salary={self.!r})"

    class FutureSalary(Salary):
        def __init__(self, name: str, rate: float, hours: int, salary: float, inflation: float):
            """
            Создание и подготовка к работе класса "Будущая зарплата" для планирования расходов предприятия
            :param inflation: Размер инфляции
            """
            super().__init__(name, rate, hours, salary)
            self.inflation = inflation

        def salary (self) -> float:
            """ Метод, рассчитывающий будущую зарплату работника с учетом инфляции.
                Метод перегружается, так как необходимо учесть новый аргумент (инфляцию)"""
            self.salary = self.rate * self.hours * (1 + self.inflation)

        def __str__(self) -> str:
            return f"Сотрудник {self.name} будет получать зарплату в размере {self.salary}."

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(name={self.name!r}, salary={self.salary!r})"
