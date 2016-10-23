cars = 100 # Here I defined my quantity of cars. It's important because I later will use people for which car
space_in_a_car = 4.0 #the floating point seems not need on this equation as I don't have broken number of pax to calculate
drivers = 30
passengers = 90
cars_not_driven = cars - drivers #cars_not_driven need to be defined because the amount of drivers are different than the number of cars available
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passenger_per_car = passengers / cars_driven
travel_times = space_in_a_car * cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passenger_per_car, "in each car."
print "We need to travel", travel_times, "times."
