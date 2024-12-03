class Nutrition:
    def __init__(self):
        self.fruits = {
            "Apple": 130,
            "Avocado California": 50,
            "Banana": 110,
            "Cantaloupe": 50,
            "Grapefruit": 60,
            "Grapes": 90,
            "Honeydew Melon": 50,
            "Kiwifruit": 90,
            "Lemon": 15,
            "Lime": 20,
            "Nectarine": 60,
            "Orange": 80,
            "Peach": 60,
            "Pear": 100,
            "Pineapple": 50,
            "Plums": 70,
            "Strwberries": 50,
            "Sweet Cherries": 100,
            "Tangerine": 50,
            "Watermelon": 80
        }
    def no_of_calories(self, fruit: str)-> int:
        """_Given a fruit return the amount of calories in a portion of the fruit_

        Args:
            fruit (str): _Fruit to get calories_

        Returns:
            int: _Number of calories_
        Example:
        >>> no_of_calories("Apple")
            130
        """
        return self.fruits[fruit.title()]
    def main(self)->None:
        fruit = input("Item: ")
        if fruit.title() in self.fruits:
            calories = self.no_of_calories(fruit)
            print(f"Calories: {calories}")
if __name__ == "__main__":
    nutrition = Nutrition()
    nutrition.main()