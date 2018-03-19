
from _datetime import datetime

filename = '2018-03-19_15:18:43.516286.csv'

# gets information just from the name of the .csv file
date = filename[:19]
date_obj = datetime.strptime(date, '%Y-%m-%d_%H:%M:%S')
day_num = date_obj.day
month_num = date_obj.month
time_of_day = date_obj.time()
day_of_week = date_obj.isoweekday()         # Sunday = 0 & Saturday = 6


def make_subset(item):
    return {key: item[key] for key in ['name', 'size', 'category', 'price', 'quantity', ]}


class InventoryQueries:

    def __init__(self, inventory):
        self.inventory = inventory

    def get_available_inventory(self):
        return [make_subset(item) for item in self.inventory.get_historic_inventory()
                if item is not None and item['quantity'] > 0]
