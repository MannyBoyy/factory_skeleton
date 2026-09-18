from ingredients.dough.ThinCrustDough import ThinCrustDough
from ingredients.sauce.MarinaraSauce import MarinaraSauce
from ingredients.cheese.ReggianoCheese import ReggianoCheese
from ingredients.veggies.Garlic import Garlic
from ingredients.veggies.Mushroom import Mushroom
from ingredients.veggies.RedPepper import RedPepper
from ingredients.veggies.Onion import Onion
from ingredients.pepperoni.SlicedPepperoni import SlicedPepperoni
from ingredients.clams.FreshClams import FreshClams
from ingredient_factories.PizzaIngredientFactory import PizzaIngredientFactory
# this is why this is a factory this NYPizzaingredientsFactory holds
# all the ingredients that THIS region uses. This is sending
# to the PizzaStore the info that is needed for NY pizza
# and so with the Chicago one as well


class NYPizzaIngredientFactory(PizzaIngredientFactory):

    def create_dough(self):
        return ThinCrustDough()

    def create_sauce(self):
        return MarinaraSauce()

    def create_cheese(self):
        return ReggianoCheese()

    def create_veggies(self):
        return [Garlic(), Onion(), Mushroom(), RedPepper()]

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clams(self):
        return FreshClams()
