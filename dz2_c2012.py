class Employee:
    def __init__(self, name, job, company):
        self.name = name
        self.job = job
        self.company = company
        print(f"Employee {self.name}, work as {self.job} at {self.company}")
    def change_name(self, new_name):
        self.name = new_name
        print(f"New name: {self.name}")
    def change_job(self, new_job):
        self.job = new_job
        print(f"New job: {self.job}")
    def change_company(self, new_company):
        self.company = new_company
        print(f"New company: {self.company}")
john = Employee("John", "Senior Game Developer", "Nintendo")
john.change_name("Ben")
john.change_job("UI Artist")
john.change_company("Sony")

natalia = Employee("Natalia", "Game Designer", "Valve")
natalia.change_company("EA")