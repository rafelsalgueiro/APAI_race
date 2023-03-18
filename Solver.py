#import os.subprocess
import sys
import random 
import numpy

def main():
    #os.subprocess("python3 rnd-conf-gen.py 50 100 > config.conf")
    #os.subprocess("./minicom config.conf &> stdout.txt")
    if len(sys.argv) != 2:
        sys.exit("Use: %s <input_cnf_formula>" % sys.argv[0])

    try:
        file1 = open(sys.argv[1], "r")
    except:
        sys.exit("ERROR: Could not open (%s)." % sys.argv[1])

    #Skip comments
    while(True):
        line = file1.readline()
        if line[0]!= 'c':
            break
    #Error handling
    if (line[0]!='p'):
        sys.exit("ERROR: Not correctly formatted file (%s)." % sys.argv[1])
    



    #Get cfg parameters
    tokens = line.split()
    n_variables = tokens[2]
    n_clauses   = tokens[3]
    all_vars    = []
    
    if (line[0] == 'p'):
        line = file1.readline()

    clauses = []
    while(True):
        line = line.rstrip()[:-1]
        clauses.append(line)
        line = file1.readline()
        if line == '':
            break
    for i in range(int(n_variables)):
        i = i + 1
        all_vars.append(i)
    negative_vars = []
    for i in range(int(n_variables)):
        i = i + 1
        negative_vars.append(-i)
    for i in list(reversed(negative_vars)): 
        all_vars.append(i)



    print(n_variables)
    print(n_clauses)
    print(all_vars)
    print(clauses)

    #Read config

    file1.close()


if __name__ == "__main__":
    main()

                                            ### Walksat problem ###

def walk_sat(formula, max_flips, p):
    # Inicializar una asignación aleatoria
    assignment = {var: random.choice([True, False]) for var in formula.variables}
    
    for i in range(max_flips):
        # Verificar si la asignación actual satisface la fórmula
        if formula.evaluate(assignment):
            return assignment
        
        # Seleccionar una cláusula insatisfecha al azar
        unsatisfied_clauses = [c for c in formula.clauses if not c.evaluate(assignment)]
        clause = random.choice(unsatisfied_clauses)
        
        # Seleccionar una variable al azar de la cláusula
        var = random.choice(clause.variables)
        
        # Seleccionar la asignación que maximiza el número de cláusulas satisfechas
        if random.uniform(0, 1) < p:
            # Elegir aleatoriamente una asignación para la variable seleccionada
            assignment[var] = random.choice([True, False])
        else:
            # Elegir la asignación que maximiza el número de cláusulas satisfechas
            flipped_assignment = {var: not assignment[var]}
            if formula.num_satisfied_clauses(flipped_assignment) > formula.num_satisfied_clauses(assignment):
                assignment = flipped_assignment
    
    return None

