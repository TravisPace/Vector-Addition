def vecAddition(V1,V2):
  '''
  This function adds to vectors together. A is equal to an empty list and if the lengths of V1 and V2 do not equal, then the algorithim
  will return none. If they are equal, then we take the length of V1 and add each element of the list together and then
  we return the list A.
  '''
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
