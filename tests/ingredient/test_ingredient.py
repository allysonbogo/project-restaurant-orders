from src.models.ingredient import Ingredient, Restriction


def test_ingredient():
    ingredient_1 = Ingredient("bacon")
    ingredient_2 = Ingredient("massa de lasanha")

    assert ingredient_1.name == "bacon"
    assert ingredient_2.name == "massa de lasanha"

    assert ingredient_1.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }

    assert ingredient_2.restrictions == {
        Restriction.GLUTEN,
        Restriction.LACTOSE,
    }

    assert hash(ingredient_1) == hash("bacon")
    assert hash(ingredient_2) == hash("massa de lasanha")

    assert ingredient_1.__eq__(ingredient_1) is True
    assert ingredient_1.__eq__(ingredient_2) is False
    assert ingredient_1 == ingredient_1
    assert ingredient_1 != ingredient_2

    assert repr(ingredient_1) == "Ingredient('bacon')"
    assert repr(ingredient_2) == "Ingredient('massa de lasanha')"
