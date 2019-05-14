import tkinter as tk

class Params(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self)
        self.title('Parameter input')
        self.geometry('600x320')
        self.lift()
        self.attributes("-topmost", True)
        self.parent = parent
        
        tk.Label(self, text="Number of ants").grid(row=0, column=0)
        
        self.ants = tk.Entry(self, width=6, borderwidth=4, relief="ridge")
        self.ants.insert(0, 20)
        self.ants.grid(row=0, column=1)
        
        tk.Label(self, text="Number of iterations per ant").grid(row=1, column=0)
        
        self.iterations = tk.Entry(self, width=6, borderwidth=4, relief="ridge")
        self.iterations.insert(0, 12)
        self.iterations.grid(row=1, column=1)
        
        tk.Label(self, text="Number of algorithm executions").grid(row=2, column=0)
        
        self.executions = tk.Entry(self, width=6, borderwidth=4, relief="ridge")
        self.executions.insert(0, 1)
        self.executions.grid(row=2, column=1)

        tk.Label(self, text="Alpha").grid(row=3, column=0)
        
        self.alpha = tk.Entry(self, width=6, borderwidth=4, relief="ridge")
        self.alpha.insert(0, 0.1)
        self.alpha.grid(row=3, column=1)

        tk.Label(self, text="Beta").grid(row=4, column=0)
        
        self.beta = tk.Entry(self, width=6, borderwidth=4, relief="ridge")
        self.beta.insert(0, 1)
        self.beta.grid(row=4, column=1)

        tk.Label(self, text="Q0").grid(row=5, column=0)
        
        self.q0 = tk.Entry(self, width=6, borderwidth=4, relief="ridge")
        self.q0.insert(0, 0.5)
        self.q0.grid(row=5, column=1)

        tk.Label(self, text="Rho").grid(row=6, column=0)
        
        self.rho = tk.Entry(self, width=6, borderwidth=4, relief="ridge")
        self.rho.insert(0, 0.99)
        self.rho.grid(row=6, column=1)

        
        
        tk.Button(self, text="Start", command=self.start).grid(row=7, column=0)
        
        tk.Label(self, text="Made by:").grid(row=8, column=0)
        tk.Label(self, text="Kacper Leszczyński").grid(row=9, column=0)
        tk.Label(self, text="Bartłomiej Szymański").grid(row=10, column=0)
        tk.Label(self, text="Youssef Ibrahim").grid(row=11, column=0)
        tk.Label(self, text="Kamil Czerniak").grid(row=12, column=0)
        
    def start(self):
        self.parent.start(int(self.ants.get()), int(self.iterations.get()), int(self.executions.get()),
        float(self.alpha.get()), float(self.beta.get()), float(self.q0.get()), float(self.rho.get()))
        #cs = [self.c1.get(), self.c2.get(), self.c3.get()]
        #self.parent.start(float(self.start_temp.get()), float(self.end_temp.get()), float(self.cooling.get()), int(self.iters.get()), cs)
        
        