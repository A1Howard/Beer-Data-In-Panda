
from _datetime import datetime

filename = 'Inventories/2018-02-26_16:18:25.458346.csv'
beer_list = []
size_list = []
category_list = []

with open(filename, 'r+') as f_in:
    for line in f_in:
        line = line.split(',"')
        name = line[0]
        size = line[1]
        category = line[2]
        quantity_available = line[3]
        retail_price = line[4]
        case_retail_price = line[5]
        case_pack = line[6]

        if name.startswith('"Name'):
            continue
        elif name not in beer_list:
            beer_list.append(name)

        if size.startswith('size'):
            continue
        elif size not in size_list:
            size_list.append(size)

        if category.startswith('Category'):
            continue
        elif category not in category_list:
            category_list.append(category)


date = filename[:19]
date_obj = datetime.strptime(date, '%Y-%m-%d_%H:%M:%S')
day_num = date_obj.day
month_num = date_obj.month
time_of_day = date_obj.time()
day_of_week = date_obj.isoweekday()         # Sunday = 0 & Saturday = 6
