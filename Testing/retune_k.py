class Employee:
    num_of_emps = 0
    raised_amount = 1.2

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raised(self):
        self.pay = int(self.pay * self.raised_amount)




emp1 = Employee("kory", "shanw", 231)
emp1.raised_amount = 1.3
print(isinstance(emp1, Employee))

print(emp1.pay)
print(emp1.apply_raised())
print(emp1.pay)

