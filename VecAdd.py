def vecAddition(V1,V2):
  '''
  This function adds to vectors together. A is equal to an empty list and if the lengths of V1 and V2 do not equal, then the algorithim
  will return none. If they are equal, then we take the length of V1 and add each element of the list together and then
  we return the list A.
  '''
  A = [ ]
  #A is an empty list.
  if len(V1) != len(V2):
    print('error')
    return None
  #If the lengths of the lists V1 and V2 do not equal each other, then this prints an error and returns none.
  for i in range(len(V1)):
    A.append(V1[i] + V2[i])
    #This adds the lengths of V1 and V2 and adds each element of the list together.
  return A
  #This returns the list A.

V1 = [1,2]
V2 = [3,4]
print(vecAddition(V1,V2))
