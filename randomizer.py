import sys
import random 

def main():
    if len(sys.argv) != 2:
        sys.exit("Use: %s <input_cnf_formula>" % sys.argv[0])

    try:
        cnf_file = open(sys.argv[1], "r")
    except:
        sys.exit("ERROR: Could not open (%s)." % sys.argv[1])

    #Skip comments
    while(True):
        line = cnf_file.readline()
        if line[0]!= 'c':
            break

    #Error handling
    if (line[0]!='p'):
        sys.exit("ERROR: Not correctly formatted file (%s)." % sys.argv[1])
    
    #Get cfg parameters
    args            = line.split()
    n_variables     = args[2]
    n_clauses       = args[3]
    clauses         = dict()

    #For each clause, save literals
    #Initialice keys
    for i in range(int(n_clauses)):
        clauses[i] = []
    
    #Read file and add literals
    count = 0
    for line in cnf_file:
        line = line.rstrip()[:-1]
        literals = line.split()
        for i in literals:
            clauses[int(count)].append(i)
        count+=1 

    while (True):
        #Make decission
        decission = {}
        for i in range(1, int(n_variables)+1):
            decission[i] = random.randint(0,1)
        
        #Check if is satisfactible
        count_sat_literals = []
        for i in clauses:
            count_sat_literals.append(count_satisf(clauses[i], decission))
        
        if check_sat(count_sat_literals):
            print("c Randomizer")
            print("s SATISFIABLE")
            finallist = printVars(decission)
            print("V " + str(finallist)[1:-1])
            break

        # #Flip variables
        # for i in range(len(count_sat_literals)):
        #     if count_sat_literals[i] == 0:
        #         chosen = clauses[i]

        # decission = findBestFlip(chosen, decission,clauses)

        
        # print("Satisfactible clauses: ")
        # print(count_sat_literals)
        
    cnf_file.close()

def findBestFlip(clause, originalDecissions, clauses):
    numBrokenClauses = []
    testDecisions = {}
    count_sat_literals = []
    for literal in clause:
        testDecisions = originalDecissions.copy()
        
        flipValue(literal,testDecisions)
        for c in clauses:
            count_sat_literals.append(count_satisf(clauses[c], testDecisions))
        numBrokenClauses.append(insatClauseCounter(count_sat_literals))
    #print (numpy.min(numBrokenClauses))
    
    finalTestDecision = testDecisions[min(numBrokenClauses)]
    return finalTestDecision
        
def flipValue(literal, testDecisions):
    if literal in testDecisions and testDecisions[literal] == 0:
        testDecisions[literal] = 1
    if literal in testDecisions and testDecisions[literal] == 1:
        testDecisions[literal] = 0

def insatClauseCounter(count_sat_literals):
    countZero = 0
    for i in count_sat_literals:
        if i == 0:
            countZero += 1
    return countZero
    
def check_sat(count_sat_literals):
    clause_sat = 0
    for i in count_sat_literals:
        if i > 0:
            clause_sat +=1
    if clause_sat == len(count_sat_literals):
        return True
    
    return False
    

def count_satisf(clausula, decision):
    count = 0
    for literal in clausula:
        if literal[0] == '-':
            if decision[int(literal.lstrip('-'))] == 0:
                count += 1
        else:
            if decision[int(literal)] != 0:
                count += 1

    return count

def printVars(decission):
    l = []
    j = 1
    for i in decission:
        if decission[i] == 0:
            l.append(-j)
        else:
            l.append(j)
        j+=1
    return l


if __name__ == "__main__":
    main()