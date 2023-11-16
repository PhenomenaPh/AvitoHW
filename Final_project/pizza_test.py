import pytest
from pizza import Hawaiian, Margherita, Pepperoni, Pizza


# Тестирование создания разных видов пиццы
def test_margherita_creation():
    pizza = Margherita("L")
    assert pizza.size == "L"
    assert "Tomato Sauce" in pizza.ingredients
    assert "Mozzarella" in pizza.ingredients
    assert "Basil" in pizza.ingredients


def test_hawaiian_creation():
    pizza = Hawaiian("XL")
    assert pizza.size == "XL"
    assert "Ham" in pizza.ingredients
    assert "Pineapple" in pizza.ingredients


def test_pepperoni_creation():
    pizza = Pepperoni("L")
    assert "Pepperoni" in pizza.ingredients


# Тестирование расчета цены пиццы
def test_pepperoni_price():
    pizza = Pepperoni("L")
    base_price = 5
    ingredient_price = 3 * len(pizza.ingredients)
    expected_price = base_price + ingredient_price
    assert pizza.calculate_price() == expected_price


# Тестирование добавления дополнительных ингредиентов
def test_add_extra_ingredients():
    pizza = Margherita("L")
    pizza.add_ingredients("Olives")
    pizza.add_ingredients("Mushrooms")
    assert "Olives" in pizza.ingredients
    assert "Mushrooms" in pizza.ingredients


# Тестирование цен для разных размеров пиццы
def test_price_for_different_sizes():
    small_pizza = Margherita("L")
    large_pizza = Margherita("XL")
    assert small_pizza.calculate_price() < large_pizza.calculate_price()


# Тестирование обработки исключений для невалидных размеров пиццы
def test_invalid_pizza_size():
    with pytest.raises(ValueError):
        Pizza("Medium")
