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
        temp_dishes = {}

        with open(data_path, encoding="utf-8") as file:
            for row in DictReader(file):
                dish_key = (row["dish"], float(row["price"]))

                if dish_key not in temp_dishes:
                    dish = Dish(row["dish"], float(row["price"]))
                    temp_dishes[dish_key] = dish
                    self.dishes.add(dish)
                else:
                    dish = temp_dishes[dish_key]

                dish.add_ingredient_dependency(
                    Ingredient(row["ingredient"]),
                    int(row["recipe_amount"]),
                )
