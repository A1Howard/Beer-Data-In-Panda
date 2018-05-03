import random

inventory = open('/beer_data/2018-04-27_15:16:30.982991.csv', 'r+')
file_out = open('silly_style_names.csv', 'w+')
silly_styles = ['"ballpit"', '"jawn"', '"silly style"', '"something cool"', '"dunder"', '"what is life"',
                '"capstone"', '"arugula"', '"Keith Stone"', '"justforkingaround"', '"Adam.jpg"',
                '"catch me outside"', '"Uncle Bob"']

name_list = []
count = 0
for item in inventory:
    if count == 0:
        count += 1
        continue
    item = item.split(',')
    beer_name = item[0].title()
    if beer_name not in name_list:
        name_list.append(beer_name)
        style = random.choice(silly_styles)
        style.title()
        out = "%s,%s\n" % (beer_name, style)
        file_out.write(out)



