class PizzaParty(object):
    def __init__(self):
        self.people = int(input("How many people? "))
        self.pizzas = int(input("How many pizzas do you have? "))
        self.slices_per_pizza = int(input("How many slices do the pizzas have? "))
        self.print_stats()

    def total_slices(self, pizzas, slices_per_pizza):
        return pizzas * slices_per_pizza

    def slices_per_person(self, total_slices_output, people):
        return total_slices_output / people

    def remaining_slices(self, total_slices_output, people):
        return total_slices_output % people

    def print_stats(self):
        print("{} people with {} pizzas.".format(self.people, self.pizzas))

        per_person_slices = self.total_slices(self.pizzas, self.slices_per_pizza)

        print("Each person gets {} pieces of pizza.".format(
            self.slices_per_person(per_person_slices, self.people)))

        print("There are {} slices leftover.".format(
            self.remaining_slices(per_person_slices, self.people)))

party = PizzaParty()
