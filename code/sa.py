import random as r
import gui
import point
import tspio
import sys

E = 2.71828

class SA:
    def __init__(self):
        self.TEMP_START = 100
        self.TEMP_END = 0.2
        self.COOLING = 0.98
        self.ITERS = 1000
        self.path = sys.argv[1]
        
        self.points = tspio.readProblem(self.path)
        self.POINTS = len(self.points)
        self.matrix = self.generateDistanceMatrix()
        self.gui = gui.GUI(self.points)
        self.anneal()
        
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
            
    def anneal(self):
        bestSolution = list(range(self.POINTS))
        bestDistance = self.calculateTotalDistance(bestSolution)
        temp = self.TEMP_START
        while(temp > self.TEMP_END):
            temp *= self.COOLING
            solution = bestSolution[:]
            distance = bestDistance
            for i in range(self.ITERS):
                newSolution = solution[:]
                self.mutate(newSolution)
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
            print("Temparature: " + str(temp) + "      Best distance: " + str(bestDistance)) 
            self.gui.draw(bestSolution)
            self.gui.update()
        tspio.writeSolution(bestSolution, self.path)
        input("Finished! Press Enter to continue...")
            
    def mutate(self, solution):
        index1 = r.randint(0, len(solution) - 1) #Select 2 random points
        index2 = r.randint(0, len(solution) - 1)
        if(index1 > index2):
            index1, index2 = index2, index1
        type = r.randint(0, 2)
        if(type == 0): #Swap the points
            temp = solution[index1]
            solution[index1] = solution[index2]
            solution[index2] = temp
        elif(type == 1): #Insert a point elsewhere in the path
            solution.insert(index1, solution.pop(index2))
        elif(type == 2): #reverse a subpath
            temp = solution[index1:index2]
            temp.reverse()
            solution[index1:index2] = temp
                
    def calculateTotalDistance(self, solution):
        distance = 0
        for i in range(len(solution) - 1):
            distance += self.matrix[solution[i]][solution[i + 1]]
        distance += self.matrix[solution[-1]][solution[0]]
        return distance
        
SA()