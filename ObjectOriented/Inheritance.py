# python 3.5.2

class Employee(object):

    def __init__(self, _name_first, _name_last):
        self.name_first = _name_first
        self.name_last = _name_last
        self.hours = 0

    def calculate_wage(self):
        return self.hours * 20.00

    def name(self):
        return self.name_first + " " + self.name_last


class PartTimeEmployee(Employee):

    def calculate_wage(self):
        return self.hours * 12.00


print (" *** Full-Time Employee *** ");
milton=Employee("Milton", "Smith")
milton.hours = 12

print("Employee Name: " + milton.name())
print("Monthly Salary: " + str( milton.calculate_wage()))



print("\n"*2)
print (" *** Part-Time Employee *** ");
ken=PartTimeEmployee("Ken", "Jones")
ken.hours = 12

print("Employee Name: " + ken.name())
print("Monthly Salary: " + str( ken.calculate_wage()))

