import random

#Part A
weeks = 16
print ("Weeks:",weeks, type(weeks))

classes_per_week = 3 
print ("Classes per week:",classes_per_week, type(classes_per_week))

classes = 5
print ("Classes:",classes, type(classes))

tuition = 6000
print("Tuition: $",tuition, type(tuition))
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
cost_per_class = (cost_per_week/classes_per_week)
print("Okay! so the cost per class is $", cost_per_class)

#Part B
my_list = ["f", 3, 4, "blaze", "12.2","words","more_words","even_more_words"]
result = random.choice(my_list)
print(result)