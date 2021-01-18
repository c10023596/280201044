class Employee:

  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
  
  def get_name(self):
    return self.name
  
  def set_name(self, name):
    self.name = name
  
  def get_salary(self):
    return self.salary
  
  def set_salary(self, salary):
    self.salary = salary
  
  def display(name, salary):
    print(f"{name}{salary}")


class Company:

  def __init__(self):
    self.employee_list = []

  def get_employee_list(self):
    return self.employee_list
  
  def set_employee_list(self, employee_list):
    if type(employee_list) == list:
      self.employee_list = employee_list
  
  def add_employee(self, new_employee):
    if isinstance(new_employee, Employee):
      self.employee_list.append(new_employee)
  
  def calc_ave_salary(self):
    summ = 0
    for i in self.employee_list:
      summ += i.get_salary()
  
  def display(self):
    for i in self.employee_list:
      i.display()


employee1 = Employee("Recep", "2600")


employee2 = Employee("Huseyin", "2800")


companyA = Company()
companyA.add_employee(employee1)
companyA.add_employee(employee2)
companyA.display()