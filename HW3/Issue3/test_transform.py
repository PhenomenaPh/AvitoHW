import unittest

from fit_transform import fit_transform


class TestFitTransform(unittest.TestCase):
    def test_unique_categories(self):
        """Проверка, что функция корректно обрабатывает уникальные категории"""
        result = fit_transform("cat", "dog", "fish")
        expected = [
            ("cat", [0, 0, 1]),
            ("dog", [0, 1, 0]),
            ("fish", [1, 0, 0]),
        ]
        self.assertEqual(result, expected)

    def test_unseen_category(self):
        """Проверка, что в результате нет неизвестных категорий"""
        result = fit_transform("cat", "dog")
        self.assertNotIn(("fish", [0, 0, 1]), result)
        self.assertNotIn(("bird", [0, 1, 0]), result)

    def test_duplicate_categories(self):
        """Обработка повторяющихся категорий"""
        result = fit_transform("cat", "dog", "cat")
        expected = [("cat", [0, 1]), ("dog", [1, 0]), ("cat", [0, 1])]
        self.assertEqual(result, expected)

    def test_empty_input(self):
        """Проверка вызова исключения при отсутствии аргументов"""
        with self.assertRaises(TypeError):
            fit_transform()

    def test_category_order(self):
        """Проверка порядока бинарных представлений"""
        result = fit_transform("cat", "dog", "bird", "dog", "cat", "cat")
        expected_order = ["cat", "dog", "bird"]
        categories_order = [x[0] for x in result]
        self.assertEqual(expected_order, categories_order[:3])


if __name__ == "__main__":
    unittest.main()
