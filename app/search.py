from app.get_stolen_bikes import StolenBikes
from app.storage import Storage


class Search:

    def __init__(self):
        self.storage = Storage()

    def search_by_state_number(self, state_number):
        return self.storage.find({'details': {'Гос. рег. номер:': state_number}})


    def get_all_vendors(self):
        vendors = []
        for bike in self.stolen_bikes:
            for detail in bike['details']:
                if detail[0] == 'Производитель:':
                    if detail[1] not in vendors:
                        vendors.append(detail[1])
        return vendors

    def get_places(self):
        places = []
        for bike in self.stolen_bikes:
            for detail in bike['details']:
                if detail[0] == 'Место угона:':
                    if detail[1] not in places:
                        places.append(detail[1])
        return places

    def get_models_by_venor(self, vendor):
        for bike in self.stolen_bikes:
            for detail in bike['details']:
                if detail[0] == 'Производитель:':
                    if detail[1] == vendor

