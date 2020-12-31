def pascal_triangle_line(n):
  if n == 1:
    return [1]
  else:
    base = [1]
    
    previous_line = pascal_triangle_line(n-1)

    for i in range(len(previous_line)-1):
      base.append(previous_line[i] + previous_line[i+1])
    base += [1]

    return base

print(pascal_triangle_line(4))