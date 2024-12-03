import pytest
from nutrition import Nutrition

@pytest.mark.parametrize("fruit, no_calories",[
    ("apple", 130),
    ("avocado california", 50),
    ("banana", 110),
    ("honeydew melon", 50)
 ])
class TestNoOfCaloriesWithLowercase:
    nutrition = Nutrition()
    def test_no_of_calories_with_lowercase_fruit(self, fruit, no_calories):
        assert self.nutrition.no_of_calories(fruit) == no_calories