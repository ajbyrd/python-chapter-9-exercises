class Pizza:

    def __init__(self):
        self.size = ""
        self.crust = ""
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)

    def print_order(self):
        print(f"You ordered a {self.size} inch {self.crust} crust pizza with {self.toppings[0]} and {self.toppings[1]}.")

pizza_one = Pizza()

pizza_one.size = 12
pizza_one.crust = "thin"
pizza_one.add_topping("pepperoni")
pizza_one.add_topping("sausage")
pizza_one.print_order() 

pizza_two = Pizza()

pizza_two.size = 16
pizza_two.crust = "stuffed"
pizza_two.add_topping("bacon")
pizza_two.add_topping("kiwi")
pizza_two.print_order() 
        