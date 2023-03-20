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

    for i in range(int(n_clauses)):
        CNF_codified[i] = []
    
    count = 0
    for line in cnf_file:
        line = line.rstrip()[:-1]
        literals = line.split()
        for i in literals:
            CNF_codified[int(count)].append(i)
        count+=1 

    while (True):
        #Make decission
        decission = {}
        for i in range(1, int(n_variables)+1):
            decission[i] = random.randint(0,1)
        print("Decision made: ")
        print(decission)
        
        count_sat_literals = []
        for i in CNF_codified:
            count_sat_literals.append(count_satisf(CNF_codified[i], decission))
        
        for i in count_sat_literals:
            if count_sat_literals[i] == 0:
                
        print("Satisfactible clauses: ")
        print(count_sat_literals)
        
        if check_sat(count_sat_literals):
            print("Satisfactible")
            break
    
    cnf_file.close()

    
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
   

   


    #     print(decission)
    #     for i in decission:
            
    #         if decission[i] == 1 and CNF_codified[i] != []:
    #             satisfactible[1].append(CNF_codified[i])
    #             if i in satisfactible[0]:
    #                 satisfactible[0].remove(CNF_codified[i])
    #         else:
    #             if i not in satisfactible[1] and CNF_codified[i] != []:
    #                 satisfactible[0].append(CNF_codified[i])
    #         if decission[-i] == 1 and CNF_codified[-i] != []:
    #             satisfactible[1].append(CNF_codified[-i])
    #             if -i in satisfactible[0]:
    #                 satisfactible[0].remove(CNF_codified[-i])
    #         else:
    #             if i not in satisfactible[1] and CNF_codified[-i] != []:
    #                 satisfactible[0].append(CNF_codified[-i])

    #     #print (satisfactible)
    #     for j in range(int (n_variables)):
    #         if len(satisfactible[0]) == 0:
    #             print("Satisfactible")

    # while(True):
    #     line = line.rstrip()[:-1]
    #     clauses.append(line)
    #     for i in decission:
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
            



    


if __name__ == "__main__":
    main()