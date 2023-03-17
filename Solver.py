#import os.subprocess
import sys

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
    
    print(n_variables)
    print(n_clauses)

    #Read config

    file1.close()


if __name__ == "__main__":
    main()


