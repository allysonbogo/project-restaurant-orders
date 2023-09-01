from models.ingredient import Ingredient
from models.dish import Dish
import csv


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.load(source_path)

    def __iter__(self):
        return iter(self.dishes)

    def __str__(self) -> str:
        return f"{self.dishes}"

    def load(self, source_path: str) -> None:
        with open(source_path, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                dish = Dish(row[0], float(row[1]))
                self.dishes.add(dish)

                for dish in self.dishes:
                    if dish == Dish(row[0], float(row[1])):
                        dish.add_ingredient_dependency(
                            Ingredient(row[2]), int(row[3])
                        )
