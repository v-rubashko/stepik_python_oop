class Postman:
    def __init__(self):
        self.delivery_data = []

    def add_delivery(self, street, house, flat):
        self.delivery_data.append((street, house, flat))

    def get_houses_for_street(self, street):
        res = []
        for item in self.delivery_data:
            if item[1] not in res and street == item[0]:
                res.append(item[1])
        return res

    def get_flats_for_house(self, street, flat):
        res = []
        for item in self.delivery_data:
            if item[2] not in res and item[:2] == (street, flat):
                res.append(item[2])
        return res


postman = Postman()

postman.add_delivery('Советская', 151, 74)
postman.add_delivery('Советская', 151, 75)
postman.add_delivery('Советская', 90, 2)
postman.add_delivery('Советская', 151, 74)

print(postman.get_houses_for_street('Советская'))
print(postman.get_flats_for_house('Советская', 151))
