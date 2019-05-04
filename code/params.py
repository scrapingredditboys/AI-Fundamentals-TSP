import tkinter as tk

class Params(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self)
        self.title('Parameter input')
        self.geometry('200x320')
        self.lift()
        self.attributes("-topmost", True)
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
        
        self.c1 = tk.IntVar(value=1)
        self.c2 = tk.IntVar(value=1)
        self.c3 = tk.IntVar(value=1)
        
        tk.Label(self, text="Swap 2 points").grid(row=4, column=0)
        tk.Checkbutton(self, variable=self.c1).grid(row=4, column=1)
        
        tk.Label(self, text="Insert point elsewhere").grid(row=5, column=0)
        tk.Checkbutton(self, variable=self.c2).grid(row=5, column=1)
        
        tk.Label(self, text="Reverse subpath").grid(row=6, column=0)
        tk.Checkbutton(self, variable=self.c3).grid(row=6, column=1)
        
        tk.Button(self, text="Start", command=self.start).grid(row=7, column=0)
        
        tk.Label(self, text="Made by:").grid(row=8, column=0)
        tk.Label(self, text="Kacper Leszczyński").grid(row=9, column=0)
        tk.Label(self, text="Bartłomiej Szymański").grid(row=10, column=0)
        tk.Label(self, text="Youssef Ibrahim").grid(row=11, column=0)
        tk.Label(self, text="Kamil Czerniak").grid(row=12, column=0)
        
    def start(self):
        cs = [self.c1.get(), self.c2.get(), self.c3.get()]
        self.parent.start(float(self.start_temp.get()), float(self.end_temp.get()), float(self.cooling.get()), int(self.iters.get()), cs)
        
        