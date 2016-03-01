people = int(input("How many people? "))
pizzas = int(input("How many pizzas do you have? "))
slices_per_pizza = int(input("How many slices do the pizzas have? "))

total_slices = pizzas * slices_per_pizza
slices_per_person = total_slices / people

print("{} people with {} pizzas".format(people, pizzas))
print("Each person gets {} pieces of pizza.".format(slices_per_person))
