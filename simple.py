from pyomo.core import *
from pyomo.environ import *
from pyomo.opt import SolverFactory

import pandas as pd

model = ConcreteModel()

model.x1 = Var(initialize=1, within= Integers)
model.x2 = Var(initialize=1, within= Integers)

model.constraint1 = Constraint(expr = 10*model.x1 + 7*model.x2 <= 40)
model.constraint2 = Constraint(expr = model.x1 + model.x2 <= 5)

model.objective =  Objective(expr = -17*model.x1-12*model.x2,sense=minimize)

instance = model

solver = 'glpk'
solver_io = 'nl'
opt = SolverFactory(solver)
opt.options['outlev'] = 1 # tell gurobi to be verbose with output
#opt.options['solnsens'] = 1

results = opt.solve(instance,tee=True)


list_of_vars =[v.value for v in instance.component_objects(ctype=Var, active=True, descend_into=True)]

var_names =[v.name for v in instance.component_objects(ctype=Var, active=True, descend_into=True)]

print(list_of_vars)
print(var_names)

result_series = pd.Series(list_of_vars,index=var_names)
result_series.to_csv('my_results.csv')