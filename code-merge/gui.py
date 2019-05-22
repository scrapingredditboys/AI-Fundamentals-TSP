import tkinter as tk
from sa import SA
#from tsp_pso import CompleteGraph, PSO
import tspio
import anttsp
#from Travelling_Genetic import GA

class GUI(tk.Tk):
    def __init__(self, algorithmType, path):
        tk.Tk.__init__(self)
        self.title('World Traveller')
        self.geometry('550x550')
        self.SIZE = 500
        self.CIRCLE_RADIUS = 2
        self.canvas = tk.Canvas(self, width=self.SIZE, height=self.SIZE)
        self.canvas.pack()
        
        self.points = None
        
        if(algorithmType == 'sa'):
            sa = SA(path, self)
            self.points = sa.points
        #elif(algorithmType == 'pso'):
        #    self.points = tspio.readProblem(path)
        #    graph = CompleteGraph(amount_vertices=len(self.points))
        #    graph.vertices = list(self.points)
        #    graph.generates()
        #    pso = PSO(graph, iterations=10, size_population=1000, beta=0.5, alpha=0.5, gui = self)
        elif(algorithmType == 'ac'):
            self.points = tspio.readProblem(path)
            ants = anttsp.Ants(points=self.points, num_ants=20, num_iterations=12, num_repetitions=1, alpha = 0.1, beta=1, q0=0.5, rho=1, gui=self)
        #elif(algorithmType == 'ga'):
        #    ga = GA(path, self)
        #    self.points = ga.cities
        
        self.offsetX = self.getOffsetX()
        self.offsetY = self.getOffsetY()
        self.norm = self.getNormalizationFactor()
        
    def draw(self, solution):
        self.canvas.delete("all")
        self.drawPoints()
        self.drawLines(solution)
        
    def drawPoints(self):
        for i in range(len(self.points)):
            self.canvas.create_oval((self.points[i].x - self.offsetX) * self.norm * self.SIZE - self.CIRCLE_RADIUS,
                                    (self.points[i].y - self.offsetY) * self.norm * self.SIZE - self.CIRCLE_RADIUS,
                                    (self.points[i].x - self.offsetX) * self.norm * self.SIZE + self.CIRCLE_RADIUS,
                                    (self.points[i].y - self.offsetY) * self.norm * self.SIZE + self.CIRCLE_RADIUS)
                                    
    def drawLines(self, solution):
        for i in range(len(solution) - 1):
            self.drawLine(solution[i], solution[i+1])
        self.drawLine(solution[-1], solution[0])
                                    
    def drawLine(self, index1, index2):
        self.canvas.create_line((self.points[index1].x - self.offsetX) * self.norm * self.SIZE,
                                (self.points[index1].y - self.offsetY) * self.norm * self.SIZE,
                                (self.points[index2].x - self.offsetX) * self.norm * self.SIZE,
                                (self.points[index2].y - self.offsetY) * self.norm * self.SIZE)
                                
    def drawGA(self, solution):
        self.canvas.delete("all")
        self.drawPoints()
        self.drawLinesGA(solution)
                                
    def drawLinesGA(self, solution):
        for i in range(len(solution) - 1):
            self.drawLineGA(solution[i], solution[i+1])
        self.drawLineGA(solution[-1], solution[0])
                                    
    def drawLineGA(self, index1, index2):
        self.canvas.create_line((index1.x - self.offsetX) * self.norm * self.SIZE,
                                (index1.y - self.offsetY) * self.norm * self.SIZE,
                                (index2.x - self.offsetX) * self.norm * self.SIZE,
                                (index2.y - self.offsetY) * self.norm * self.SIZE)
                                
    def getNormalizationFactor(self):
        xs = []
        ys = []
        for i in range(len(self.points)):
            xs.append(self.points[i].x - self.offsetX)
            ys.append(self.points[i].y - self.offsetY)
        return 1/max(max(xs), max(ys))
        
    def getOffsetX(self):
        xs = []
        for i in range(len(self.points)):
            xs.append(self.points[i].x)
        return min(xs)
        
    def getOffsetY(self):
        ys = []
        for i in range(len(self.points)):
            ys.append(self.points[i].y)
        return min(ys)
        