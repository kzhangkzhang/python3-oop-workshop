# ============================================================
# Classes Inheritance
# ============================================================
print("\n"*20)


class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.20

    def __init__(self, first, last, pay, prog_lang):
        # Method A: using super - preferred
        super().__init__(first, last, pay)
        # Method B: using class, need pass self
        # Employee.__init__(self, first, last, pay)

        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

    # using list comprehension
    # https://stackoverflow.com/questions/37084246/printing-using-list-comprehension
    def print_emps2(self):
        print(*(emp.fullname() for emp in self.employees), sep='\n')


# Unit testing
# help(Developer)     # pay attention to Method resolution order


kevin = Developer('kevin', 'zhang', 5000, 'Python/Oracle/Javascript')
print(kevin.prog_lang)
brandon = Developer('brandon', 'zhang', 5000, 'Python/Oracle/Javascript')

ying = Manager('ying', 'wang', 80000, [kevin, brandon])
print(isinstance(ying, Manager))    # True
print(isinstance(ying, Employee))   # True
print(isinstance(ying, Developer))   # Flase

print(issubclass(Developer, Employee))   # True
print(issubclass(Manager, Developer))   # False

ying.print_emps()
ying.print_emps2()


elena = Developer('elena', 'zhang', 5000, 'Javascript')

ying.add_emp(elena)
ying.print_emps2()

ying.remove_emp(brandon)
ying.print_emps2()
