num = int(input('enter # var '))
var=input('enter var ')
global truth
truth = input('enter truth ')
truth=[int(i) for i in truth ]
min_terms = [i for i in range(2 ** num)]

def generate_minterm_pairs(variable_index, num_variables=num):
    """ Generate pairs of minterms for a given variable index in a boolean function with specified number of variables. """
    total_minterms = 2 ** num_variables
    step = 2 ** variable_index
    pairs = []

    for i in range(0, total_minterms, step * 2):
        for j in range(step):
            pairs.append(i + j)
            pairs.append(i + j + step)
    return pairs


def find_simp(variable):
    new_var=[]
    for i in variable:
        new_var.append(truth[i])
    x=0
    simp = []
    while x < len(new_var):
        if new_var[x] == 1 and new_var[x+1] == 1:
            simp.append(1)
        elif new_var[x] == 1 and new_var[x+1] == 0:
            new = var + "'"
            simp.append(new)   
        elif new_var[x] == 0 and new_var[x+1] == 1:
            simp.append(var)
        else:
            simp.append(0)
        x += 2
    return simp

if num == 5:
    # Generate minterm pairs for each variable
    a = generate_minterm_pairs(4) # a is the 5th variable (index 4)
    b = generate_minterm_pairs(3) # b is the 4th variable (index 3)
    c = generate_minterm_pairs(2) # c is the 3rd variable (index 2)
    d = generate_minterm_pairs(1) # d is the 2nd variable (index 1)
    e = generate_minterm_pairs(0) # e is the 1st variable (index 0)
elif num == 4:
    a = generate_minterm_pairs(3) # b is the 4th variable (index 3)
    b = generate_minterm_pairs(2) # c is the 3rd variable (index 2)
    c = generate_minterm_pairs(1) # d is the 2nd variable (index 1)
    d = generate_minterm_pairs(0) # e is the 1st variable (index 0)
elif num == 3:
    a = generate_minterm_pairs(2) # c is the 3rd variable (index 2)
    b = generate_minterm_pairs(1) # d is the 2nd variable (index 1)
    c = generate_minterm_pairs(0) # e is the 1st variable (index 0)
else:
    a = generate_minterm_pairs(1) # d is the 2nd variable (index 1)
    b = generate_minterm_pairs(0) # e is the 1st variable (index 0)
if var == 'a':
    print(find_simp(a))
elif var == 'b':
    print(find_simp(b))
elif var == 'c':
    print(find_simp(c))
elif var == 'd':
    print(find_simp(d))   
elif var == 'e' :
    print(find_simp(e)) 