
from inventory import Inventory
from available_inventory import InventoryQueries
from volume import Volume

object_list = []


def add_volume_by_category(object, size, quantity_available):
    ounces = object.get_ounces_per_item(size)
    object.add_volume(ounces, quantity_available)


def make_data_frame(filename):
    query = InventoryQueries(Inventory(filename))
    available_inventory = query.get_available_inventory()

    name_list = []
    size_list = []
    category_list = []
    quantity_list = []
    price_list = []
    d = dict()

    for line in available_inventory:
        make_unique_lists(line['name'], name_list)
        make_unique_lists(line['size'], size_list)
        make_unique_lists(line['category'], category_list)

        price_list.append(line['price'])
        quantity_list.append(line['quantity'])

        for beer_category in object_list:
            if beer_category.name_of_object == line['category']:
                add_volume_by_category(beer_category, line['size'], line['quantity'])

    add_key_with_value(d, 'Name', name_list)
    add_key_with_value(d, 'Size', size_list)
    add_key_with_value(d, 'Category', category_list)
    add_key_with_value(d, 'Price', price_list)
    add_key_with_value(d, 'Quantity', quantity_list)

    return d


def make_unique_lists(string_to_compare, list):
    if string_to_compare not in list:
        list.append(string_to_compare)
        return list


def add_key_with_value(dict, key, value):
    dict[key] = value
    return dict


def make_volume_object(string):
    object = Volume(string)
    object_list.append(object)
    return object
