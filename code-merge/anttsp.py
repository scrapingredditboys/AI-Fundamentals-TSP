from antcolony import AntColony
from antgraph import AntGraph

import tspio, params_ac

import sys
import traceback

#default
num_nodes = 10

#if __name__ == "__main__":  

class Ants:
    def __init__(self, points, num_ants, num_iterations, num_repetitions, 
        alpha, beta, q0, rho, gui):
        self.points = points
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.num_repetitions = num_repetitions
        self.alpha = alpha
        self.beta = beta
        self.q0 = q0
        self.rho = rho
        self.gui = gui
        self.cities = list(range(len(points)))
        self.cost_mat = [[0 for x in range(len(points))] for y in range(len(points))] 
        for i in range(len(points)):
            for j in range(len(points)):
                self.cost_mat[i][j] = points[i].getDistance(points[j])

        self.num_nodes = len(points)

        self.params = params_ac.Params(self)

    def run(self):
        try:
            graph = AntGraph(self.num_nodes, self.cost_mat)
            best_path_vec = None
            best_path_cost = sys.maxsize
            for i in range(0, self.num_repetitions):
                graph.reset_tau()
                ant_colony = AntColony(graph, self.num_ants, 
                    self.num_iterations, self.alpha, self.beta, self.q0, self.rho, self.gui)
                ant_colony.start()
                if ant_colony.best_path_cost < best_path_cost:
                    best_path_vec = ant_colony.best_path_vec
                    best_path_cost = ant_colony.best_path_cost


            print ("\n------------------------------------------------------------")
            print ("                     Results                                ")
            print ("------------------------------------------------------------")
            print ("\nBest path = {0}".format(best_path_vec))
            print ("\nBest path cost = {0}\n".format(best_path_cost))
        
        except Exception as e:
            print ("exception: " + str(e))
            traceback.print_exc()
        
    def start(self, ants, iterations, executions, alpha, beta, q0, rho):
        self.params.destroy()
        self.__init__(points=self.points, num_ants=ants, num_iterations=iterations, 
            num_repetitions=executions, alpha = alpha, beta = beta,
            q0 = q0, rho = rho, gui=self.gui)
        self.params.destroy()
        self.run()
        self.params = params_ac.Params(self)
