import tkinter as tk

class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('TSP')
        self.geometry('550x550')
        self.SIZE = 500
        self.CIRCLE_RADIUS = 2
        self.canvas = tk.Canvas(self, width=self.SIZE, height=self.SIZE)
        self.canvas.pack()
        
    def draw(self, points, solution):
        self.canvas.delete("all")
        self.drawPoints(points)
        self.drawLines(points, solution)
        
    def drawPoints(self, points):
        for i in range(len(points)):
            self.canvas.create_oval(points[i].x * self.SIZE - self.CIRCLE_RADIUS,
                                    points[i].y * self.SIZE - self.CIRCLE_RADIUS,
                                    points[i].x * self.SIZE + self.CIRCLE_RADIUS,
                                    points[i].y * self.SIZE + self.CIRCLE_RADIUS)
                                    
    def drawLines(self, points, solution):
        for i in range(len(solution) - 1):
            self.drawLine(points, solution[i], solution[i+1])
        self.drawLine(points, solution[-1], solution[0])
                                    
    def drawLine(self, points, index1, index2):
        self.canvas.create_line(points[index1].x * self.SIZE,
                                points[index1].y * self.SIZE,
                                points[index2].x * self.SIZE,
                                points[index2].y * self.SIZE)