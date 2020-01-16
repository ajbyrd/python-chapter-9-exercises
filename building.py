import datetime

class Building():
    def __init__(self, address, stories):
        self.designer = "Adam Byrd"
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories

    def construct(self):
        self.date_constructed = datetime.datetime.now()
    
    def purchase(self, owner):
        self.owner = owner

eight_hundred_eighth = Building("800 8th Street", 12)
building_two = Building("2203 Lindell Avenue", 2)
building_three = Building("301 Plus Park Blvd", 5)
building_four = Building("315 Deaderick Street", 28)
building_five = Building("401 Bowling Avenue", 3)


eight_hundred_eighth.purchase("Nick Saban")
building_two.purchase("Allen Parker")
building_three.purchase("John")
building_four.purchase("Sergio")
building_five.purchase("Wilson")

eight_hundred_eighth.construct()
building_two.construct()
building_three.construct()
building_four.construct()
building_five.construct()


print(f"{eight_hundred_eighth.address} was purchased by {eight_hundred_eighth.owner} on {eight_hundred_eighth.date_constructed} and has {eight_hundred_eighth.stories} stories.")
print(f"{building_two.address} was purchased by {building_two.owner} on {building_two.date_constructed} and has {building_two.stories} stories.")
print(f"{building_three.address} was purchased by {building_three.owner} on {building_three.date_constructed} and has {building_three.stories} stories.")
print(f"{building_four.address} was purchased by {building_four.owner} on {building_four.date_constructed} and has {building_four.stories} stories.")
print(f"{building_five.address} was purchased by {building_five.owner} on {building_five.date_constructed} and has {building_five.stories} stories.")



