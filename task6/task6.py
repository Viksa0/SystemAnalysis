def task(csvString):
  from io import StringIO
  import json
  import csv
  import numpy as np
  f = StringIO(csvString)
  reader = csv.reader(f, delimiter=',')
  u = []
  for row in reader:
    u.append(row)
    
  def get_table(u, col):
    t = np.zeros(np.array(u).shape)
    for i in range(t.shape[1]):
      for j in range(t.shape[0]):
        if (u[i][col] < u[j][col]):
          t[i,j] = 1
        elif (u[i][col] == u[j][col]):
          t[i,j] = 0.5
        else:
          t[i,j] = 0
    return t
  t = []

  for i in range(len(u)):
    t.append(get_table(u, i))
  x  = np.zeros((len(u), len(u)))

  for i in range(len(u)):
    x += t[i]
  x = x/len(u)
  k0 = np.array([1/len(u)]*len(u))
  e = 0.001
  y = x.dot(k0)
  l = (np.ones(len(u))).dot(y)
  k1 = 1/l*y
  while (abs(max(k1-k0))>=e):
    k0 = k1
    y = x.dot(k0)
    l = (np.ones(len(u))).dot(y)
    k1 = 1/l*y
  for i in range(len(k1)):
    k1[i] = round(k1[i], 3)
  return(json.dumps(k1.tolist()))
