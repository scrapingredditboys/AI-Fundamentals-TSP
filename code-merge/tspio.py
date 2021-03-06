import point
from pandas import DataFrame

def readProblem(path):
    file = open(path, "r")
    points = []
    for line in file:
        numbers = line.split(' ')
        if(len(numbers) == 3 and numbers[0].isdigit()):
            points.append(point.Point(float(numbers[2]), -float(numbers[1])))
    file.close()
    return points

def writeSolution(solution, path):
    parts = path.split('.')
    parts[0] += 'Solution'
    path = parts[0] + '.txt'
    
    file = open(path, "w")
    file.write(' '.join(str(x) for x in solution))
    file.close()
    
def readSolution(path):
    file = open(path, "r")
    return list(map(int, file.read().split(' ')))
    
def writeDataSA(temps, dists, path):
    data = {
        'Temperature': temps,
        'Distance': dists
    }
    
    df = DataFrame(data, columns = ['Temperature', 'Distance'])
    
    parts = path.split('.')
    parts[0] += 'DataSA'
    path = parts[0] + '.csv'
    
    df.to_csv(path)
    
def writeDataPSO(global_best, path):
    data = {
        'Global best': global_best
    }
    
    df = DataFrame(data, columns = ['Global best'])
        
    df.to_csv(path)
    
def writeDataAC(global_best, path):
    data = {
        'Global best': global_best
    }
    
    df = DataFrame(data, columns = ['Global best'])
        
    df.to_csv(path)
    
def writeDataGA(generations, bestInGen, path):
    data = {
        'Generation': generations,
        'Distance': bestInGen
    }
    
    df = DataFrame(data, columns = ['Generation', 'Distance'])
    
    parts = path.split('.')
    parts[0] += 'DataGA'
    path = parts[0] + '.csv'
    
    df.to_csv(path)
    