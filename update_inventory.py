#
#   BY: Adam Howard

import requests
import datetime

url = 'http://www.tanczos.com/tanczos.com/beerinventory/webexport.csv'

while True:
    result = requests.get(url)
    # result.text contains the inventory data in a CSV format

    filename = str(datetime.datetime.now()).replace(' ', '_') + '.csv'

    out_file = open('Inventories/' + filename, 'w')
    out_file.write(result.text)

    out_file.close()
    print("Success... " + filename)

    # time.sleep(5)
    break
