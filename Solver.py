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
    size_list_vars = int(n_variables) * 2
    vars = []
    for i in range(int(n_variables)):
        i = i + 1
        vars.append(i)
    negative_vars = []
    for i in range(int(n_variables)):
        i = i + 1
        negative_vars.append(-i)
    for i in list(reversed(negative_vars)): 
        vars.append(i)
    
    print(n_variables)
    print(n_clauses)
    print(vars)

    #Read config

    file1.close()


if __name__ == "__main__":
    main()


