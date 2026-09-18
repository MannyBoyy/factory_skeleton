from PizzaStores.PizzaStore import PizzaStore
from ingredient_factories.NYPizzaIngredientFactory import (
    NYPizzaIngredientFactory)
from pizzas.PizzaType import PizzaType
from pizzas.CheesePizza import CheesePizza
from pizzas.PepperoniPizza import PepperoniPizza
from pizzas.ClamPizza import ClamPizza
from pizzas.VeggiePizza import VeggiePizza

# this is where the region is being decided
# we send this to the Factories


class NYStylePizzaStore(PizzaStore):
    # basically asking whatpizza wants to be created
    def create_pizza(self, pizza_type: PizzaType):
        ingredient_factory = NYPizzaIngredientFactory()

        if pizza_type == PizzaType.CHEESE:
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name("New York Style Cheese Pizza")
            return pizza

        elif pizza_type == PizzaType.PEPPERONI:
            pizza = PepperoniPizza(ingredient_factory)
            pizza.set_name("New York Style Pepperoni Pizza")
            return pizza

        elif pizza_type == PizzaType.CLAM:
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name("New York Style Clam Pizza")
            return pizza

        elif pizza_type == PizzaType.VEGGIE:
            pizza = VeggiePizza(ingredient_factory)
            pizza.set_name("New York Style Veggie Pizza")
            return pizza
