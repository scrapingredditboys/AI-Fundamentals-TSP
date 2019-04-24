import tkinter as tk

class Params(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self)
        self.title('TSP')
        self.geometry('200x150')
        self.parent = parent
        
        tk.Label(self, text="Starting temperature").grid(row=0, column=0)
        
        self.start_temp = tk.Entry(self, width=6, borderwidth=4, relief="ridge")
        self.start_temp.insert(0, 100)
        self.start_temp.grid(row=0, column=1)
        
        tk.Label(self, text="Ending temperature").grid(row=1, column=0)
        
        self.end_temp = tk.Entry(self, width=6, borderwidth=4, relief="ridge")
        self.end_temp.insert(0, 0.2)
        self.end_temp.grid(row=1, column=1)
        
        tk.Label(self, text="Cooling rate").grid(row=2, column=0)
        
        self.cooling = tk.Entry(self, width=6, borderwidth=4, relief="ridge")
        self.cooling.insert(0, 0.98)
        self.cooling.grid(row=2, column=1)
        
        tk.Label(self, text="Iterations").grid(row=3, column=0)
        
        self.iters = tk.Entry(self, width=6, borderwidth=4, relief="ridge")
        self.iters.insert(0, 1000)
        self.iters.grid(row=3, column=1)
        
        tk.Button(self, text="Start", command=self.start).grid(row=4, column=0)
        
    def start(self):
        self.parent.start(float(self.start_temp.get()), float(self.end_temp.get()), float(self.cooling.get()), int(self.iters.get()))
        
        