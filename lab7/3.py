import random
def get_rand_list(A, B, N):
  mylist = []
  for var in range(N):
    mylist.append(random.sample(range(A, B)))
  return mylist
def get_overlap(A, B):
  C = []
  for x in range(len(A)):
    if A[x] in B:
      C.append(A[x])
  return C