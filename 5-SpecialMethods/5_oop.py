# ============================================================
# Magic/Dunder Method
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

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return f"{self.fullname()} - {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

# Unit testing
kevin = Employee('kevin', 'zhang', 6000)
brandon = Employee('brandon', 'zhang', 8000)
repr(kevin)
print(kevin)

print(1+2)
# same as below
print(int.__add__(1, 2))

kevin + brandon

len(kevin)