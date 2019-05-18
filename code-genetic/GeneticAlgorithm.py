from Population import Population
from Tour import Tour
import random

class GeneticAlgorithm:
    def __init__(self, tourManager):
        self.tourManager = tourManager
        self.mutationRate = 0.015
        self.tournamentSize = 5
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

        for i in range(population.populationSize()):
            self.mutate(population.getTour(i))

        return population


    def crossover(self, parenti, parentii):
        child = Tour(self.tourManager)
        startPos = int(random.random() * parenti.tourSize())
        endPos = int(random.random() * parentii.tourSize())

        for i in range(child.tourSize()):
            if startPos < endPos and startPos < i < endPos:
                child.setCity(i, parenti.getCity(i))
            elif startPos > endPos:
                if not startPos < i < endPos:
                    child.setCity(i, parenti.getCity(i))

        for i in range(parentii.tourSize()):
            if not child.containsCity(parentii.getCity(i)):
                for j in range(child.tourSize()):
                    if child.getCity(j) is None:
                        child.setCity(j, parentii.getCity(i))
                        break

        return child


    def tournamentSelection(self, pop):
        tournament = Population(self.tourManager, self.tournamentSize, False)
        for i in range(self.tournamentSize):
            rand = int(random.random() * self.tournamentSize)
            tournament.saveTour(i, pop.getTour(rand))

        tourFittest = tournament.getFittest()
        return tourFittest


    def mutate(self, tour):
        for i in range(tour.tourSize()):
            if random.random() < self.mutationRate:
                j = int(random.random()*tour.tourSize())
                cityI = tour.getCity(i)
                cityII = tour.getCity(j)
                tour.setCity(i, cityII)
                tour.setCity(j, cityI)