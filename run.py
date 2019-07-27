# runmodel.py
# runs model defined in OSe_2019_05_13.py

from __future__ import division
from pyomo.environ import *
import pandas as pd
#import numpy as np
#import datetime as dt

# get the model from another file OSe_2019_05_13.py
from OSe_2019_05_13 import model
#from report import *

# Create a model instance and optimize
instance = model.create_instance('U_2015_08_27.dat')

# Create a solver
opt = SolverFactory('glpk')
results = opt.solve(instance)
#instance.display()

print('--- Solve FINISHED ---')

my_dict = yaml.safe_load(open('results.yml'))
abc = my_dict['Solution'][1]['Variable']

dfResults =  pd.DataFrame.from_dict(abc, orient='index' )
dfResults.reset_index(level=0, inplace=True)
dfResults.rename({'index':'old'}, axis=1, inplace=True)



# http://hselab.org/pyomo-get-variable-values.html
# http://math.jacobs-university.de/oliver/teaching/jacobs/spring2016/ilme202/files/
# http://math.jacobs-university.de/oliver/teaching/jacobs/spring2016/ilme202/files/20160210d-HL-A3_1-Steelworks.html
 
#res = instance.NewCapacity.get_values()

# or
#list_of_vars =[v.get_values() for v in instance.component_objects(ctype=Var, active=True, descend_into=True)]
#
#var_names =[v.name for v in instance.component_objects(ctype=Var, active=True, descend_into=True)]
#
#print(list_of_vars)
#print(var_names)

## YAML stuff

#from yaml
#import yaml
#import yamlordereddictloader

 
#with open("results.yml") as f:
#    yaml_data = yaml.load(f, Loader=yamlordereddictloader.Loader)

#import pandas as pd

# https://pyomo.readthedocs.io/en/latest/working_models.html
