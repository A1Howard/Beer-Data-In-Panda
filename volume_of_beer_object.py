
class VolumePerCategory:

    def __init__(self, category):
        self.category = category
        self.list_of_volumes = []

    def create_volume_per_single_item(self, size):
        number_per = 1
        if 'KEG' in size:
            if '1/2' in size:
                return 1984
            elif '1/4' in size:
                return 992
            elif '1/6' in size:
                return 661
            elif '1/8' in size:
                return 496
        elif '/' in size:
            size = size.split('/')
            number_per = int(size[0])
            size = size[1]

        if '50 LTR' in size:
            return number_per * 1690

        elif '30 LTR' in size:
            return number_per * 1014

        elif '10 LITER' in size:
            return number_per * 338

        elif '6 LITER' in size:
            return number_per * 202

        elif '5 LITER' in size:
            return number_per * 169

        elif '3 LITER' in size:
            return number_per * 101

        elif '1.5 LTR' in size:
            return number_per * 50

        elif '765 ML' in size:
            return number_per * 25

        elif '750 ML' in size:
            return number_per * 25

        elif '375 ML' in size:
            return number_per * 12

        elif '64 OZ' in size:
            return number_per * 64

        elif '40 OZ' in size:
            return number_per * 40

        elif '32 OZ' in size:
            return number_per * 32

        elif '25 OZ' in size:
            return number_per * 25

        elif '24 OZ' in size:
            return number_per * 24

        elif '23.5 OZ' in size:
            return number_per * 23.5

        elif '22 OZ' in size:
            return number_per * 22

        elif '19.2 OZ' in size:
            return number_per * 19.2

        elif '19 OZ' in size:
            return number_per * 19

        elif '16.9 OZ' in size:
            return number_per * 16.9

        elif '16 OZ' in size:
            return number_per * 16

        elif '15.2 OZ' in size:
            return number_per * 15.2

        elif '14.9 OZ' in size:
            return number_per * 14.9

        elif '13.65 OZ' in size:
            return number_per * 13.65

        elif '12.7 OZ' in size:
            return number_per * 12.7

        elif '12 OZ' in size:
            return number_per * 12

        elif '11.5 OZ' in size:
            return number_per * 11.5

        elif '11.2 OZ' in size:
            return number_per * 11.2

        elif '10 OZ' in size:
            return number_per * 10

        elif '8.4 OZ' in size:
            return number_per * 8.4

        elif '8 OZ' in size:
            return number_per * 8

        elif '7 OZ' in size:
            return number_per * 7

    def add_volume(self, ounces, quantity_available):
        x = ounces * quantity_available
        self.list_of_volumes.append(x)

    def get_volume(self):
        sum = 0
        for item in self.list_of_volumes:
            sum += item
        return sum
