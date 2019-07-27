# write values to CSV
# https://groups.google.com/forum/#!topic/pyomo-forum/nbynW4EPTMk

# construct loop to write primal values for NewCapacity variable
with open('my_results.csv', 'w') as f:
   f.write('REGION, TECHNOLOGY, YEAR,  VALUE\n')
   for r in instance.REGION:
      for t in instance.TECHNOLOGY:
         for y in instance.YEAR:
            f.write('%s, %s, %s, %s\n' % (r, t, y, instance.NewCapacity[r,t,y].value))

# next: pass list of variables and perform loop for them