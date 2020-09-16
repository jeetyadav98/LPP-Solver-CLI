import sys, os
import numpy as np
import pulp as p
from termcolor import colored

def make_variable_dictionary(n_var):
    print(colored('\nEnter variable names ', 'cyan'))
    print(colored('Any alphabet except from the word var_dict', 'red'))
    var_dict= {}
    for i in range(n_var):
        var_string= input()
        var_dict[var_string]=  p.LpVariable(var_string, lowBound = 0)

    return var_dict

def get_objective(var_dict):
    obj_string= input(colored('\nEnter the objective function: ','cyan'))

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
    print(colored('\nCreate an LP Model from user inputs. Requirements:','cyan'))
    print(colored('-- Objective function (to minimize or maximize)','cyan'))
    print(colored('-- Nonnegative decision variables (N) \n','cyan'))
    print(colored('-- Inequality or Equality constraints (M)','cyan'))

def get_args():
    #Print command line introduction
    print_intro()

    #Get type of optimization and create LpProblem
    type_string= input(colored('Type of optimization [max/min]: ','cyan'))
    if type_string=='min':
        Lp_prob= p.LpProblem('Problem', p.LpMinimize)
    elif type_string=='max':
        Lp_prob= p.LpProblem('Problem', p.LpMaximize)
    else:
        print('Error: bad syntax, optimization type not recognized \nExiting..')
        exit()
    
    print(colored('Optimization type selected is ', 'red') + type_string)
    
    # Get number of variables and constraints
    n_var= int(input(colored('\nNumber of decision variables: ', 'cyan')))
    n_con= int(input(colored('Number of constraints (excluding nonnegative): ', 'cyan')))

    #Get variable names and make dictionary
    var_dict = make_variable_dictionary(n_var)

    #Get objective function and add to LP
    Lp_prob += eval(get_objective(var_dict))
    
    #Get constraints and add to LP
    print(colored('\nEnter constraints', 'cyan') + '[of form a1*x1 + a2*x2.. (<= , == , >=) RHS]')
    for j in range(n_con):
        Lp_prob += eval(get_constraint(var_dict))

    return Lp_prob, var_dict


def main():
    
    Lp_model= get_args()
    Lp_prob= Lp_model[0]
    var_dict= Lp_model[1]

    #Print problem summary
    print(colored('\nProblem Summary: ', 'cyan'))
    print(Lp_prob)

    print(colored('------------------------------------------','cyan'))
    Lp_solve= Lp_prob.solve()
    print(colored('------------------------------------------','cyan'))
    print(colored('Solution status', 'cyan'), p.LpStatus[Lp_solve])

    #Print solution
    for key,value in var_dict.items():
        print('Value of ' + key + ' is: ', p.value(value))
    
    print('Objective function value: ', p.value(Lp_prob.objective))


if __name__ == "__main__":
    main()
    
    