##when there is unknown no. of arguments
def pizza(size,flavour,*toppings):
    print(f"The size of pizza is{size},while flavour I like is{flavour},along with these toppings {toppings}")
pizza(15,"FAJITA","Cheese","Garlic")

#output
#The size of pizza is15,while flavour I like isFAJITA,along with these toppings ('Cheese', 'Garlic')

#but *parameters always be in last