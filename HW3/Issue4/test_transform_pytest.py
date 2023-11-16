import pytest
from fit_transform import fit_transform


def test_unique_categories():
    result = fit_transform("cat", "dog", "fish")
    expected = [("cat", [0, 0, 1]), ("dog", [0, 1, 0]), ("fish", [1, 0, 0])]
    assert result == expected


def test_duplicate_categories():
    result = fit_transform("cat", "dog", "cat")
    expected = [("cat", [0, 1]), ("dog", [1, 0]), ("cat", [0, 1])]
    assert result == expected


def test_no_arguments():
    with pytest.raises(TypeError):
        fit_transform()


def test_category_order():
    result = fit_transform("cat", "dog", "bird", "dog", "cat", "cat")
    expected_order = ["cat", "dog", "bird"]
    categories_order = [x[0] for x in result][:3]
    assert expected_order == categories_order
