# reading the file

def reading_cost(file_name):
    
    with open(file_name) as f:
        d = dict(line.strip().split(',') for line in f)
    return d
path = "../project/data/call-costs-3.txt"


call_costs = (reading_routes(path))
