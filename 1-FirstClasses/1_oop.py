# ============================================================
# Classes and Instances
# ============================================================


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f"{self.first}.{self.last}@knowles.com"
        self.pay = pay

    def fullname(self):
        return f"{self.first} {self.last}"

# Unit testing
kevin = Employee('kevin', 'zhang', 5000)        
ying = Employee('ying', 'wang', 6000)

