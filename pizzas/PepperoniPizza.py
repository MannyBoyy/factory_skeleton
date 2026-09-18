from ingredient_factories.PizzaIngredientFactory import PizzaIngredientFactory
from pizzas.Pizza import Pizza
# gave us this example for the others as well.
# So here, basically saying "We ARE pepperoni pizza send this to
# the factory". Pizza.py says every pizza MUST implement prepare()
# and we implement it for our own PepperoniPizza


class PepperoniPizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self._ingredient_factory = ingredient_factory

    def prepare(self):
        print(f'preparing: {self._name}')
        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()
        self._pepperoni = self._ingredient_factory.create_pepperoni()
