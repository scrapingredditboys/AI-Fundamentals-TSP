import random
from City import City
from GeneticAlgorithm import GeneticAlgorithm
from Population import Population
from TourManager import TourManager
import tspio
from params_ga import Params

class GA:
    def __init__(self, path, gui):

        self.POPULATION_SIZE = 50
        self.GENERATIONS = 100

        self.path = path
        self.gui = gui

        self.population = None
        self.ga = None
        self.tourmanager = None

        self.cities = tspio.readProblem(self.path)

        self.params = Params(self)


    def start(self, populationSize, gens):
        self.POPULATION_SIZE = populationSize
        self.GENERATIONS = gens
        self.params.destroy()
        self.geneticAlgorithmStart()

    def geneticAlgorithmStart(self):

        # print(self.cities)

        self.tourmanager = TourManager()

        self.tourmanager.addCities(self.cities)
        self.population = Population(self.tourmanager, self.POPULATION_SIZE, True)
        self.ga = GeneticAlgorithm(self.tourmanager)
        self.population = self.ga.evolvePopulation(self.population)
        
        generations = []
        bestInGen = []
        
        for i in range(0, self.GENERATIONS):
            self.population = self.ga.evolvePopulation(self.population)
            self.gui.drawGA(self.population.getFittest())
            self.gui.update()
            generations.append(i)
            bestInGen.append(self.population.getFittest().getDistance())
            print("Generation: " + "{:d}".format(i) + "      Best distance: " + str(self.population.getFittest().getDistance())) 
        # Print final results
        print("Finished")
        print("Final distance: " + str(self.population.getFittest().getDistance()))
        
        tspio.writeDataGA(generations, bestInGen, self.path)





# def generateRandom():
#     return int(random.random()*500)
#
#
# if __name__ == '__main__':
#
#     tourmanager = TourManager()
#
#     # Create and add our cities
#     for i in range(30):
#         city = City(generateRandom(), generateRandom())
#         tourmanager.addCity(city)
#
#     # Initialize population
#     pop = Population(tourmanager, 50, True)
#     print("Initial distance: " + str(pop.getFittest().getDistance()))
#
#     # Evolve population for 50 generations
#     ga = GeneticAlgorithm(tourmanager)
#     pop = ga.evolvePopulation(pop)
#     for i in range(0, 100):
#         pop = ga.evolvePopulation(pop)
#
#     # Print final results
#     print("Finished")
#     print("Final distance: " + str(pop.getFittest().getDistance()))
#     print("Solution:")
#     print(pop.getFittest()