
from _datetime import datetime

filename = '2018-03-11_19:24:51.217556.csv'
date = filename[:19]
date_obj = datetime.strptime(date, '%Y-%m-%d_%H:%M:%S')
day_num = date_obj.day
month_num = date_obj.month
time_of_day = date_obj.time()
day_of_week = date_obj.isoweekday()         # Sunday = 0 & Saturday = 6


def get_all_inventory(filename):
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

            line = line.strip()
            line = line.split(',')
            name = line[0]
            size = line[1]
            category = line[2]
            quantity_available = float(line[3])
            retail_price = float(line[4])
            case_retail_price = float(line[5])
            case_pack = float(line[6])

            beer_list.append(name)
            size_list.append(size)
            category_list.append(category)
            quantity_list.append(quantity_available)
            retail_list.append(retail_price)
            case_retail.append(case_retail_price)
            case_pack_list.append(case_pack)

    d['Name'] = beer_list
    d['Size'] = size_list
    d['Category'] = category_list
    d['Quantity Available'] = quantity_list
    d['Retail Price'] = retail_list
    d['Case Retail Price'] = case_retail
    d['Case Pack'] = case_pack_list

    return d


def get_available_inventory_dict(filename):
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

            beer_list.append(name)
            size_list.append(size)
            category_list.append(category)
            quantity_list.append(quantity_available)
            retail_list.append(retail_price)
            case_retail.append(case_retail_price)
            case_pack_list.append(case_pack)

    d['Name'] = beer_list
    d['Size'] = size_list
    d['Category'] = category_list
    d['Quantity Available'] = quantity_list
    d['Retail Price'] = retail_list
    d['Case Retail Price'] = case_retail
    d['Case Pack'] = case_pack_list

    return d

