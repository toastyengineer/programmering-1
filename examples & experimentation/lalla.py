class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}{last}@tera.org".lower()

    def __str__(self):
        return f"{self.last} ; {self.first} ; {self.pay} SEK / Month"

    def fullname(self):
        return f"{self.first} {self.last}"


class Ceo(Employee):
    def __init__(self, first, last, pay):
        super().__init__(first, last, pay)

emp1 = Employee("Anton", "Lundmark", 43500)
print(emp1)
print(emp1.fullname())
print(emp1.email)