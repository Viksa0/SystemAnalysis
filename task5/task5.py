def task(str1, str2):
  import json
  import numpy as np
  dataA = json.loads(str1)
  dataB = json.loads(str2)
  def m(A):
    n = []
    for item in A:
      try:    
        n.append(int(item))
      except:
        m = []
        for i in range(len(item)):
          m.append(int(item[i]))
        n.append(m)
    return n
  def get_table(n):
    max = 0
    for l in n:
      try:
        if l > max:
          max = l
      except:
        for i in l:
          if i > max:
            max = i
    table = np.zeros((max,max)) 
    m = np.zeros(max)
    for item in n:
      try:
        m[item-1] = 1
        for j in range(max):
          if m[j] == 0:
            table[j, item-1] = 0
          else:
            table[j, item-1] = 1
      except:
        for l in item:
          m[l-1] = 1
        for l in item:
          for j in range(max):
            if m[j] == 0:
              table[j, l-1] = 0
            else:
              table[j, l-1] = 1
    return table
  def back_string(a):
    est = []
    for item in a:
      try:
        est.append(str(item + 1))
      except:
        m = []
        for l in item:
          m.append(str(l + 1))
        est.append(m)
    return est
  dataA = m(dataA)
  dataB = m(dataB)
  tableA = get_table(dataA)
  tableB = get_table(dataB)
  mergedTable = tableA * tableB + tableA.T * tableB.T
  answer = []
  for j in range(mergedTable.shape[1]):
    for i in range(j):
      if mergedTable[i,j] == 0:
        answer.append([i,j])
  return back_string(answer)
