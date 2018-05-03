
from inventory import Inventory
from available_inventory import InventoryQueries
from volume import Volume

# TODO: make a pie chart of all the beers from a certain category

file = 'tests/test_files/domestic_beers.csv'
i = InventoryQueries(Inventory(file))
available_inventory = i.get_available_inventory()

list = []

class Beer:

    def __init__(self, name, size, category, price, quantity):
        self.name = name
        self.size = size
        self.category = category
        self.price = price
        self.quantity = quantity
        self.volume = Volume(name_of_object=name)
        self.list_of_quantity = []

    def add_quantity(self, quantity):
        self.list_of_quantity.append(quantity)

    def get_quantity(self):
        total = 0
        for x in self.list_of_quantity:
            total += x
        return total

    def get_volume(self, name):
        if self.name == name:
            return self.volume.get_volume()

for item in available_inventory:
    