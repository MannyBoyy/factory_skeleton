from PizzaStores.PizzaStore import PizzaStore
from ingredient_factories.ChicagoPizzaIngredientFactory import (
    ChicagoPizzaIngredientFactory)
from pizzas.PizzaType import PizzaType
from pizzas.CheesePizza import CheesePizza
from pizzas.PepperoniPizza import PepperoniPizza
from pizzas.ClamPizza import ClamPizza
from pizzas.VeggiePizza import VeggiePizza

# this is where the region is being decided
# we send this to the Factories
# here we use the rule with the names between the Pizza.py


class ChicagoStylePizzaStore(PizzaStore):
    # basically asking what pizza wants to be created
    def create_pizza(self, pizza_type: PizzaType):
        ingredient_factory = ChicagoPizzaIngredientFactory()

        if pizza_type == PizzaType.CHEESE:
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name("Chicago Style Cheese Pizza")
            return pizza

        elif pizza_type == PizzaType.PEPPERONI:
            pizza = PepperoniPizza(ingredient_factory)
            pizza.set_name("Chicago Style Pepperoni Pizza")
            return pizza

        elif pizza_type == PizzaType.CLAM:
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name("Chicago Style Clam Pizza")
            return pizza

        elif pizza_type == PizzaType.VEGGIE:
            pizza = VeggiePizza(ingredient_factory)
            pizza.set_name("Chicago Style Veggie Pizza")
            return pizza
