import tkinter as tk
import sys
from Travelling_Genetic import GA

class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('World Traveller')
        self.geometry('550x550')
        self.SIZE = 500
        self.CIRCLE_RADIUS = 2
        self.canvas = tk.Canvas(self, width=self.SIZE, height=self.SIZE)
        self.canvas.pack()
        
        self.ga = GA(sys.argv[1], self)
        self.points = self.ga.cities

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
        
gui = GUI()
gui.mainloop()