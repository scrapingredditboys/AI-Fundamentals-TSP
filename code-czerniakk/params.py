import tkinter as tk

class Params(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self)
        self.title('Parameter input')
        self.geometry('600x320')
        self.lift()
        self.attributes("-topmost", True)
        self.parent = parent
        
        tk.Label(self, text="Iterations").grid(row=0, column=0)
        
        self.iters = tk.Entry(self, width=6, borderwidth=4, relief="ridge")
        self.iters.insert(0, 100)
        self.iters.grid(row=0, column=1)
        
        tk.Label(self, text="Particles").grid(row=1, column=0)
        
        self.particles = tk.Entry(self, width=6, borderwidth=4, relief="ridge")
        self.particles.insert(0, 10)
        self.particles.grid(row=1, column=1)
        
        tk.Label(self, text="Alpha (probability order of particle best path stays the same)").grid(row=2, column=0)
        
        self.alpha = tk.Entry(self, width=6, borderwidth=4, relief="ridge")
        self.alpha.insert(0, 1)
        self.alpha.grid(row=2, column=1)
        
        tk.Label(self, text="Beta (probability order of overall best path stays the same)").grid(row=3, column=0)
        
        self.beta = tk.Entry(self, width=6, borderwidth=4, relief="ridge")
        self.beta.insert(0, 1)
        self.beta.grid(row=3, column=1)
        
        
        tk.Button(self, text="Start", command=self.start).grid(row=7, column=0)
        
        tk.Label(self, text="Made by:").grid(row=8, column=0)
        tk.Label(self, text="Kacper Leszczyński").grid(row=9, column=0)
        tk.Label(self, text="Bartłomiej Szymański").grid(row=10, column=0)
        tk.Label(self, text="Youssef Ibrahim").grid(row=11, column=0)
        tk.Label(self, text="Kamil Czerniak").grid(row=12, column=0)
        
    def start(self):
        self.parent.start(int(self.iters.get()), int(self.particles.get()), float(self.alpha.get()),
            float(self.beta.get()))
        #cs = [self.c1.get(), self.c2.get(), self.c3.get()]
        #self.parent.start(float(self.start_temp.get()), float(self.end_temp.get()), float(self.cooling.get()), int(self.iters.get()), cs)
        
        