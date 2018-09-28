# ============================================================
# Property Decorator 
# ============================================================
print("\n"*20)

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last):
        self.first = first
        self.last = last

    # property decator allows us to access a method like an attribute
    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, new_name):
        new_first, new_last = new_name.split(" ")
        self.first = new_first
        self.last = new_last

    @fullname.deleter
    def fullname(self):
        print('deleting name ...')
        self.first = None
        self.last = None

# Unit testing
kevin = Employee('kevin', 'zhang')
print(kevin.first)
print(kevin.email)
print(kevin.fullname)

kevin.first = 'xxx'
print(kevin.first)
print(kevin.email)
print(kevin.fullname)

# change the name
kevin.fullname = 'BestKevin **Zhang**'
print(kevin.fullname)

# delete the name
del kevin.fullname
print(kevin.fullname)
