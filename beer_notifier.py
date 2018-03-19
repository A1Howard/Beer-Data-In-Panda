#   Notifies the author when a specific beer is in stock via the newest inventory .CSV file
#   BY: Adam Howard

from twilio.rest import Client
import time

account_sid = "AC4c2291dc257ebc4de7afcda7b91b14b1"
auth_token = "116bbd76f3f365c0a43b334bf6746367"

client = Client(account_sid, auth_token)
filename = input('Please input the name of the .csv file: ')


def loop(filename):
    with open(filename, 'r') as f:
        # skip first line because it is labels for the columns
        next(f)
        # loop through .CSV file
        for line in f:
            line = line.strip()
            line = line.split(',')
            # create variables for each column
            name, size, category, quantity_available, retail, case_retail, case_pack = line[0], line[1], line[2], line[3], line[4], line[5], line[6]

            # if a 1/2 keg of COORS LIGHT is in the inventory, I want to be notified
            if name == '"COORS LIGHT"' and size == '"1/2 KEG"' and quantity_available != '"0.00"':
                client.messages.create(
                    to="+17177771946",
                    from_="+17172760528",
                    body="COORS LIGHT Keg Available!")

            # if a 24/12 OZ BTL of LIONSHEAD is in the inventory, I want to be notified
            elif name == '"LIONSHEAD"' and size == '"24/12 OZ BTL"' and quantity_available != '"0.00"':
                client.messages.create(
                    to="+17177771946",
                    from_="+17172760528",
                    body="LIONSHEAD BOTTLES Available!")
    f.close()


loop(filename)