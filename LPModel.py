import sys, os
import pulp as p
from termcolor import colored

'''
Description:
Command line tool to solve linear programming problems. Run the main script to enter the problem statement interactively. The solution is displayed in the terminal.

Author: Jeet Yadav

License: MIT License

Notes:
This script may be updated in the future, for further convenience. Optional input/output from files, allowing mixed integer problems etc. The latest version can be found at https://github.com/jeetyadav98/LPP-Solver-CLI.
'''

def cyanc(string):
    return (colored(string, 'cyan'))

def make_variable_dictionary(n_var):
    print(cyanc('\nEnter variable names '))
    print(colored('Any alphabet except from the word var_dict', 'red'))
    var_dict= {}
    for i in range(n_var):
        var_string= input()
        var_dict[var_string]=  p.LpVariable(var_string, lowBound = 0)

    return var_dict

def get_objective(var_dict):
    obj_string= input(cyanc('\nEnter the objective function: '))

    for key,value in var_dict.items():
        var_key = "var_dict['" + key + "']"
        obj_string = obj_string.replace(key, var_key)

    return obj_string   

def get_constraint(var_dict):
    con_string= input()

    for key,value in var_dict.items():
        var_key = "var_dict['" + key + "']"
        con_string = con_string.replace(key, var_key)

    return con_string  

def print_intro():
    print(cyanc('\nCreate an LP Model from user inputs. Requirements:'))
    print(cyanc('-- Objective function (to minimize or maximize)'))
    print(cyanc('-- Nonnegative decision variables (N)'))
    print(cyanc('-- Inequality or Equality constraints (M)'))

def get_args():
    #Print command line introduction
    print_intro()

    #Get type of optimization and create LpProblem
    type_string= input(cyanc('\nType of optimization [max/min]: '))
    if type_string=='min':
        Lp_prob= p.LpProblem('Problem', p.LpMinimize)
    elif type_string=='max':
        Lp_prob= p.LpProblem('Problem', p.LpMaximize)
    else:
        print('Error: bad syntax, optimization type not recognized \nExiting..')
        exit()
    
    print(colored('Optimization type selected is ', 'red') + type_string)
    
    # Get number of variables and constraints
    n_var= int(input(cyanc('\nNumber of decision variables: ',)))
    n_con= int(input(cyanc('Number of constraints (excluding nonnegative): ',)))

    #Get variable names and make dictionary
    var_dict = make_variable_dictionary(n_var)

    #Get objective function and add to LP
    Lp_prob += eval(get_objective(var_dict))
    
    #Get constraints and add to LP
    print(cyanc('\nEnter constraints',) + '[of form a1*x1 + a2*x2.. (<= , == , >=) RHS]')
    for j in range(n_con):
        Lp_prob += eval(get_constraint(var_dict))

    return Lp_prob, var_dict


def main():
    
    Lp_model= get_args()
    Lp_prob= Lp_model[0]
    var_dict= Lp_model[1]

    #Print problem summary
    print(cyanc('\nProblem Summary: ',))
    print(Lp_prob)

    print(cyanc('------------------------------------------'))
    Lp_solve= Lp_prob.solve()
    print(cyanc('------------------------------------------'))
    print(cyanc('Solution status'), p.LpStatus[Lp_solve])

    #Print solution
    for key,value in var_dict.items():
        print('Value of ' + key + ' is: ', p.value(value))
    
    print('Objective function value: ', p.value(Lp_prob.objective))


if __name__ == "__main__":
    main()
    
    