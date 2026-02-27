# Variables and domains
variables = ['A', 'B', 'C', 'D']
colors = ['Red', 'Green', 'Blue']
# Constraints (neighbors cannot have same color)
neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}
# Check if assignment is consistent
def is_consistent(var, color, assignment):
    for neighbor in neighbors[var]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True
    
# Backtracking search
def backtrack(assignment={}):
    # If all variables assigned, return assignment
    if len(assignment) == len(variables):
        return assignment
    # Select unassigned variable
    unassigned = [v for v in variables if v not in assignment]
    var = unassigned[0]
    for color in colors:
        if is_consistent(var, color, assignment):
            assignment[var] = color
            print(assignment)
            result = backtrack(assignment)
            print(result)
            if result:
                return result
            del assignment[var] #Backtrack
    return None

# Solve CSP
solution = backtrack()

print("Solution for map coloring CSP:")
print(solution)
