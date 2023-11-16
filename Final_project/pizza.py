import functools
import time
from typing import List

import click


def log(func):
    """Декоратор для логирования времени выполнения функции."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} — {end_time - start_time:.2f}с!")
        return result

    return wrapper


def log_with_template(template):
    """Декоратор для логирования с форматированным сообщением."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(template.format(end_time - start_time))
            return result

        return wrapper

    return decorator


class Pizza:
    """Базовый класс для всех видов пиццы.

    Атрибуты:
        size (str): Размер пиццы.
        base_price (int): Базовая цена.
        ingredients (List[str]): Список ингредиентов.
    """

    def __init__(self, size: str) -> None:
        if size not in ["L", "XL"]:
            raise ValueError(f"Invalid pizza size: {size}")
        self.size = size
        self.base_price = 5 if size == "L" else 15 if size == "XL" else 0
        self.ingredients: List[str] = []

    def add_ingredients(self, ingredient: str) -> None:
        """Добавляет ингредиент к пицце."""
        self.ingredients.append(ingredient)

    def calculate_price(self) -> int:
        """Рассчитывает и возвращает общую цену пиццы."""
        return self.base_price + len(self.ingredients) * 3


class Margherita(Pizza):
    """Пицца Маргарита, подкласс Pizza."""

    def __init__(self, size: str) -> None:
        super().__init__(size)
        self.add_ingredients("Tomato Sauce")
        self.add_ingredients("Mozzarella")
        self.add_ingredients("Basil")


class Hawaiian(Pizza):
    """Пицца Гавайская, подкласс Pizza."""

    def __init__(self, size: str) -> None:
        super().__init__(size)
        self.add_ingredients("Tomato Sauce")
        self.add_ingredients("Mozzarella")
        self.add_ingredients("Ham")
        self.add_ingredients("Pineapple")


class Pepperoni(Pizza):
    """Пицца Пепперони, подкласс Pizza."""

    def __init__(self, size: str):
        super().__init__(size)
        self.add_ingredients("Tomato Sauce")
        self.add_ingredients("Mozzarella")
        self.add_ingredients("Pepperoni")


def order():
    """Запускает процесс заказа пиццы."""
    print("Welcome to our Pizza Ordering System!")
    pizza_type = input("Choose a pizza (Margherita, Hawaiian, Pepperoni): ")
    size = input("Choose the size (L/XL): ")

    if pizza_type not in ["Margherita", "Hawaiian", "Pepperoni"] or size not in ["L", "XL"]:
        print("Invalid selection. Please try again.")
        return

    if pizza_type == "Margherita":
        pizza = Margherita(size)
    elif pizza_type == "Hawaiian":
        pizza = Hawaiian(size)
    else:
        pizza = Pepperoni(size)

    extra = input("Add extra ingredient (yes/no)? ")
    while extra.lower() == "yes":
        ingredient = input("Enter ingredient to add: ")
        pizza.add_ingredients(ingredient)
        extra = input("Add another ingredient (yes/no)? ")

    print("Your order is complete.")
    print(pizza)


@click.group()
def cli():
    """CLI для управления системой заказа пиццы."""
    pass


@cli.command()
@log
def menu():
    """Отображает меню доступных пицц."""
    print("Menu:\n1. Margherita\n2. Hawaiian\n3. Pepperoni")


@cli.command()
@log_with_template(" Заказ выполнен за {:.2f}с!")
def make_order():
    """Обрабатывает создание заказа пиццы через CLI."""
    order()


if __name__ == "__main__":
    cli()
