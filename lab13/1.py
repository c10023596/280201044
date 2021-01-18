def selection_sort(the_list, out=[]):

  for x in range(len(the_list)):
    for i in range(1, len(the_list)-1):
      if the_list[i]<the_list[i+1]:
        smallest = the_list[i]
        index = i
      else:
        smallest = the_list[i+1]
        index = i+1
  
    swap1 = the_list[x]
    swap2 = the_list[index]

    the_list[x] = swap2
    the_list[index] = swap1
  return the_list


print(selection_sort([43, 342, 343, 2, 34]))