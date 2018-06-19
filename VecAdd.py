def vecAddition(V1,V2):
  A = [ ]
  if len(V1) != len(V2):
    print('error')
    return None
  for i in range(len(V1)):
    A.append(V1[i] + V2[i])
  return A


V1 = [1,2]
V2 = [3,4]
print(vecAddition(V1,V2))
