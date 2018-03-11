
from volume_of_beer_object import VolumePerCategory

filename = '2018-03-11_19:24:51.217556.csv'
list = []


def make_volume_object(string):
    object = VolumePerCategory(string)
    list.append(object)
    return object


def add_volume_by_category(object, size, quantity_available):
    ounces = object.create_volume_per_single_item(size)
    object.add_volume(ounces, quantity_available)


def make_data_frame(filename):
    beer_list = []
    size_list = []
    category_list = []
    quantity_list = []
    retail_list = []
    case_retail = []
    case_pack_list = []
    d = dict()

    with open('Inventories/' + filename, 'r+') as f_in:
        count = 0
        for line in f_in:
            if count == 0:
                count += 1
                continue

            line = line.split('","')
            name = line[0].strip('""')
            size = line[1].strip('""')
            category = line[2].strip('""')
            quantity_available = float(line[3].strip('""'))
            retail_price = float(line[4].strip('""'))
            case_retail_price = float(line[5].strip('""'))
            case_pack = float(line[6].strip('"",\n'))

            if quantity_available <= 0.00:
                continue

            if category not in category_list:
                category_list.append(category)

            beer_list.append(name)
            size_list.append(size)
            quantity_list.append(quantity_available)
            retail_list.append(retail_price)
            case_retail.append(case_retail_price)
            case_pack_list.append(case_pack)

            for beer_category in list:
                if beer_category.category == category:
                    print(size)
                    add_volume_by_category(beer_category, size, quantity_available)

    d['Name'] = beer_list
    d['Size'] = size_list
    d['Category'] = category_list
    d['Quantity Available'] = quantity_list
    d['Retail Price'] = retail_list
    d['Case Retail Price'] = case_retail
    d['Case Pack'] = case_pack_list

    return d


cider_category = make_volume_object('CIDER')
craft_category = make_volume_object('CRAFT')
domestic_category = make_volume_object('DOMESTIC')
import_category = make_volume_object('IMPORT')
malt_category = make_volume_object('MALTERNATIVE')
mead_category = make_volume_object('MEAD')

make_data_frame(filename)
