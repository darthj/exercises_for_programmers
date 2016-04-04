puts "How many people?"
people = gets.chomp

puts "How many pizzas?"
pizzas = gets.chomp

puts "How many slices do the pizzas have?"
slices_per_pizza = gets.chomp

total_slices = pizzas.to_i * slices_per_pizza.to_i
slices_per_person = total_slices.to_i / people.to_i
remaining_slices = total_slices.to_i % people.to_i

puts "#{people} with #{pizzas}"
puts "Each person gets #{slices_per_person} pieces of pizza."
puts "There are #{remaining_slices} leftover."
