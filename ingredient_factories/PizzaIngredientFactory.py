from abc import ABC, abstractmethod
# main abstraction that holds onto the ingredients
# and pizza making. Here is the most biggest changes that happen


class PizzaIngredientFactory(ABC):

    @abstractmethod
    def create_dough(self):
        pass

    @abstractmethod
    def create_sauce(self):
        pass

    @abstractmethod
    def create_cheese(self):
        pass

    @abstractmethod
    def create_veggies(self):
        pass

    @abstractmethod
    def create_pepperoni(self):
        pass

    @abstractmethod
    def create_clams(self):
        pass
