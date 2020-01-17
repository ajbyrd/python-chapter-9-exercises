class Employee():
    def __init__(self, name, job_title, start_date):
        self.name = name
        self.job_title = job_title
        self.start_date = start_date

class Company():
    def __init__(self, business_name, address, industry_type):
        self.business_name = business_name
        self.address = address
        self.industry_type = industry_type
        self.employees = list()

adam = Employee("Adam Byrd", "Software Engineer", "March 28th, 2020")
hank = Employee("Hank Byrd", "Branch Manager", "March 28th, 2020")
lilly = Employee("Lilly Holladay", "Assistant Branch Manager", "March 28th, 2020")
dwight = Employee("Dwight Schrute", "Assistant to the Regional Manager", "March 29th, 2020")
michael = Employee("Michael Scott", "Regional Manager", "March 29th, 2020")

dunder_mifflin = Company("Dunder Mifflin Paper Company", "1 Scranton Street", "Paper")
waterlogged = Company("Waterlogged", "2203 Lindell Avenue", "Outdoor Tech")

dunder_mifflin.employees.append(michael)
dunder_mifflin.employees.append(dwight)

waterlogged.employees.append(adam)
waterlogged.employees.append(hank)
waterlogged.employees.append(lilly)

print(f"{dunder_mifflin.business_name} is in the {dunder_mifflin.industry_type} industry and has the following employees: \n* {dunder_mifflin.employees[0].name} \n* {dunder_mifflin.employees[1].name} ")

print(f"{waterlogged.business_name} is in the {waterlogged.industry_type} industry and has the following employees: \n* {waterlogged.employees[0].name} \n* {waterlogged.employees[1].name} \n* {waterlogged.employees[2].name}")
