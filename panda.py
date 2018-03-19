
import pandas as pd
import matplotlib.pyplot as plt
from query_volumes_of_beer import make_volume_object, make_data_frame

filename = 'Inventories/2018-03-19_15:18:43.516286.csv'


def make_list_of_objects(data_struct):
    temp = []
    for string in data_struct:
        object = make_volume_object(string)
        temp.append(object)
    return temp


def display_beer_categories_by_volume():
    labels = ['Cider', 'Craft', 'Domestic', 'Import', 'Malternative', 'Mead']
    explode = [0.1, 0, 0, 0, 0, 0]
    sizes = []

    temp = make_list_of_objects(labels)
    make_data_frame(filename)

    for object in temp:
        sizes.append(object.get_volume())

    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red', 'purple']

    # Plot
    plt.pie(sizes, labels=labels, explode=explode, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.show()


display_beer_categories_by_volume()
