from models.ingredient import Ingredient
from models.dish import Dish
from csv import DictReader

DATA_PATH = "data/menu_base_data.csv"


class MenuData:
    def __init__(self, data_path=DATA_PATH) -> None:
        self.dishes = set()
        self.read_csv_menu(data_path)

    def __iter__(self):
        return iter(self.dishes)

    def __str__(self) -> str:
        return f"{self.dishes}"

    def read_csv_menu(self, data_path=DATA_PATH) -> None:
        with open(data_path, encoding="utf-8") as file:
            for row in DictReader(file):
                dish = Dish(row["dish"], float(row["price"]))
                self.dishes.add(dish)

                for dish in self.dishes:
                    if dish == Dish(row["dish"], float(row["price"])):
                        dish.add_ingredient_dependency(
                            Ingredient(row["ingredient"]),
                            int(row["recipe_amount"]),
                        )
