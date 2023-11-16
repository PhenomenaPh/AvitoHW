import functools
import time
from typing import List

import click


# Декоратор для логирования
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} — {end_time - start_time:.2f}с!")
        return result

    return wrapper


# Декоратор с шаблоном
def log_with_template(template):
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
    def __init__(self, size: str) -> None:
        if size not in ["L", "XL"]:
            raise ValueError(f"Invalid pizza size: {size}")
        self.size = size
        self.base_price = 5 if size == "L" else 15 if size == "XL" else 0
        self.ingredients: List[str] = []

    def add_ingredients(self, ingredients: str) -> None:
        self.ingredients.append(ingredients)

    def calculate_price(self) -> int:
        return self.base_price + len(self.ingredients) * 3

    def __str__(self) -> str:
        ingredients_str = ", ".join(self.ingredients)
        return f"{self.size} pizza with {ingredients_str} - ${self.calculate_price()}"


class Margherita(Pizza):
    def __init__(self, size: str) -> None:
        super().__init__(size)
        self.add_ingredients("Tomato Sauce")
        self.add_ingredients("Mozzarella")
        self.add_ingredients("Basil")


class Hawaiian(Pizza):
    def __init__(self, size: str) -> None:
        super().__init__(size)
        self.add_ingredients("Tomato Sauce")
        self.add_ingredients("Mozzarella")
        self.add_ingredients("Ham")
        self.add_ingredients("Pineapple")


class Pepperoni(Pizza):
    def __init__(self, size: str):
        super().__init__(size)
        self.add_ingredients("Tomato Sauce")
        self.add_ingredients("Mozzarella")
        self.add_ingredients("Pepperoni")


def order():
    print("Welcome to our Pizza Ordering System!")
    pizza_type = input("Choose a pizza (Margherita, Hawaiian, Pepperoni): ")
    size = input("Choose the size (L/XL): ")

    if pizza_type not in [
        "Margherita",
        "Hawaiian",
        "Pepperoni",
    ] or size not in ["L", "XL"]:
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
    pass


@cli.command()
@log
def menu():
    """Display the pizza menu."""
    time.sleep(1)  # Имитация задержки
    print("Menu:\n1. Margherita\n2. Hawaiian\n3. Pepperoni")


@cli.command()
@log_with_template(" Заказ выполнен за {:.2f}с!")
def make_order():
    """Order a pizza."""
    order()


if __name__ == "__main__":
    cli()
