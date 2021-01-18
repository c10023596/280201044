def binary_search(sorted_list, low, high, x):

  if high >= low:
    mid = (high + low) // 2

    if sorted_list[mid] == x:
      return mid
    
    elif sorted_list[mid] < x:
      return binary_search(sorted_list, low, mid-1, x)
    
    else:
      return binary_search(sorted_list, mid+1, high, x)
  
  else:
    return -1


