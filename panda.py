
import pandas as pd
import matplotlib.pyplot as plt
from query_inventory import get_available_inventory_dict
from query_volumes_of_beer import make_volume_object, make_data_frame

filename = '2018-03-11_19:24:51.217556.csv'


def display_beer_categories_by_count(filename):
    # Data to plot
    labels = ['Cider', 'Craft', 'Domestic', 'Import', 'Malternative', 'Mead']
    sizes = []
    cider_count = 0
    craft_count = 0
    domestic_count = 0
    import_count = 0
    malt_count = 0
    mead_count = 0
    d = get_available_inventory_dict(filename)
    for item in d['Category']:
        if item.title() == 'Cider':
            cider_count += 1
        elif item.title() == 'Craft':
            craft_count += 1
        elif item.title() == 'Domestic':
            domestic_count += 1
        elif item.title() == 'Import':
            import_count += 1
        elif item.title() == 'Malternative':
            malt_count += 1
        elif item.title() == 'Mead':
            mead_count += 1

    sizes.append(cider_count)
    sizes.append(craft_count)
    sizes.append(domestic_count)
    sizes.append(import_count)
    sizes.append(malt_count)
    sizes.append(mead_count)

    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red', 'purple']

    # Plot
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.show()


def display_beer_categories_by_volume(filename):
    labels = ['Cider', 'Craft', 'Domestic', 'Import', 'Malternative', 'Mead']
    sizes = []

    cider_category = make_volume_object('CIDER')
    craft_category = make_volume_object('CRAFT')
    domestic_category = make_volume_object('DOMESTIC')
    import_category = make_volume_object('IMPORT')
    malt_category = make_volume_object('MALTERNATIVE')
    mead_category = make_volume_object('MEAD')
    make_data_frame(filename)

    sizes.append(cider_category.get_volume())
    sizes.append(craft_category.get_volume())
    sizes.append(domestic_category.get_volume())
    sizes.append(import_category.get_volume())
    sizes.append(malt_category.get_volume())
    sizes.append(mead_category.get_volume())

    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red', 'purple']

    # Plot
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.show()


display_beer_categories_by_count(filename)
display_beer_categories_by_volume(filename)
