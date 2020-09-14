# Solving LPP Maximize/Minimize (2-variable) problem

from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, LpMinimize
model = LpProblem(name="1", sense=LpMinimize)
x1 = LpVariable(name="x", lowBound=0)
x2 = LpVariable(name="y", lowBound=0)

model += 3*x1 + x2 = 34
model += x1 + 3*x2 >= 6
model += x1 + 2*x2 <=3
obj_func = lpSum(2*x1,x2)
model += obj_func
status = model.solve()
