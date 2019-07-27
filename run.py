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

print('Solve FINISHED')

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








# from yaml
#import yaml
#import yamlordereddictloader
 
#with open("results.yml") as f:
#    yaml_data = yaml.load(f, Loader=yamlordereddictloader.Loader)

# using the PULP code
# save the results
#from pulp_report import *
#results_df = pd.DataFrame(columns=[
#        'SCENARIO',
#        'VAR_NAME',
#        'VAR_VALUE',
#        'REGION',
#        'REGION2',
#        'DAYTYPE',
#        'EMISSION',
#        'FUEL',
#        'DAILYTIMEBRACKET',
#        'SEASON',
#        'TIMESLICE',
#        'MODE_OF_OPERATION',
#       'STORAGE',
#       'TECHNOLOGY',
#       'YEAR',
#        'FLEXIBLEDEMANDTYPE'])

#results_df = save_results_to_dataframe(results_df, instance, 'utopia')
#print("Results are saved. -- Current date/time:", dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

#import pandas as pd

# https://pyomo.readthedocs.io/en/latest/working_models.html
