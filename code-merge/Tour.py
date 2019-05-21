import random

class Tour:
    def __init__(self, tourManager, tour=None):
        self.fitness = 0
        self.distance = 0
        self.tour = []
        self.tourManager = tourManager

        if tour is None:
            for i in range(tourManager.numberOfCities()):
                self.tour.append(None)

    def __len__(self):
        return len(self.tour)

    def __getitem__(self, item):
        return self.tour[item]

    def __setitem__(self, key, value):
        self.tour[key] = value

    def __repr__(self):
        geneString = " | "
        for i in range(len(self.tour)):
            geneString += str(self.__getitem__(i)) + "|"
        return geneString

    def getCity(self, tourPosition):
        return self.tour[tourPosition]

    def setCity(self, tourPosition, city):
        self.tour[tourPosition] = city
        self.fitness = 0.0
        self.distance = 0

    def generateIndividual(self):
        for i in range(self.tourManager.numberOfCities()):
            self.setCity(i, self.tourManager.getCity(i))
        random.shuffle(self.tour)

    def getFitness(self):
        if self.fitness == 0:
            self.fitness = 1/float(self.getDistance())
        return self.fitness

    def getDistance(self):
        if self.distance == 0:
            tourDistance = 0
            for i in range(self.tourSize()):
                fromCity = self.getCity(i)
                destinationCity = None
                if i+1 < self.tourSize():
                    destinationCity = self.getCity(i+1)
                else:
                    destinationCity = self.getCity(0)
                tourDistance += fromCity.distanceTo(destinationCity)
            self.distance = tourDistance
        return self.distance

    def tourSize(self):
        return len(self.tour)

    def containsCity(self, city):
        return city in self.tour

    def cityIndex(self, city):
        if city in self.tour:
            return self.tour.index(city)
        else:
            return None
