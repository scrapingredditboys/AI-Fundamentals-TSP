from Population import Population
from Tour import Tour
import random

class GeneticAlgorithm:
    def __init__(self, tourManager):
        self.tourManager = tourManager
        self.mutationRate = 1
        self.tournamentSize = 4
        self.elitism = True


    def evolvePopulation(self, inPopulation):
        population = Population(self.tourManager, inPopulation.populationSize(), False)
        elitismOffset = 0
        if self.elitism:
            population.saveTour(0, inPopulation.getFittest())
            elitismOffset = 1

        for i in range(elitismOffset, population.populationSize()):
            parenti = self.tournamentSelection(inPopulation)
            parentii = self.tournamentSelection(inPopulation)
            child = self.crossover(parenti, parentii)
            population.saveTour(i, child)
            if random.random() < self.mutationRate:
                self.mutate(population.getTour(i))

        return population


    def crossover(self, parenti, parentii):
        child = Tour(self.tourManager)
        startPos = int(random.random() * parenti.tourSize())
        endPos = int(random.random() * parentii.tourSize())
        
        if startPos > endPos:
            startPos, endPos = endPos, startPos

        for i in range(startPos, endPos):
            child.setCity(i, parenti.getCity(i))
            
        toFill = [x for x in range(child.tourSize()) if x not in range(startPos, endPos)]
        counter = 0
        
        for i in range(parentii.tourSize()):
            if not child.containsCity(parentii.getCity(i)):
                child.setCity(toFill[counter], parentii.getCity(i))
                counter += 1

        return child


    def tournamentSelection(self, pop):
        tournament = Population(self.tourManager, self.tournamentSize, False)
        for i in range(self.tournamentSize):
            rand = int(random.random() * pop.populationSize())
            tournament.saveTour(i, pop.getTour(rand))

        tourFittest = tournament.getFittest()
        return tourFittest


    def mutate(self, tour):
        i = int(random.random()*tour.tourSize())
        j = int(random.random()*tour.tourSize())
        if(i > j):
            i, j = j, i
            
        cities = []
        counter = 0
        for k in range(i, j):
            cities.append(tour.getCity(k))
            
        for k in reversed(range(i, j)):
            tour.setCity(k, cities[counter])
            counter += 1