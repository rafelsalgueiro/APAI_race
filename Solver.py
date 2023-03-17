#import os.subprocess
import sys
import random 

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
        line = file1.readlines() 
        if line[0]!= 'c':
            break
    #Error handling
    if (line[1][0]!='p'):
        sys.exit("ERROR: Not correctly formatted file (%s)." % sys.argv[1])
    
    #Get cfg parameters
    tokens = line[1].split()
    n_variables = tokens[2]
    n_clauses   = tokens[3]
    all_vars    = []
    count       = 0
    for i in range(int(n_variables)):
        i = i + 1
        all_vars.append(i)
    negative_vars = []
    for i in range(int(n_variables)):
        i = i + 1
        negative_vars.append(-i)
    for i in list(reversed(negative_vars)): 
        all_vars.append(i)
    clauses = []
    for i in range(len(line)-2):
        clauses.append(line[i+2])
        clauses[i] = clauses[i].strip(" 0\n")
    for var in all_vars:
        count = 0
        print(var)
        for match in clauses:
            if str(var) in match:
                count = count + 1
        all_vars[var] = (var, count)


    print(n_variables)
    print(n_clauses)
    print(all_vars)
    print(clauses)

    #Read config

    file1.close()


if __name__ == "__main__":
    main()


