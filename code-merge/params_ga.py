import tkinter as tk

class Params(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self)
        self.title('Parameter input')
        self.geometry('180x90')
        self.lift()
        self.attributes("-topmost", True)
        self.parent = parent
        
        tk.Label(self, text="population size").grid(row=0, column=0)
        
        self.popSize = tk.Entry(self, width=6, borderwidth=4, relief="ridge")
        self.popSize.insert(0, 50)
        self.popSize.grid(row=0, column=1)

        tk.Label(self, text="generations").grid(row=3, column=0)
        
        self.gens = tk.Entry(self, width=6, borderwidth=4, relief="ridge")
        self.gens.insert(0, 100)
        self.gens.grid(row=3, column=1)

        tk.Button(self, text="Start", command=self.start).grid(row=7, column=0)
        
    def start(self):
        self.parent.start(int(self.popSize.get()), int(self.gens.get()))
