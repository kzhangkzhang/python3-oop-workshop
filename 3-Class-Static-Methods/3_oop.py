# ============================================================
# Classes and Instances Variables
# ============================================================
print("\n"*20)


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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # it is very common using class method as alternate class constructor
    # to create object
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))

    @staticmethod
    def is_workday(day):
        l_return_value = True
        # 0: monday ... 5: Saturday, 6: Sunday
        if day.weekday() in [5, 6]:
            l_return_value = False

        return l_return_value


# Unit testing
kevin = Employee('kevin', 'zhang', 5000)
brandon = Employee('brandon', 'zhang', 6000)

print(Employee.raise_amt)
print(kevin.raise_amt)
print(brandon.raise_amt)

# class method can only be invoked by class or instance of class (object)
Employee.set_raise_amt(1.5)
print(Employee.raise_amt)
print(kevin.raise_amt)
print(brandon.raise_amt)
# call class method via object is also work. But typically we call class
# method via class, not class object
kevin.set_raise_amt(1.7)
print(Employee.raise_amt)
print(kevin.raise_amt)
print(brandon.raise_amt)

# using class method as alternate constructor to create class object
elena = Employee.from_string('elena-zhang-80000')
print(elena.fullname())

import datetime
d1 = datetime.date(2018, 9, 28)
print(Employee.is_workday(d1))      # True 2018/9/28 - Friday

d2 = datetime.date(2018, 9, 29)
print(Employee.is_workday(d2))      # False 2018/9/29 - Saturday
