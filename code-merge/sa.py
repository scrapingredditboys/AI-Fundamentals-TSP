import random as r
import point
import tspio
from params_sa import Params

E = 2.71828

class SA:
    def __init__(self, path, gui):
        self.TEMP_START = 100
        self.TEMP_END = 0.2
        self.COOLING = 0.98
        self.ITERS = 1000
        self.path = path
        
        self.points = tspio.readProblem(self.path)
        self.POINTS = len(self.points)
        self.matrix = self.generateDistanceMatrix()
        
        self.gui = gui
        
        self.params = Params(self)
        
    def start(self, start_temp, end_temp, cooling, iters, cs):
        self.TEMP_START = start_temp
        self.TEMP_END = end_temp
        self.COOLING = cooling
        self.ITERS = iters
        
        self.params.destroy()
        self.anneal(cs)
        
    def generatePoints(self):
        pts = []
        for i in range(self.POINTS):
            x = r.uniform(0, 1)
            y = r.uniform(0, 1)
            pts.append(point.Point(x, y))
        return pts

    def generateDistanceMatrix(self):
        matrix = []
        for i in range(self.POINTS):
            distances = []
            for j in range(self.POINTS):
                distances.append(self.points[i].getDistance(self.points[j]))
            matrix.append(distances)
        return matrix
            
    def anneal(self, cs):
        bestSolution = list(range(self.POINTS))
        bestDistance = self.calculateTotalDistance(bestSolution)
        temp = self.TEMP_START
        temps = []
        dists = []
        while(temp > self.TEMP_END):
            temp *= self.COOLING
            solution = bestSolution[:]
            distance = bestDistance
            for i in range(self.ITERS):
                newSolution = solution[:]
                self.mutate(newSolution, cs)
                newDistance = self.calculateTotalDistance(newSolution)
                if(newDistance < distance):
                    distance = newDistance
                    solution = newSolution[:]
                elif(E**((distance - newDistance)/temp * 100) > r.uniform(0, 1)):
                    distance = newDistance
                    solution = newSolution[:]
                if(newDistance < bestDistance):
                    bestDistance = newDistance
                    bestSolution = newSolution[:]
            print("Temparature: " + "{:0.12f}".format(temp) + "      Best distance: " + str(bestDistance)) 
            temps.append(temp)
            dists.append(bestDistance)
            self.gui.draw(bestSolution)
            self.gui.update()
        tspio.writeSolution(bestSolution, self.path)
        tspio.writeDataSA(temps, dists, self.path)
        print("Finished!\n\n")
            
    def mutate(self, solution, cs):
        index1 = r.randint(0, len(solution) - 1) #Select 2 random points
        index2 = r.randint(0, len(solution) - 1)
        if(index1 > index2):
            index1, index2 = index2, index1
            
        mutations = self.getMutations(cs)
            
        type = r.randint(0, len(mutations) - 1)
        mutations[type](solution, index1, index2)
            
    def getMutations(self, cs):
        funcs = [self.swapPoints, self.insertPoint, self.reverseSubpath]
        valid = []
        for i in range(len(funcs)):
            if(cs[i] == 1):
                valid.append(funcs[i])
        return valid
        
    def swapPoints(self, solution, index1, index2):
        solution[index1], solution[index2] = solution[index2], solution[index1]
        
    def insertPoint(self, solution, index1, index2):
        solution.insert(index1, solution.pop(index2))

    def reverseSubpath(self, solution, index1, index2):
        temp = solution[index1:index2]
        temp.reverse()
        solution[index1:index2] = temp

                
    def calculateTotalDistance(self, solution):
        distance = 0
        for i in range(len(solution) - 1):
            distance += self.matrix[solution[i]][solution[i + 1]]
        distance += self.matrix[solution[-1]][solution[0]]
        return distance
        