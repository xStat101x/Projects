"""#Start with some designs that need to be printed.
Unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

#simulate printed each design, until none are left.
#move each design to completed_models after printing.
while Unprinted_designs:
    current_design = Unprinted_designs.pop()
    #simulate creating 3d print from the design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)

#display all completed models.
print("\nThe following models have been comprinted:")
for completed_model in completed_models:
    print(completed_model)
"""
def print_models(unprinted_designs, completed_models):
    '''
    Simulate printing each design, until none are left.
    Move each design to completed models after printing.
    '''
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        #simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    #Show all the models that were printed.
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)




