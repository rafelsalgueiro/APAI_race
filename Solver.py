import sys
import random 
import numpy

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
    CNF_codified    = dict()


    for i in range(int(n_variables)):
        i += 1
        CNF_codified[i] = []

    for j in range(int(n_variables)):
        j += 1
        CNF_codified[-j] = []
    
    count = 0
    for line in cnf_file:
        line = line.rstrip()[:-1]
        literals = line.split()
        for i in literals:
            CNF_codified[int(i)].append(count)
        count+=1

    print(CNF_codified)
    

    # while(True):
    #     line = line.rstrip()[:-1]
    #     clauses.append(line)
    #     for i in all_vars:
    #         index = line.find(str(i))
    #         if index != -1 and index < len(line)-1 and line[index-1] != '-':
    #             cont[i-1] +=1
    #         # elif i>=10 and index != -1 and index < len(line)-1 and line[index-1] == '-':
    #         #     cont[-i] +=1
    #         # elif index != -1 and index < len(line)-1 and line[index+1] == ' ' and line[index-1] != '-':
    #         #     cont[i-1] +=1
    #         # elif index != -1 and index < len(line)-1 and line[index+1] == ' ' and line[index-1] == '-':
    #         #     cont[-i] +=1

        # line = cnf_file.readline()
        # if line == '':
        #     break
            

    #print(cont)
    print(n_variables)
    print(n_clauses)
    #print(clauses)

    #Read config

    cnf_file.close()


if __name__ == "__main__":
    main()