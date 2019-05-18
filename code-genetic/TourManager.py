


class TourManager:

    destinationCities = []

    def addCities(self, cities):
        for i in range(len(cities)):
            self.destinationCities.append(cities[i])

    def addCity(self, city):
        self.destinationCities.append(city)

    def getCity(self, index):
        return self.destinationCities[index]

    def numberOfCities(self):
        return len(self.destinationCities)
