import City
from pandas import DataFrame

def readProblem(path):
    file = open(path, "r")
    cities = []
    for line in file:
        numbers = line.split(' ')
        if(len(numbers) == 3 and numbers[0].isdigit()):
            cities.append(City.City(float(numbers[2]), -float(numbers[1])))
    file.close()
    return cities

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
    
def writeData(temps, dists, path):
    data = {
        'Temperature': temps,
        'Distance': dists
    }
    
    df = DataFrame(data, columns = ['Temperature', 'Distance'])
    
    parts = path.split('.')
    parts[0] += 'Data'
    path = parts[0] + '.csv'
    
    df.to_csv(path)