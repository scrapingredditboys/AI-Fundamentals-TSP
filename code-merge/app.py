import os
import tkinter as tk
import tkinter.filedialog
from sa import SA
from gui import GUI

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('World Traveller')
        self.geometry('500x230')
        self.grid_propagate(False)
        
        self.grid_columnconfigure(0, weight=4)
        self.grid_columnconfigure(1, weight=1)
        
        self.frame_left = tk.Frame(self)
        self.frame_left.grid(row=0, column=0, sticky=tk.N)
        
        self.frame_right = tk.Frame(self, bd=1)
        self.frame_right.grid(row=0, column=1, sticky=tk.N)
        
        self.fileLabel = tk.Label(self.frame_left, text='<Please select a TSP file>')
        self.fileLabel.pack()
        tk.Button(self.frame_left, text='Load TSP file', command=self.open_file).pack()
        
        tk.Label(self.frame_right, text="Made by:").grid(row=0, column=0)
        tk.Label(self.frame_right, text="Kacper Leszczynski").grid(row=1, column=0)
        tk.Label(self.frame_right, text="Bartlomiej Szymanski").grid(row=2, column=0)
        tk.Label(self.frame_right, text="Youssef Ibrahim").grid(row=3, column=0)
        tk.Label(self.frame_right, text="Kamil Czerniak").grid(row=4, column=0)
        
        self.buttons = False
        
    def open_file(self):
        self.path = tk.filedialog.askopenfilename(initialdir=os.getcwd(), title='Load TSP file',
                                             filetypes=[('TSP files', ('.tsp'))])
        self.fileLabel.config(text=self.path)
        self.make_buttons()
        
    def make_buttons(self):
        if(self.buttons == False):
            tk.Label(self.frame_left, text='Please select an algorithm to run').pack(pady=4)
            tk.Button(self.frame_left, text='Simulated Annealing', command=self.sa, width=25).pack(pady=4)
            #tk.Button(self.frame_left, text='Particle Swarm Optimization', command=self.pso, width=25).pack(pady=4)
            tk.Button(self.frame_left, text='Ant Colony', command=self.ac, width=25).pack(pady=4)
            #tk.Button(self.frame_left, text='Genetic', command=self.ga, width=25).pack(pady=4)
            self.buttons = True
        
    def sa(self):
        GUI('sa', self.path)
        
    #def pso(self):
    #    GUI('pso', self.path)
        
    def ac(self):
        GUI('ac', self.path)
        
    #def ga(self):
    #    GUI('ga', self.path)
        
app = App()
app.mainloop()