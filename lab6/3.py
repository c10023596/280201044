employees = {}
pawns_i = input("Names of employees with , between them: ")
salaries_i = input("Their payments with , between them: ")
pawns = ["pawn1","pawn2","pawn3","pawn4","pawn5"]
salaries = [350, 470, 438, 217, 387]
for i in range(len(pawns)):
  employees[salaries[i]]=pawns[i]
salaries.sort()
print(employees[salaries[-1]],employees[salaries[-2]],employees[salaries[-3]])