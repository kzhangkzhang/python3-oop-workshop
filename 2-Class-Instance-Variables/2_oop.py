# ============================================================
# Classes and Instances Variables
# ============================================================


class Employee:

    # class variable
    raise_amt = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f"{self.first}.{self.last}@knowles.com"
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        # pay attention I am using self.raise_amt, not
        # Employee.raise_amt here so that we can raise
        # for a particular employee
        self.pay = int(self.pay * self.raise_amt)


# Unit testing
print(Employee.num_of_emps)
kevin = Employee('kevin', 'zhang', 5000)
print(Employee.num_of_emps)
print(kevin.__dict__)
print(Employee.__dict__)
print(kevin.pay)
kevin.apply_raise()
print(kevin.pay)
print(kevin.raise_amt)
print(Employee.raise_amt)

# change raise_amount via object
kevin.raise_amt = 1.10
print(kevin.__dict__)
print(kevin.raise_amt)
print(Employee.raise_amt)
