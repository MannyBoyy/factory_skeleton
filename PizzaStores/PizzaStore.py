from abc import ABC, abstractmethod
# to understand: Customer order pizza -> PizzaStore.order_pizza() ->
# Either NY/Chicago create_pizza() -> Chose which PizzaType and ingredients ->
# Pizza.prepare() -> as factory for ingredients -> Ny/chicago ingredients ->
# then we bake cut and box

class PizzaStore(ABC):

    def order_pizza(self, pizza_type):
        pizza = self.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    @abstractmethod
    def create_pizza(self, pizza_type):
        pass
